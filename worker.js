importScripts("https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js");

let pyodide = null;

// This function is exposed to Pyodide. It makes a SYNCHRONOUS XMLHttpRequest.
// Because it runs in a Web Worker, it blocks this worker thread but NOT the main UI thread.
// The Service Worker intercepts this request, asks the main thread for input, and waits.
self.syncInput = function(promptText) {
    if (promptText) {
        // Send the prompt text to the main UI to display
        postMessage({ type: "stdout", text: promptText });
    }
    
    // Generate a unique ID for this input request
    const reqId = Math.random().toString(36).substring(2, 10);
    
    // Make synchronous HTTP request
    const req = new XMLHttpRequest();
    req.open('GET', `/_python_input?id=${reqId}`, false); // false = synchronous
    req.send(null);
    
    if (req.status === 200) {
        return req.responseText;
    }
    return "";
};

async function initPyodide() {
    try {
        pyodide = await loadPyodide({
            stdout: (text) => {
                postMessage({ type: "stdout", text: text + "\n" });
            },
            stderr: (text) => {
                postMessage({ type: "stderr", text: text + "\n" });
            }
        });

        // Override Python's built-in input() to use our synchronous JS function
        await pyodide.runPythonAsync(`
import builtins
import js

def _custom_input(prompt=""):
    return js.syncInput(prompt)

builtins.input = _custom_input
        `);

        postMessage({ type: "ready" });
    } catch (err) {
        postMessage({ type: "stderr", text: "Failed to initialize Pyodide: " + err.message });
    }
}

initPyodide();

self.addEventListener("message", async (e) => {
    if (e.data.type === "runCode") {
        if (!pyodide) {
            postMessage({ type: "stderr", text: "Python engine not loaded yet.\n" });
            postMessage({ type: "done" });
            return;
        }
        try {
            await pyodide.runPythonAsync(e.data.code);
            postMessage({ type: "done" });
        } catch (err) {
            postMessage({ type: "stderr", text: err.message + "\n" });
            postMessage({ type: "done" });
        }
    }
});

const inputResolvers = new Map();

self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);
    // Use endsWith to support GitHub Pages subpath deployments (e.g. /python_projects_300/_python_input)
    if (url.pathname.endsWith('_python_input')) {
        const id = url.searchParams.get('id');
        
        event.respondWith(new Promise((resolve) => {
            // Store the resolver function to respond when input is provided
            inputResolvers.set(id, (text) => {
                resolve(new Response(text, {
                    status: 200,
                    headers: { 
                        'Content-Type': 'text/plain',
                        'Cache-Control': 'no-store'
                    }
                }));
            });
            
            // Notify clients (main thread) that input is requested
            self.clients.matchAll({ includeUncontrolled: true }).then(clients => {
                clients.forEach(client => {
                    client.postMessage({ type: 'INPUT_REQUESTED', id: id });
                });
            });
        }));
    }
});

self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'INPUT_PROVIDED') {
        const resolver = inputResolvers.get(event.data.id);
        if (resolver) {
            resolver(event.data.text);
            inputResolvers.delete(event.data.id);
        }
    }
});

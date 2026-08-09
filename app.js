document.addEventListener("DOMContentLoaded", () => {
    let allProjects = [];
    let currentDifficulty = "all";
    let currentCategory = "all";
    let searchQuery = "";
    let sortOrder = "id-asc";

    const projectsGrid = document.getElementById("projects-grid");
    const visibleCountEl = document.getElementById("visible-count");
    const searchInput = document.getElementById("search-input");
    const categoryFiltersContainer = document.getElementById("category-filters");
    const difficultyPills = document.querySelectorAll("#difficulty-filters .pill");
    const sortSelect = document.getElementById("sort-select");

    // Modal elements
    const codeModal = document.getElementById("code-modal");
    const modalCloseBtn = document.getElementById("modal-close-btn");
    const modalTitle = document.getElementById("modal-project-title");
    const modalDiffBadge = document.getElementById("modal-diff-badge");
    const modalDesc = document.getElementById("modal-project-desc");
    const modalFolder = document.getElementById("modal-folder");
    const modalFilename = document.getElementById("modal-filename");
    const modalTags = document.getElementById("modal-tags");
    const modalCodeBlock = document.getElementById("modal-code-block");
    const copyCodeBtn = document.getElementById("copy-code-btn");
    const runCodeBtn = document.getElementById("run-code-btn");
    const terminalContainer = document.getElementById("terminal-container");
    const terminalOutput = document.getElementById("terminal-output");
    const clearTerminalBtn = document.getElementById("clear-terminal-btn");

    if (clearTerminalBtn) {
        clearTerminalBtn.addEventListener("click", () => {
            terminalOutput.textContent = "";
        });
    }

    let pythonWorker = null;
    let isExecuting = false;

    // Register Service Worker for synchronous input interception
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js').then((reg) => {
            console.log("Service Worker registered.", reg);
        }).catch((err) => {
            console.error("Service Worker registration failed:", err);
        });

        // Listen for messages from Service Worker (Input requests)
        navigator.serviceWorker.addEventListener('message', (event) => {
            if (event.data && event.data.type === 'INPUT_REQUESTED') {
                handleTerminalInput(event.data.id);
            }
        });
    }

    function initPythonWorker() {
        if (pythonWorker) return;
        pythonWorker = new Worker('worker.js');
        
        pythonWorker.addEventListener('message', (e) => {
            const data = e.data;
            if (data.type === 'ready') {
                runCodeBtn.textContent = "▶ Run Code";
                runCodeBtn.disabled = false;
            } else if (data.type === 'stdout') {
                terminalOutput.textContent += data.text;
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            } else if (data.type === 'stderr') {
                terminalOutput.innerHTML += `<span class="error">${data.text}</span>`;
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            } else if (data.type === 'done') {
                isExecuting = false;
                runCodeBtn.disabled = false;
                runCodeBtn.textContent = "▶ Run Code";
                terminalOutput.textContent += "\n>>> Execution Completed.\n";
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            }
        });
    }

    function handleTerminalInput(requestId) {
        // Create an input element right inside the terminal
        const inputField = document.createElement("span");
        inputField.contentEditable = "true";
        inputField.className = "terminal-input-active";
        
        terminalOutput.appendChild(inputField);
        inputField.focus();

        // Listen for Enter key
        inputField.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault();
                const text = inputField.textContent;
                
                // Lock the text in place
                inputField.contentEditable = "false";
                inputField.className = "";
                terminalOutput.appendChild(document.createTextNode("\n"));
                
                // Send answer back to Service Worker (Robust against hard-refresh null controller)
                if (navigator.serviceWorker.controller) {
                    navigator.serviceWorker.controller.postMessage({
                        type: 'INPUT_PROVIDED',
                        id: requestId,
                        text: text
                    });
                } else {
                    navigator.serviceWorker.ready.then(reg => {
                        if (reg.active) {
                            reg.active.postMessage({
                                type: 'INPUT_PROVIDED',
                                id: requestId,
                                text: text
                            });
                        }
                    });
                }
            }
        });
    }

    // Start loading Python environment in the background
    initPythonWorker();

    // Fetch projects_data.json
    fetch("projects_data.json")
        .then(response => response.json())
        .then(data => {
            allProjects = data;
            initCategories();
            renderProjects();
        })
        .catch(err => {
            console.error("Error loading projects data:", err);
            projectsGrid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: #ef4444;">Failed to load project catalog. Ensure projects_data.json is present.</div>`;
        });

    function initCategories() {
        const counts = {};
        allProjects.forEach(p => {
            counts[p.category] = (counts[p.category] || 0) + 1;
        });

        const sortedCats = Object.keys(counts).sort();
        
        sortedCats.forEach(cat => {
            const btn = document.createElement("button");
            btn.className = "cat-btn";
            btn.dataset.category = cat;
            btn.innerHTML = `
                <span>${cat}</span>
                <span class="count-badge">${counts[cat]}</span>
            `;
            btn.addEventListener("click", () => {
                document.querySelectorAll(".cat-btn").forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                currentCategory = cat;
                renderProjects();
            });
            categoryFiltersContainer.appendChild(btn);
        });

        // Add handler for 'All Categories'
        const allCatBtn = categoryFiltersContainer.querySelector('[data-category="all"]');
        allCatBtn.addEventListener("click", () => {
            document.querySelectorAll(".cat-btn").forEach(b => b.classList.remove("active"));
            allCatBtn.classList.add("active");
            currentCategory = "all";
            renderProjects();
        });
    }

    // Filter and Sort logic
    function filterProjects() {
        return allProjects.filter(p => {
            // Difficulty match
            const diffMatch = currentDifficulty === "all" || p.difficulty.toLowerCase() === currentDifficulty.toLowerCase();
            
            // Category match
            const catMatch = currentCategory === "all" || p.category === currentCategory;
            
            // Search query match
            const q = searchQuery.toLowerCase();
            const searchMatch = !q || 
                p.title.toLowerCase().includes(q) ||
                p.description.toLowerCase().includes(q) ||
                p.filename.toLowerCase().includes(q) ||
                p.tags.some(t => t.toLowerCase().includes(q));

            return diffMatch && catMatch && searchMatch;
        }).sort((a, b) => {
            if (sortOrder === "id-asc") return a.id - b.id;
            if (sortOrder === "id-desc") return b.id - a.id;
            if (sortOrder === "title-asc") return a.title.localeCompare(b.title);
            return 0;
        });
    }

    function renderProjects() {
        const filtered = filterProjects();
        visibleCountEl.textContent = filtered.length;

        if (filtered.length === 0) {
            projectsGrid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
                    <h3>No projects found</h3>
                    <p>Try adjusting your search query or filters.</p>
                </div>
            `;
            return;
        }

        projectsGrid.innerHTML = filtered.map(p => {
            const diffClass = `diff-${p.difficulty.toLowerCase()}`;
            const tagsHtml = p.tags.map(t => `<span class="tag">#${t}</span>`).join("");
            const formattedId = String(p.id).padStart(3, '0');

            return `
                <div class="project-card" data-id="${p.id}">
                    <div class="card-top">
                        <span class="project-id-badge">#${formattedId}</span>
                        <span class="diff-badge ${diffClass}">${p.difficulty}</span>
                    </div>
                    <div>
                        <h3 class="card-title">${p.title}</h3>
                        <p class="card-desc">${p.description}</p>
                    </div>
                    <div class="card-tags">
                        ${tagsHtml}
                    </div>
                    <div class="card-footer">
                        <span class="category-name">${p.category}</span>
                        <button class="view-code-btn">View Code &rarr;</button>
                    </div>
                </div>
            `;
        }).join("");

        // Attach click listeners to cards
        document.querySelectorAll(".project-card").forEach(card => {
            card.addEventListener("click", () => {
                const pid = parseInt(card.dataset.id, 10);
                const proj = allProjects.find(p => p.id === pid);
                if (proj) openModal(proj);
            });
        });
    }

    // Modal Handlers
    function openModal(proj) {
        const formattedId = String(proj.id).padStart(3, '0');
        modalTitle.textContent = `${formattedId}: ${proj.title}`;
        modalDiffBadge.textContent = proj.difficulty;
        modalDiffBadge.className = `diff-badge diff-${proj.difficulty.toLowerCase()}`;
        modalDesc.textContent = proj.description;
        modalFolder.textContent = proj.folder;
        modalFilename.textContent = proj.filename;
        modalTags.innerHTML = proj.tags.map(t => `<span class="tag">#${t}</span>`).join("");

        modalCodeBlock.textContent = proj.code;
        hljs.highlightElement(modalCodeBlock);

        // Reset terminal state
        terminalContainer.style.display = "none";
        terminalOutput.textContent = "";

        codeModal.classList.add("active");
    }

    function closeModal() {
        codeModal.classList.remove("active");
    }

    modalCloseBtn.addEventListener("click", closeModal);
    codeModal.addEventListener("click", (e) => {
        if (e.target === codeModal) closeModal();
    });

    // Copy to Clipboard
    copyCodeBtn.addEventListener("click", () => {
        const codeText = modalCodeBlock.textContent;
        navigator.clipboard.writeText(codeText).then(() => {
            copyCodeBtn.textContent = "✅ Copied!";
            setTimeout(() => {
                copyCodeBtn.textContent = "📋 Copy Code";
            }, 2000);
        });
    });

    // Run Code Listener
    runCodeBtn.addEventListener("click", () => {
        if (!pythonWorker || isExecuting) return;
        
        const codeText = modalCodeBlock.textContent;
        terminalContainer.style.display = "block";
        terminalOutput.textContent = "Executing...\n\n";
        
        isExecuting = true;
        runCodeBtn.disabled = true;
        runCodeBtn.textContent = "⏳ Running...";

        pythonWorker.postMessage({ type: "runCode", code: codeText });
    });

    // Search Input Listener
    searchInput.addEventListener("input", (e) => {
        searchQuery = e.target.value;
        renderProjects();
    });

    // Difficulty Pill Listeners
    difficultyPills.forEach(pill => {
        pill.addEventListener("click", () => {
            difficultyPills.forEach(p => p.classList.remove("active"));
            pill.classList.add("active");
            currentDifficulty = pill.dataset.difficulty;
            renderProjects();
        });
    });

    // Sort Select Listener
    sortSelect.addEventListener("change", (e) => {
        sortOrder = e.target.value;
        renderProjects();
    });
});

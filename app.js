document.addEventListener("DOMContentLoaded", () => {
    let allProjects = [];
    let currentDifficulty = "all";
    let currentCategory = "all";
    let currentSpecialFilter = "all"; // 'all', 'featured', 'input', 'compatible'
    let searchQuery = "";
    let sortOrder = "id-asc";
    let activeProject = null;

    const projectsGrid = document.getElementById("projects-grid");
    const featuredGrid = document.getElementById("featured-grid");
    const featuredSection = document.getElementById("featured-section");
    const visibleCountEl = document.getElementById("visible-count");
    const searchInput = document.getElementById("search-input");
    const categoryFiltersContainer = document.getElementById("category-filters");
    const difficultyPills = document.querySelectorAll("#difficulty-filters .pill");
    const sortSelect = document.getElementById("sort-select");

    // Stats elements
    const statTotal = document.getElementById("stat-total");
    const statBeginner = document.getElementById("stat-beginner");
    const statIntermediate = document.getElementById("stat-intermediate");
    const statAdvanced = document.getElementById("stat-advanced");

    // Modal elements
    const codeModal = document.getElementById("code-modal");
    const modalCloseBtn = document.getElementById("modal-close-btn");
    const modalTitle = document.getElementById("modal-project-title");
    const modalDiffBadge = document.getElementById("modal-diff-badge");
    const modalCompatBadge = document.getElementById("modal-compat-badge");
    const modalDesc = document.getElementById("modal-project-desc");
    const modalFolder = document.getElementById("modal-folder");
    const modalFilename = document.getElementById("modal-filename");
    const modalTags = document.getElementById("modal-tags");
    const modalGithubLink = document.getElementById("modal-github-link");
    const modalReadmeLink = document.getElementById("modal-readme-link");
    const modalCodeBlock = document.getElementById("modal-code-block");
    const copyCodeBtn = document.getElementById("copy-code-btn");
    const runCodeBtn = document.getElementById("run-code-btn");
    const terminalContainer = document.getElementById("terminal-container");
    const terminalOutput = document.getElementById("terminal-output");
    const clearTerminalBtn = document.getElementById("clear-terminal-btn");
    const clearSearchBtn = document.getElementById("clear-search-btn");
    const downloadCodeBtn = document.getElementById("download-code-btn");
    const execTimerBadge = document.getElementById("exec-timer-badge");
    const themeToggleBtn = document.getElementById("theme-toggle");
    let executionStartTime = 0;

    // Theme Management
    const savedTheme = localStorage.getItem("theme") || "dark";
    document.body.dataset.theme = savedTheme;
    if (themeToggleBtn) {
        themeToggleBtn.textContent = savedTheme === "light" ? "☀️ Light" : "🌙 Dark";
        themeToggleBtn.addEventListener("click", () => {
            const current = document.body.dataset.theme === "light" ? "dark" : "light";
            document.body.dataset.theme = current;
            localStorage.setItem("theme", current);
            themeToggleBtn.textContent = current === "light" ? "☀️ Light" : "🌙 Dark";
        });
    }

    // Search Highlight Helper
    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function highlightText(text, query) {
        if (!query || !text) return text;
        const regex = new RegExp(`(${escapeRegExp(query.trim())})`, 'gi');
        return text.replace(regex, '<mark class="highlight-match">$1</mark>');
    }

    const userInputSection = document.getElementById("user-input-section");
    const dynamicInputsContainer = document.getElementById("dynamic-inputs");
    const inputValidationMsg = document.getElementById("input-validation-msg");

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
                if (data.text.includes('\x1bc')) {
                    terminalOutput.textContent = data.text.replace(/\x1bc/g, '');
                } else {
                    terminalOutput.textContent += data.text;
                }
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            } else if (data.type === 'stderr') {
                if (!terminalOutput.innerHTML.includes('PYTHON ERROR')) {
                    terminalOutput.innerHTML += `<div class="python-error-banner">⚠️ PYTHON ERROR</div>`;
                }
                terminalOutput.innerHTML += `<span class="error">${data.text}</span>`;
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            } else if (data.type === 'done') {
                isExecuting = false;
                runCodeBtn.disabled = false;
                runCodeBtn.textContent = "▶ Run Code";
                const dynamicSubmitBtn = document.getElementById("dynamic-submit-btn");
                if (dynamicSubmitBtn) {
                    dynamicSubmitBtn.disabled = false;
                    dynamicSubmitBtn.innerHTML = "▶ Submit & Run Code";
                    dynamicSubmitBtn.style.opacity = "1";
                    dynamicSubmitBtn.style.cursor = "pointer";
                }

                if (executionStartTime && execTimerBadge) {
                    const elapsedMs = Math.round(performance.now() - executionStartTime);
                    execTimerBadge.textContent = `⚡ ${elapsedMs}ms`;
                    execTimerBadge.style.display = "inline-block";
                }

                terminalOutput.textContent += "\n>>> Execution Completed.\n";
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            }
        });
    }

    function handleTerminalInput(requestId) {
        if (window.inputQueue && window.inputQueue.length > 0) {
            const text = window.inputQueue.shift();
            // Send answer back to Service Worker
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
            terminalOutput.textContent += text + "\n";
            terminalOutput.scrollTop = terminalOutput.scrollHeight;
            return;
        }

        // Create interactive prompt fallback inside the terminal
        const inputField = document.createElement("input");
        inputField.type = "text";
        inputField.className = "terminal-input-active";
        inputField.autocomplete = "off";
        
        terminalOutput.appendChild(inputField);
        inputField.focus();
        terminalOutput.scrollTop = terminalOutput.scrollHeight;

        inputField.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault();
                const text = inputField.value;
                inputField.remove();
                terminalOutput.appendChild(document.createTextNode(text + "\n"));
                
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

    // Start loading Python environment in background
    initPythonWorker();

    // Fetch projects_data.json
    fetch("projects_data.json")
        .then(response => response.json())
        .then(data => {
            allProjects = data;
            updateStats();
            initCategories();
            renderFeaturedProjects();
            renderProjects();
            handleInitialHash();
        })
        .catch(err => {
            console.error("Error loading projects data:", err);
            projectsGrid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: #ef4444; padding: 40px;">Failed to load project catalog.</div>`;
        });

    function updateStats() {
        if (!statTotal) return;
        statTotal.textContent = allProjects.length;
        statBeginner.textContent = allProjects.filter(p => p.difficulty.toLowerCase() === 'beginner').length;
        statIntermediate.textContent = allProjects.filter(p => p.difficulty.toLowerCase() === 'intermediate').length;
        statAdvanced.textContent = allProjects.filter(p => p.difficulty.toLowerCase() === 'advanced').length;
    }

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

        const allCatBtn = categoryFiltersContainer.querySelector('[data-category="all"]');
        allCatBtn.addEventListener("click", () => {
            document.querySelectorAll(".cat-btn").forEach(b => b.classList.remove("active"));
            allCatBtn.classList.add("active");
            currentCategory = "all";
            renderProjects();
        });
    }

    function updateCategoryCounts() {
        const filteredForCats = allProjects.filter(p => {
            const diffMatch = currentDifficulty === "all" || p.difficulty.toLowerCase() === currentDifficulty.toLowerCase();
            
            let specialMatch = true;
            if (currentSpecialFilter === "featured") specialMatch = p.featured === true;
            else if (currentSpecialFilter === "input") specialMatch = p.requiresInput === true;
            else if (currentSpecialFilter === "compatible") specialMatch = p.browserCompatibility === "compatible";

            const q = searchQuery.toLowerCase();
            const searchMatch = !q || 
                String(p.id).includes(q) ||
                p.title.toLowerCase().includes(q) ||
                p.description.toLowerCase().includes(q) ||
                p.filename.toLowerCase().includes(q) ||
                (p.tags && p.tags.some(t => t.toLowerCase().includes(q))) ||
                (p.code && p.code.toLowerCase().includes(q));

            return diffMatch && specialMatch && searchMatch;
        });

        const counts = {};
        filteredForCats.forEach(p => {
            counts[p.category] = (counts[p.category] || 0) + 1;
        });

        document.querySelectorAll(".cat-btn").forEach(btn => {
            if (btn.dataset.category === "all") {
                const badge = btn.querySelector(".count-badge");
                if (badge) badge.textContent = filteredForCats.length;
            } else {
                const cat = btn.dataset.category;
                const count = counts[cat] || 0;
                const badge = btn.querySelector(".count-badge");
                if (badge) badge.textContent = count;
                
                if (count === 0 && currentCategory !== cat) {
                    btn.style.opacity = "0.4";
                    btn.style.pointerEvents = "none";
                } else {
                    btn.style.opacity = "1";
                    btn.style.pointerEvents = "auto";
                }
            }
        });
    }

    function renderFeaturedProjects() {
        if (!featuredGrid) return;
        const featuredList = allProjects.filter(p => p.featured === true);
        
                if (featuredList.length === 0) {
            featuredSection.style.display = "none";
            return;
        }

        featuredSection.style.display = "block";
        featuredGrid.innerHTML = featuredList.map(p => {
            const formattedId = String(p.id).padStart(3, '0');
            const diffClass = `diff-${p.difficulty.toLowerCase()}`;
            const highlightedTitle = highlightText(p.title, searchQuery);
            const highlightedDesc = highlightText(p.description, searchQuery);
            return `
                <div class="featured-card" data-id="${p.id}">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span class="featured-badge">⭐ Featured</span>
                            <span class="diff-badge ${diffClass}">${p.difficulty}</span>
                        </div>
                        <h4 style="font-size: 0.95rem; font-weight: 700; color: #fff; margin-bottom: 4px;">#${formattedId}: ${highlightedTitle}</h4>
                        <p style="font-size: 0.85rem; color: var(--text-muted);">${highlightedDesc}</p>
                    </div>
                    <button class="view-code-btn" style="align-self: flex-start; margin-top: 8px;">View Project &rarr;</button>
                </div>
            `;
        }).join("");

        featuredGrid.querySelectorAll(".featured-card").forEach(card => {
            card.addEventListener("click", () => {
                const pid = parseInt(card.dataset.id, 10);
                const proj = allProjects.find(p => p.id === pid);
                if (proj) openModal(proj);
            });
        });
    }

    function filterProjects() {
        return allProjects.filter(p => {
            // Difficulty match
            const diffMatch = currentDifficulty === "all" || p.difficulty.toLowerCase() === currentDifficulty.toLowerCase();
            
            // Category match
            const catMatch = currentCategory === "all" || p.category === currentCategory;
            
            // Special filter match
            let specialMatch = true;
            if (currentSpecialFilter === "featured") specialMatch = p.featured === true;
            else if (currentSpecialFilter === "input") specialMatch = p.requiresInput === true;
            else if (currentSpecialFilter === "compatible") specialMatch = p.browserCompatibility === "compatible";

            // Search query match
            const q = searchQuery.toLowerCase();
            const searchMatch = !q || 
                String(p.id).includes(q) ||
                p.title.toLowerCase().includes(q) ||
                p.description.toLowerCase().includes(q) ||
                p.filename.toLowerCase().includes(q) ||
                (p.tags && p.tags.some(t => t.toLowerCase().includes(q))) ||
                (p.code && p.code.toLowerCase().includes(q));

            return diffMatch && catMatch && specialMatch && searchMatch;
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
        
        updateCategoryCounts();

        if (filtered.length === 0) {
            projectsGrid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
                    <h3>No projects match your filter</h3>
                    <p>Try adjusting your search term or active category filters.</p>
                </div>
            `;
            return;
        }

        projectsGrid.innerHTML = filtered.map(p => {
            const diffClass = `diff-${p.difficulty.toLowerCase()}`;
            const tagsHtml = p.tags ? p.tags.map(t => `<span class="tag">#${t}</span>`).join("") : "";
            const formattedId = String(p.id).padStart(3, '0');
            const compatBadge = p.browserCompatibility === "compatible" ? `<span class="compat-badge compat-compatible">💻 Ready</span>` : (p.browserCompatibility === "limited" ? `<span class="compat-badge compat-limited">⚠️ Limited</span>` : `<span class="compat-badge compat-terminal_only">🖥️ Terminal</span>`);
            const highlightedTitle = highlightText(p.title, searchQuery);
            const highlightedDesc = highlightText(p.description, searchQuery);

            return `
                <div class="project-card" data-id="${p.id}">
                    <div class="card-header">
                        <span class="project-id">#${formattedId}</span>
                        <div style="display: flex; gap: 6px;">
                            ${compatBadge}
                            <span class="diff-badge ${diffClass}">${p.difficulty}</span>
                        </div>
                    </div>
                    <h3 class="project-title">${highlightedTitle}</h3>
                    <p class="project-desc">${highlightedDesc}</p>
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
        activeProject = proj;
        const formattedId = String(proj.id).padStart(3, '0');
        modalTitle.textContent = `${formattedId}: ${proj.title}`;
        modalDiffBadge.textContent = proj.difficulty;
        modalDiffBadge.className = `diff-badge diff-${proj.difficulty.toLowerCase()}`;
        
        // Compatibility badge
        const compatText = proj.browserCompatibility === "compatible" ? "💻 Browser Ready" : (proj.browserCompatibility === "limited" ? "⚠️ Limited Support" : "🖥️ Terminal Only");
        modalCompatBadge.textContent = compatText;
        modalCompatBadge.className = `compat-badge compat-${proj.browserCompatibility}`;

        modalDesc.textContent = proj.description;
        modalFolder.textContent = proj.folder;
        modalFilename.textContent = proj.filename;
        modalTags.innerHTML = proj.tags ? proj.tags.map(t => `<span class="tag">#${t}</span>`).join("") : "";

        if (proj.githubUrl) {
            modalGithubLink.href = proj.githubUrl;
            modalGithubLink.style.display = "inline-flex";
        } else {
            modalGithubLink.style.display = "none";
        }

        if (proj.readmeUrl) {
            modalReadmeLink.href = proj.readmeUrl;
            modalReadmeLink.style.display = "inline-flex";
        } else {
            modalReadmeLink.style.display = "none";
        }

        modalCodeBlock.textContent = proj.code;
        hljs.highlightElement(modalCodeBlock);

        // Reset validation & terminal state
        inputValidationMsg.style.display = "none";
        inputValidationMsg.textContent = "";
        dynamicInputsContainer.innerHTML = "";
        terminalOutput.textContent = "";

        const hasInputs = proj.requiresInput && proj.inputPrompts && proj.inputPrompts.length > 0;
        window.currentProjectHasInputs = hasInputs;

        if (hasInputs) {
            // Single Run Button Logic: Hide header run button when inputs are required to avoid duplicates
            runCodeBtn.style.display = "none";
            userInputSection.style.display = "block";
            terminalContainer.style.display = "flex";

            proj.inputPrompts.forEach((promptText, idx) => {
                const group = document.createElement("div");
                group.className = "input-group";
                
                const label = document.createElement("label");
                label.className = "input-label";
                label.textContent = promptText;
                
                const inputEl = document.createElement("input");
                inputEl.type = "text";
                inputEl.className = "dynamic-input";
                inputEl.dataset.idx = idx;
                inputEl.dataset.prompt = promptText;
                
                inputEl.addEventListener("keydown", (e) => {
                    if (e.key === "Enter") {
                        e.preventDefault();
                        const next = dynamicInputsContainer.querySelector(`input[data-idx="${idx + 1}"]`);
                        if (next) {
                            next.focus();
                        } else {
                            executeProgram();
                        }
                    }
                });

                group.appendChild(label);
                group.appendChild(inputEl);
                dynamicInputsContainer.appendChild(group);
            });

            // Single Submit & Run button inside input form
            const submitBtn = document.createElement("button");
            submitBtn.className = "input-submit-btn";
            submitBtn.id = "dynamic-submit-btn";
            submitBtn.innerHTML = "▶ Submit & Run Code";
            submitBtn.addEventListener("click", () => {
                executeProgram();
            });
            dynamicInputsContainer.appendChild(submitBtn);

            setTimeout(() => {
                const firstInput = dynamicInputsContainer.querySelector("input");
                if (firstInput) firstInput.focus();
            }, 100);
        } else {
            // No inputs required: Show header run code button
            runCodeBtn.style.display = "inline-flex";
            userInputSection.style.display = "none";
            terminalContainer.style.display = "none";
        }

        codeModal.classList.add("active");
        document.body.classList.add("modal-open");
        window.location.hash = `#/project/${formattedId}`;
    }

    function closeModal() {
        activeProject = null;
        codeModal.classList.remove("active");
        document.body.classList.remove("modal-open");
        if (window.location.hash.startsWith("#/project/")) {
            history.pushState("", document.title, window.location.pathname + window.location.search);
        }
    }

    function executeProgram() {
        if (!pythonWorker || isExecuting) return;

        // Input validation
        window.inputQueue = [];
        if (window.currentProjectHasInputs) {
            const inputEls = document.querySelectorAll("#dynamic-inputs .dynamic-input");
            for (let el of inputEls) {
                const val = el.value;
                if (val === undefined || val === null || val.trim() === "") {
                    inputValidationMsg.textContent = `⚠️ Please enter a value for: "${el.dataset.prompt}"`;
                    inputValidationMsg.style.display = "block";
                    el.focus();
                    return;
                }
            }
            inputValidationMsg.style.display = "none";
            inputEls.forEach(el => {
                window.inputQueue.push(el.value);
            });
        }

        const codeText = modalCodeBlock.textContent;
        terminalContainer.style.display = "flex";
        terminalOutput.textContent = "Executing...\n\n";
        if (execTimerBadge) {
            execTimerBadge.style.display = "none";
        }
        executionStartTime = performance.now();
        
        isExecuting = true;
        runCodeBtn.disabled = true;
        runCodeBtn.textContent = "⏳ Running...";
        const dynamicSubmitBtn = document.getElementById("dynamic-submit-btn");
        if (dynamicSubmitBtn) {
            dynamicSubmitBtn.disabled = true;
            dynamicSubmitBtn.innerHTML = "⏳ Running...";
            dynamicSubmitBtn.style.opacity = "0.7";
            dynamicSubmitBtn.style.cursor = "not-allowed";
        }

        pythonWorker.postMessage({ type: "runCode", code: codeText });
    }

    function handleInitialHash() {
        const hash = window.location.hash;
        if (hash && hash.startsWith("#/project/")) {
            const pidStr = hash.replace("#/project/", "");
            const pid = parseInt(pidStr, 10);
            if (!isNaN(pid)) {
                const proj = allProjects.find(p => p.id === pid);
                if (proj) openModal(proj);
            }
        }
    }

    window.addEventListener("hashchange", () => {
        handleInitialHash();
    });

    modalCloseBtn.addEventListener("click", closeModal);
    codeModal.addEventListener("click", (e) => {
        if (e.target === codeModal) closeModal();
    });

    // Copy to Clipboard
    copyCodeBtn.addEventListener("click", () => {
        if (!activeProject) return;
        navigator.clipboard.writeText(activeProject.code).then(() => {
            copyCodeBtn.textContent = "✅ Copied!";
            setTimeout(() => {
                copyCodeBtn.textContent = "📋 Copy Code";
            }, 2000);
        });
    });

    // Download Code (.py)
    if (downloadCodeBtn) {
        downloadCodeBtn.addEventListener("click", () => {
            if (!activeProject || !activeProject.code) return;
            const blob = new Blob([activeProject.code], { type: "text/x-python;charset=utf-8" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = activeProject.filename || `project_${activeProject.id}.py`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        });
    }

    // Run Code Listener for Header button
    runCodeBtn.addEventListener("click", () => {
        executeProgram();
    });

    // Clear Search Listener
    if (clearSearchBtn) {
        clearSearchBtn.addEventListener("click", () => {
            searchInput.value = "";
            searchQuery = "";
            clearSearchBtn.style.display = "none";
            renderProjects();
        });
    }

    // Search Listener
    searchInput.addEventListener("input", (e) => {
        searchQuery = e.target.value;
        if (clearSearchBtn) {
            clearSearchBtn.style.display = searchQuery ? "flex" : "none";
        }
        renderProjects();
    });

    // Real-Time Keyboard Input Listener for Interactive Games (Project 116)
    document.addEventListener("keydown", (e) => {
        if (!isExecuting || !codeModal.classList.contains("active")) return;
        if (activeProject && (activeProject.id === 116 || activeProject.filename.includes("snake"))) {
            const key = e.key;
            const validKeys = ["w", "a", "s", "d", "p", "r", "q", "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"];
            if (validKeys.includes(key.toLowerCase()) || key.startsWith("Arrow")) {
                e.preventDefault();
                if (pythonWorker) {
                    pythonWorker.postMessage({ type: "keypress", key: key });
                }
            }
        }
    });

    // Difficulty & Special Pill Listeners
    difficultyPills.forEach(pill => {
        pill.addEventListener("click", () => {
            difficultyPills.forEach(p => p.classList.remove("active"));
            pill.classList.add("active");
            
            if (pill.dataset.difficulty) {
                currentDifficulty = pill.dataset.difficulty;
                currentSpecialFilter = "all";
            } else if (pill.dataset.filter) {
                currentDifficulty = "all";
                currentSpecialFilter = pill.dataset.filter;
            }
            renderProjects();
        });
    });

    // Sort Select Listener
    sortSelect.addEventListener("change", (e) => {
        sortOrder = e.target.value;
        renderProjects();
    });
});

/* AVRY Discovery Shared UI Engine */
const NAV_ITEMS = [
    { name: "Home", path: "index.html", icon: "home" },
    { name: "Reports", path: "reports.html", icon: "file-text" },
    { name: "Code Analysis", path: "code-analysis.html", icon: "zap" },
    { name: "VPS Analysis", path: "vps.html", icon: "server" },
    { name: "Tests", path: "tests.html", icon: "check-circle" },
    { name: "Documentation", path: "documentation.html", icon: "book-open" },
    { name: "Visualizations", path: "visualization.html", icon: "map" }
];

function injectSidebar() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    if (currentPath === 'index.html') return; // No sidebar on Home

    const sidebar = document.createElement('aside');
    sidebar.className = 'sidebar';
    
    let menuHtml = `
        <a href="index.html" style="text-decoration: none;"><h2>AVRY</h2></a>
        <nav class="nav-menu">
    `;
    
    NAV_ITEMS.forEach(item => {
        const isActive = currentPath === item.path;
        menuHtml += `
            <a href="${item.path}" class="nav-item ${isActive ? 'active' : ''}">
                <i data-feather="${item.icon}"></i> ${item.name}
            </a>
        `;
    });
    
    menuHtml += `</nav>`;
    sidebar.innerHTML = menuHtml;
    
    const container = document.getElementById('app-container');
    if (container) {
        container.prepend(sidebar);
        if (typeof feather !== 'undefined') feather.replace();
    }
}

// Unified Modal Logic
function injectModal() {
    if (document.getElementById('modal')) return;
    const modal = document.createElement('div');
    modal.id = 'modal';
    modal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modal-title" style="margin:0; color:var(--accent); font-family:'Fira Code', monospace; font-size:14px;"></h3>
                <button onclick="closeModal()" style="background: none; border: none; color: #666; cursor: pointer;"><i data-feather="x"></i></button>
            </div>
            <div class="modal-body">
                <pre><code id="code-box" class="language-python"></code></pre>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

async function openCode(path) {
    injectModal();
    const modal = document.getElementById('modal');
    const title = document.getElementById('modal-title');
    const codeBox = document.getElementById('code-box');
    
    title.innerText = path;
    codeBox.textContent = "Loading content...";
    modal.style.display = 'block';

    try {
        const resp = await fetch(`data/vault/${path}`);
        if (!resp.ok) throw new Error("File not found");
        const code = await resp.text();
        codeBox.textContent = code;
        if (typeof Prism !== 'undefined') Prism.highlightElement(codeBox);
    } catch (e) {
        codeBox.textContent = `Error loading file: ${path}\n\nMake sure the file exists in data/vault/`;
    }
    if (typeof feather !== 'undefined') feather.replace();
}

function closeModal() {
    const modal = document.getElementById('modal');
    if (modal) modal.style.display = 'none';
}

// Unified Table Loader
async function loadTableData(dataFile, targetElementId, filterType = null) {
    try {
        const resp = await fetch(`data/${dataFile}`);
        let data = await resp.json();
        if (filterType) {
            data = data.filter(d => d.type === filterType || (d.path && d.path.toLowerCase().includes(filterType.toLowerCase())));
        }
        
        const body = document.getElementById(targetElementId);
        if (!body) return;
        body.innerHTML = "";

        data.forEach(d => {
            const tr = document.createElement('tr');
            tr.style.cursor = 'pointer';
            
            const fileName = d.name || d.path.split('/').pop();
            const description = d.description || "System documentation asset.";
            const timestamp = d.timestamp || "2026-05-15 22:00:00";
            const path = d.path || d.file || "";

            tr.onclick = () => openCode(path);
            tr.innerHTML = `
                <td><span style="color:var(--accent); font-weight:600;">${fileName}</span></td>
                <td style="color: #999;">${description}</td>
                <td style="color: #666; font-size: 12px;">${timestamp}</td>
            `;
            body.appendChild(tr);
        });
    } catch (e) {
        console.error(`Error loading ${dataFile}:`, e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    injectSidebar();
    injectModal();
    if (typeof feather !== 'undefined') feather.replace();
});

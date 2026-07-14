
const form = document.getElementById("searchForm");
const input = document.getElementById("parametro");
const textArea = document.getElementById("resultContainer");
const btn = document.getElementById("submitBtn");

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const query = input.value.trim();
    if (!query) return;

    textArea.style.display = 'block';
    textArea.innerHTML = "<em>Ricerca e analisi in corso con l'LLM... attendi...</em>";
    btn.disabled = true;

    try {
        const response = await fetch(`https://llm-wikipedia-research.onrender.com/q?parametro=${encodeURIComponent(query)}`);

        if (!response.ok) throw new Error("Errore del server ${response.status}");

        const data = await response.json();
        textArea.style.whiteSpace = "pre-line";
        textArea.textContent = data.analisi;
    } catch (error) {
        textArea.innerHTML = `<span style="color: #e74c3c;">❌ Si è verificato un errore: ${error.message}</span>`;
    } finally {
        btn.disabled = false;
    }
});
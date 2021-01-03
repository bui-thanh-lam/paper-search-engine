const searchBtn = document.querySelector(".search-button");
const input = document.querySelector("input");
const rankBtn = document.querySelector(".text-rank-button");
const results = document.querySelector(".results");

input.addEventListener("input", (e) => {
    e.preventDefault();
    query = e.target.value;
});

function clearResults() {
    results.innerHTML = '';
}

function displayResult(json) {
    let length = json.n_results;
    let resultsElement = document.createElement("div");
    resultsElement.innerHTML = `
    <p>Found ${length} result(s).</p>
    `;
    results.appendChild(resultsElement);
    for (let i = 0; i < length; i++) {
        let paper = json.results[i];
        let paperElement = document.createElement("div");
        paperElement.innerHTML = `
        <h3>${paper.title}</h3>
        <p>Abstract: ${paper.abstract}</p>
        <p>Year: ${paper.time}</p>
        <p>Venue: ${paper.venue}</p>    
        <hr>                    
        `;
        results.appendChild(paperElement);
    }
}

async function normalSearch(query) {
    const response = await fetch(`http://localhost:8000/search/normal/?q=${query}`);
    const resultJson = await response.json();
    displayResult(resultJson);
}

async function textRankSearch(query) {
    const response = await fetch(`http://localhost:8000/search/text-rank/?q=${query}`);
    const resultJson = await response.json();
    displayResult(resultJson);
}

searchBtn.addEventListener("click", () => {
    clearResults();
    if (!input.value) {
        return;
    } else {
        normalSearch(input.value);
    }
});

rankBtn.addEventListener("click", () => {
    clearResults();
    if (!input.value) {
        return;
    } else {
        json = textRankSearch(input.value);
    }
});

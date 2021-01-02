const searchBtn = document.querySelector(".search-button");
const input = document.querySelector("input");
const rankBtn = document.querySelector(".text-rank-button");

input.addEventListener("input", (e) => {
    e.preventDefault();
    query = e.target.value;
});

async function normalSearch(query) {
    const response = await fetch(`http://localhost:8000/search/normal/?q=${query}`);
    const result = await response.json();
    console.log(result);
}

async function textRankSearch(query) {
    const response = await fetch(`http://localhost:8000/search/text-rank/?q=${query}`);
    const result = await response.json();
    console.log(result);
}

searchBtn.addEventListener("click", () => {
    if (!input.value) {
        return;
    } else {
        normalSearch(input.value);
    }
});

rankBtn.addEventListener("click", () => {
    if (!input.value) {
        return;
    } else {
        textRankSearch(input.value);
    }
});

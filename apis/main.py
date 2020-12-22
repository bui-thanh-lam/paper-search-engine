from fastapi import FastAPI
import uvicorn
from database import repository as repo
from apis.rankers import TextRank

papers = []

app = FastAPI()


@app.get("/search/{keyword}")
def search(keyword):
    global papers
    papers = repo.search(keyword)
    return repo.search(keyword)


@app.get("/ranking/best-items/")
def rank_by_quality():
    global papers
    scores = TextRank(papers)
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
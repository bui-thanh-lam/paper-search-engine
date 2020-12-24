from fastapi import FastAPI
import uvicorn
import numpy as np
from database import repository as repo
from apis.rankers import text_rank, vectorize

papers = []

app = FastAPI()


@app.get("/search/{keyword}")
def search(keyword):
    global papers
    papers = repo.search(keyword)
    return {'results': papers,
            'n_results': len(papers)}


@app.get("/ranking/best-items/")
def rank_by_quality():
    global papers
    docs = [p['title'] + p['abstract'] for p in papers]
    scores = np.array(text_rank(vectorize(docs)))
    indexes = (-scores).argsort()
    sorted_results = []
    for index in indexes:
        p = papers[index]
        p['score'] = scores[index]
        sorted_results.append(p)
    return {'results': sorted_results,
            'n_results': len(sorted_results)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
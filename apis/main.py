from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from database import repository as repo
from apis.rankers import text_rank, vectorize

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search/normal/{query}")
def search(q):
    papers = repo.search(q)
    if len(papers) == 0:
        return {
            'query': q,
            'results': [],
            'n_results': 0
        }
    return {
        'query': q,
        'results': papers,
        'n_results': len(papers)
    }


@app.get("/search/text-rank/{query}")
def rank_by_quality(q):
    papers = repo.search(q)
    if len(papers) == 0:
        return {
            'query': q,
            'results': [],
            'n_results': 0
        }
    docs = [p['title'] + p['abstract'] for p in papers]
    scores = np.array(text_rank(vectorize(docs)))
    indexes = (-scores).argsort()
    sorted_results = []
    for index in indexes:
        p = papers[index]
        p['score'] = scores[index]
        sorted_results.append(p)
    return {
        'query': q,
        'results': sorted_results,
        'n_results': len(sorted_results)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
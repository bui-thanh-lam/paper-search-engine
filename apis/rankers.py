import numpy as np
from nltk.tokenize import word_tokenize


def vectorize(docs):
    docs = docs
    bow = []
    vectors = []
    for doc in docs:
        toks = word_tokenize(doc)
        toks = [word.lower() for word in toks if word.isalpha()]
        for tok in toks:
            if tok not in bow:
                bow.append(tok)
    for doc in docs:
        toks = word_tokenize(doc)
        toks = [word.lower() for word in toks if word.isalpha()]
        vector = [0] * len(bow)
        for tok in toks:
            vector[bow.index(tok)] += 1
        vectors.append(vector)
    vectors = np.array(vectors)
    return vectors


def cosine_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        return 0
    else:
        return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))


def normalize(vec):
    sum = np.sum(vec)
    return [float(element/sum) for element in vec]


def TextRank(vectors, n_epochs=10, d=0.85):
    vectors = np.array(vectors)
    n_nodes = vectors.shape[0]
    graph = np.zeros((n_nodes, n_nodes))
    for i in range(n_nodes):
        for j in range(n_nodes):
            if i == j:
                continue
            graph[i][j] = cosine_distance(vectors[i], vectors[j])
            graph[j][i] = cosine_distance(vectors[i], vectors[j])
    scores = np.full(n_nodes, 1.0/n_nodes)
    for _ in range(n_epochs):
        for i in range(n_nodes):
            prev_scores = scores
            update = 0
            for j in range(n_nodes):
                update += graph[j][i] / np.sum(graph[j]) * prev_scores[j]
            scores[i] += (1-d)*prev_scores[i] + d*update
        scores = normalize(scores)
    return scores


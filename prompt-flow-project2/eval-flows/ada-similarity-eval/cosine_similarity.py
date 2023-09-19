from promptflow import tool

import numpy as np
from numpy.linalg import norm


@tool
def cosine_similarity(groundtruth: list[float], prediction: list[float]):

    cosine_similarity = np.dot(groundtruth, prediction) / (norm(groundtruth) * norm(prediction))
    return cosine_similarity

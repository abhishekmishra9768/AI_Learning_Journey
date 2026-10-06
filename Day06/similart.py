"""Day 06 - Similarity helper.

Purpose: cosine_similarity() scores how close two embedding vectors are.
"""

import numpy as np


def cosine_similarity(vector1, vector2):
    """Return how similar two embedding vectors are.

    The result is close to 1 for similar meaning and close to 0 for unrelated text.
    """

    v1 = np.array(vector1)
    v2 = np.array(vector2)

    # dot product divided by the product of the vector lengths
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

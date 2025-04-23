import numpy as np


class DummyMatch:
    def __init__(self, queryIdx, trainIdx, distance):
        self.queryIdx = queryIdx  # index in des1
        self.trainIdx = trainIdx  # index in des2
        self.distance = distance
# __________end of block__________



def match_key_points_numpy(des1: np.ndarray, des2: np.ndarray) -> list:
    """
    Match descriptors using brute-force matching with cross-check.

    Args:
        des1 (np.ndarray): Descriptors from image 1, shape (N1, D)
        des2 (np.ndarray): Descriptors from image 2, shape (N2, D)

    Returns:
        List[DummyMatch]: Sorted list of mutual best matches.
    """

    #YOUR CODE HERE

    dist_matrix = (np.sum(des1 ** 2, axis=1, dtype='f')[:, np.newaxis] + np.sum(des2 ** 2, axis=1) - 2 * np.dot(des1, des2.T)) ** 0.5

    matches = []

    for i in range(dist_matrix.shape[0]):
        arm = np.argmin(dist_matrix[i, :])
        #print(i, arm, np.argmin(dist_matrix[:, arm]))
        if np.argmin(dist_matrix[:, arm]) == i:
            matches.append(DummyMatch(i, arm, dist_matrix[i, arm]))


    return sorted(matches, key=lambda x: x.distance)

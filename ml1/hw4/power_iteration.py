import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """

    ### YOUR CODE HERE
    x = np.ones(data.shape[0])
    for i in  range(num_steps):
        y = data.dot(x)
        x = y / np.sqrt(np.sum(np.power(y, 2)))
        #print('y is', y)
        #print('norm is', np.sqrt(np.sum(np.power(y, 2))))
        #print('x is', x, end='\n\n')

    return float(data.dot(x).dot(x).item() / x.dot(x)), x

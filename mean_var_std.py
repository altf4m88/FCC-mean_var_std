import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.array(list).reshape(3, 3)
    flatten_array = array.flatten()

    calculations = {
        'mean': [
            np.mean(array, axis=0).tolist(),
            np.mean(array, axis=1).tolist(),
            np.mean(flatten_array).item()
        ],
        'variance': [
            np.var(array, axis=0).tolist(),
            np.var(array, axis=1).tolist(),
            np.var(flatten_array).item()
        ],
        'standard deviation': [
            np.std(array, axis=0).tolist(),
            np.std(array, axis=1).tolist(),
            np.std(flatten_array).item()
        ],
        'max': [
            np.max(array, axis=0).tolist(),
            np.max(array, axis=1).tolist(),
            np.max(flatten_array).item()
        ],
        'min': [
            np.min(array, axis=0).tolist(),
            np.min(array, axis=1).tolist(),
            np.min(flatten_array).item()
        ],
        'sum': [
            np.sum(array, axis=0).tolist(),
            np.sum(array, axis=1).tolist(),
            np.sum(flatten_array).item()
        ]
    }

    return calculations
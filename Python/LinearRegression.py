import numpy as np

class LinearRegression:
    def __init__(self,lr: float = 0.01, n_iters: int = 1_000):
        self.lr , self.n_iters = lr, n_iters
        self.w, self.bias = None,0.0 

    def fit(self, X: np.ndarray, y: np.ndarray)-> None:
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        for _ in range (self.n_iters):
            y_pred = X @ self.w + self.bias
            error = y_pred - y

    def prdict(self, X: np.ndarray)-> np.ndarray:
        return X @ self.w + self.bias
import numpy as np
from numpy.random import random_sample

class Kmeans:
    def __init__(self, n_clusters = 3,max_iter = 100, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
    
    def fit(self, X):
        n_samples = X.shape[0]
        rng = np.random.default_rng()
        self.centroids = X[rng.choice(n_samples, self.n_clusters, replace = False)]

        for i in range (self.max_iter):
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis = 2)
            self.labels = np.argmin(distances, axis = 1)

            new_centroids = np.array([X[self.labels == i].mean(axis = 0)
            for i in range(self.n_clusters)])
            
            if np.all(np.linalg.norm(self.centroids - new_centroids, axis = 1)<- self.tol):
                break
            self.centroids = new_centroids
    
    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis  = 2)
        return np.argmin(distances, axis = 1)


if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

    model = Kmeans(n_clusters=4, max_iter=300)
    model.fit(X)
    y_pred = model.predict(X)

    print("Centroids: ",model.centroids)
    print('sample assignments: ',y_pred[:20])
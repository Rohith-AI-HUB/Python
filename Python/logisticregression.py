import numpy as np

class LogisticRegression:
    """
    Simple logistic regression classifier using gradient descent.
    """

    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def compute_loss(self, y_true, y_pred):
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def fit(self, X, y):
        """
        Fit the model to the data using gradient descent.
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.n_iters):
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(linear_model)

            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict_proba(self, X):
        """
        Predict probability estimates for samples in X.
        """
        if self.weights is None or self.bias is None:
            raise Exception("Model is not trained yet. Call fit() before predict().")
        linear_model = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_model)

    def predict(self, X, threshold=0.5):
        """
        Predict binary class labels for samples in X.
        """
        probs = self.predict_proba(X)
        return (probs >= threshold).astype(int)

    def score(self, X, y, threshold=0.5):
        """
        Return the mean accuracy on the given test data and labels.
        """
        preds = self.predict(X, threshold)
        return np.mean(preds == y)

if __name__ == "__main__":
    from sklearn.datasets import make_classification
    X, y = make_classification(
        n_samples=1000,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        random_state=42
    )
    model = LogisticRegression(lr=0.01, n_iters=1000)
    model.fit(X, y)
    accuracy = model.score(X, y)
    print("Accuracy: ", accuracy)
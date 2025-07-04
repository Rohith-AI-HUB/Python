import numpy as np
class DecisionTree:

    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None
    
    def gini_impurity(self, labels):
        classes, counts = np.unique(labels, return_counts = True)
        impurity = 1 - np.sum((counts/len(labels))**2)
        return impurity

    def split_dataset(self, X, y, feature_idx, threshold):
        left_idx = X[:, feature_idx] <= threshold
        right_idx = X[:, feature_idx] > threshold
        return X[left_idx], X[right_idx], y[left_idx], y[right_idx]

    def best_split(self, X, y):
        best_gain = 0
        best_feature, best_thres = None, None
        parent_gini = self.gini_impurity(y)

        n_features = X.shape[1]

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for t in thresholds:
                X_left, X_right, y_left, y_right =self.split_dataset(X, y, feature, t)
                if len(y_left)==0 or len(y_right)==0:
                    continue
                gini = (len(y_left)/len(y)) * self.gini_impurity(y_left) + \
                       (len(y_right)/len(y)) * self.gini_impurity(y_right)
                info_gain = parent_gini - gini
                if info_gain > best_gain:
                    best_gain = info_gain
                    best_feature = feature
                    best_thres = t

        return best_feature, best_thres

    def build_tree(self, X, y, depth = 0, max_depth = 3):
        if len(set(y))==1 or depth == max_depth:
            return {"leaf": True, "class": np.bincount(y).argmax()}

        feat, thresh = self.best_split(X, y)
        if feat is None:
            return {"leaf": True, "class": np.bincount(y).argmax()}
        
        X_left, X_right, y_left, y_right = self.split_dataset(X, y, feat, thresh)
        return{
            "leaf": False,
            "feature": feat,
            "threshold": thresh,
            "left": self.build_tree(X_left, y_left, depth+1, max_depth),
            "right": self.build_tree(X_right, y_right, depth+1, max_depth)
        }

    def fit(self, X, y, max_depth=3):
        self.root = self.build_tree(X, y, max_depth=max_depth)

    def predict(self, X):
        def traverse(tree, sample):
            if tree["leaf"]:
                return tree["class"]
            if sample[tree["feature"]] <= tree["threshold"]:
                return traverse(tree["left"], sample)
            else:
                return traverse(tree["right"], sample)
        if isinstance(X, np.ndarray) and X.ndim == 1:
            return traverse(self.root, X)
        else:
            return np.array([traverse(self.root, x) for x in X])

if __name__ == "__main__":
    from sklearn.datasets import load_iris

    X, y = load_iris(return_X_y=True)
    dt = DecisionTree()
    dt.fit(X, y, max_depth=3)
    print(dt.predict(X[0]))
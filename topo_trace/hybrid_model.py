import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

class HybridClassifier:
    def __init__(self):
        self.model = GradientBoostingClassifier()
        self.is_fitted = False
    
    def fit(self, topo_features, gnn_embeddings, y):
        X = np.concatenate([topo_features, gnn_embeddings], axis=1)
        self.model.fit(X, y)
        self.is_fitted = True

    def predict(self, topo_features, gnn_embeddings):
        X = np.concatenate([topo_features, gnn_embeddings], axis=1)
        return self.model.predict(X)
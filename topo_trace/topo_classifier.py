import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

class TopoClassifier:
    def __init__(self, model=None):
        self.model = model or RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_fitted = False

    def _flatten_features(self, feature_dicts):

        features = []
        for feat in feature_dicts:
            row = []
            for dim in ["H0", "H1", "H2"]:
                for key in ["num_features", "max_lifetime", "avg_lifetime", "num_long_cycles"]:
                    row.append(feat.get(dim, {}).get(key, 0.0))
            features.append(row)
        return np.array(features)

    def fit(self, X_dicts, y):
        X = self._flatten_features(X_dicts)
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_fitted = True

    def predict(self, X_dicts):
        if not self.is_fitted:
            raise RuntimeError("Model not fitted yet.")
        X = self._flatten_features(X_dicts)
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def predict_proba(self, X_dicts):
        if not self.is_fitted:
            raise RuntimeError("Model not fitted yet.")
        X = self._flatten_features(X_dicts)
        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)
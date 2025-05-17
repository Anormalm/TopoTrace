def rule_based_anomaly_score(feature_dict, weights=None):
    if weights is None:
        weights = {
            "H0_num" : 0.2,
            "H0_avg_life": 0.2,
            "H1_num": 0.2,
            "H1_max_life": 0.4
        }
    H0 = feature_dict.get("H0", {})
    H1 = feature_dict.get("H1", {})
    details = {
        "H0_num": weights["H0_num"] * H0.get("num_features", 0),
        "H0_avg_life": weights["H0_avg_life"] * H0.get("avg_lifetime", 0.0),
        "H1_num": weights["H1_num"] * H1.get("num_features", 0),
        "H1_max_life": weights["H1_max_life"] * H1.get("max_lifetime", 0.0),
    }
    score = sum(details.values())
    return score, details
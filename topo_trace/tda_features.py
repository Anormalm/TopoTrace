import numpy as np

def summarize_diagram(diagram, threshold=0.05):
    if len(diagram) == 0:
        return {
            "num_features": 0,
            "max_lifetime": 0.0,
            "avg_lifetime": 0.0,
            "num_long_cycles": 0,
        }
    birth = diagram[:, 0]
    death = diagram[:, 1]
    lifetime = death - birth
    lifetime = lifetime[np.isfinite(lifetime)]  
    if len(lifetime) == 0:
        return {
            "num_features": 0,
            "max_lifetime": 0.0,
            "avg_lifetime": 0.0,
            "num_long_cycles": 0,
        }

    return {
        "num_features": int(len(lifetime)),
        "max_lifetime": float(np.max(lifetime)),
        "avg_lifetime": float(np.mean(lifetime)),
        "num_long_cycles": int(np.sum(lifetime > threshold)),
    }

def summarize_all(diagrams):
    summary = {}
    for dim, diagram in enumerate(diagrams):
        summary[f"H{dim}"] = summarize_diagram(diagram)
    return summary


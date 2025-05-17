# topo_trace/visualizer.py

import matplotlib.pyplot as plt
from persim import plot_diagrams
import numpy as np

def plot_annotated_diagram(diagrams, annotate_top_n=1, save_path=None, title="TopoTrace Diagram"):

    fig, ax = plt.subplots(figsize=(8, 6))
    plot_diagrams(diagrams, show=False, ax=ax, title=title)

    for dim, dgm in enumerate(diagrams):
        if len(dgm) == 0:
            continue

        lifetimes = dgm[:, 1] - dgm[:, 0]
        top_idxs = np.argsort(-lifetimes)[:annotate_top_n]

        for idx in top_idxs:
            birth, death = dgm[idx]
            ax.annotate(f"H{dim}: {round(death - birth, 2)}",
                        xy=(birth, death),
                        xytext=(birth + 0.1, death + 0.1),
                        arrowprops=dict(arrowstyle="->", color='black'),
                        fontsize=8)
        print(diagrams)
    return fig
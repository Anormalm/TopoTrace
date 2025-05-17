import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams  

def compute_persistent_homology(points, maxdim=2):
    result = ripser(points, maxdim=maxdim)
    return result['dgms']

def visualize_diagrams(diagrams, title="Persistence Diagram"):
    plot_diagrams(diagrams, show=True, title=title)

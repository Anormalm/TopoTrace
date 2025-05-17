import numpy as np
import json
import csv

def load_csv_path(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = [list(map(float, row)) for row in reader if row]
    return np.array(data)

def load_json_path(filename):
    with open(filename, 'r') as f:
        raw = json.load(f)
    data = [[pt["x"], pt["y"]] for pt in raw]
    return np.array(data)

def load_npy(filename):
    return np.load(filename)


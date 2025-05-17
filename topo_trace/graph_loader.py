import pandas as pd
import torch
from torch_geometric.data import Data
from sklearn.preprocessing import LabelEncoder

def load_edge_csv(filepath):
    df = pd.read_csv(filepath)
    le = LabelEncoder()
    nodes = pd.concat([df['source'], df['target']]).unique()
    le.fit(nodes)
    edge_index = torch.tensor([le.transform(df['source']), le.transform(df['target'])], dtype=torch.long)
    edge_index = edge_index.contiguous()
    num_nodes = len(le.classes_)
    x = torch.eye(num_nodes)
    return Data(x=x, edge_index=edge_index), le.classes_
    
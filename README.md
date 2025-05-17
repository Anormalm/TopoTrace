# TopoTrace

**TopoTrace** is a topology-aware behavior fingerprinting toolkit that extracts persistent homology patterns from trace data — such as robot paths, transaction graphs, or network activity — and uses them for anomaly detection and classification.

## Features

- Persistent homology computation (Ripser)
- Barcode and diagram visualization
- Topological feature extraction (H₀, H₁, H₂)
- Rule-based and ML-based anomaly scoring
- GNN integration for graph traces
- Streamlit-based web UI
- Supports CSV, JSON, edge lists

## Usage

```bash
streamlit run app.py
```
Or use as a Python module.

## Examples
See the examples/ folder for robot and graph traces.

## Installation

```bash
pip install -e .
```
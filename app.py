# app.py

import streamlit as st
import numpy as np
import os
import matplotlib.pyplot as plt

from topo_trace.data_loader import load_csv_path, load_json_path
from topo_trace.homology import compute_persistent_homology
from topo_trace.tda_features import summarize_all
from topo_trace.anomaly_detector import rule_based_anomaly_score
from topo_trace.visualizer import plot_annotated_diagram

# Optional hybrid classifier (you must load your trained model yourself)
from topo_trace.hybrid_model import HybridClassifier
# You can load your saved model here (not implemented in this minimal version)

# Set page config
st.set_page_config(page_title="TopoTrace", layout="wide")

# Title
st.title("TopoTrace: Topological Behavior Fingerprinting")

# Upload file
uploaded_file = st.file_uploader("Upload a trace file (.csv or .json)", type=["csv", "json"])
filetype = st.selectbox("Select input file type", ["csv", "json"])

if uploaded_file:
    filename = "temp_uploaded.csv" if filetype == "csv" else "temp_uploaded.json"
    with open(filename, "wb") as f:
        f.write(uploaded_file.read())

    # Load file
    if filetype == "csv":
        points = load_csv_path(filename)
    else:
        points = load_json_path(filename)

    st.subheader("1. Trace Preview")
    st.dataframe(points)

    # Compute persistent homology
    diagrams = compute_persistent_homology(points, maxdim=1)

    st.subheader("2. Persistence Diagram")
    fig = plot_annotated_diagram(diagrams, annotate_top_n=2)
    st.pyplot(fig)

    # Extract features
    features = summarize_all(diagrams)

    st.subheader("3. Topological Features")
    st.json(features)

    # Anomaly score
    score, breakdown = rule_based_anomaly_score(features)
    st.subheader("4. Rule-Based Anomaly Score")
    st.metric("Score", f"{score:.3f}")
    st.json(breakdown)

    # Loop detection
    loop_detected = features["H1"]["num_long_cycles"] > 0
    st.subheader("5. Loop Detection")
    st.success("Loop detected in trace (H1 > 0)!") if loop_detected else st.info("No topological loops detected.")

    # Optional hybrid classifier (extend here)
    if "HybridClassifier" in globals():
        st.subheader("6. ML Classifier (Optional)")
        st.info("You can add a trained classifier for live prediction.")
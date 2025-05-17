import argparse

from data_loader import load_csv_path, load_json_path
from homology import compute_persistent_homology, visualize_diagrams

def run_pipeline(input_file: str, filetype: str):
    if filetype == 'csv':
        points = load_csv_path(input_file)
    elif filetype == 'json':
        points = load_json_path(input_file)
    else:
        raise ValueError("Unsupported file type. Use 'csv' or 'json'.")
    diagrams = compute_persistent_homology(points)
    visualize_diagrams(diagrams, title=f"TopoTrace: {input_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run TopoTrace on trace data.")
    parser.add_argument("input_file", type=str, help="Path to the input file.")
    parser.add_argument("filetype", type=str, choices=['csv', 'json'], help="Type of the input file.")
    args = parser.parse_args()
    run_pipeline(args.input_file, args.filetype)
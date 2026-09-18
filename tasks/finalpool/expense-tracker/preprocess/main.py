# Preprocess script for expense-tracker
# This script prepares the workspace before evaluation

def preprocess(workspace_path):
    """Prepare the workspace for expense-tracker evaluation."""
    import os
    # Create necessary directories
    os.makedirs(os.path.join(workspace_path, "data"), exist_ok=True)
    print("Preprocessing complete for expense-tracker")

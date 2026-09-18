# Evaluation script for expense-tracker
# This script checks if the implementation meets the requirements

def evaluate(workspace_path):
    """Evaluate the expense-tracker implementation."""
    results = {"passed": True, "checks": []}
    
    # Check if main implementation file exists
    import os
    main_file = os.path.join(workspace_path, "expense_tracker.py")
    if os.path.exists(main_file):
        results["checks"].append({"name": "main_file_exists", "passed": True})
    else:
        results["checks"].append({"name": "main_file_exists", "passed": False})
        results["passed"] = False
    
    return results

# Import necessary modules using dynamic import
import sys
from pathlib import Path
import importlib


# Determine the package name dynamically
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
package_name = current_dir.name
# Add the parent directory to sys.path
sys.path.append(str(parent_dir))
# Dynamically import modules from the determined package
modal = importlib.import_module(f"{package_name}.modal")
nspa = importlib.import_module(f"{package_name}.nspa")

# Perform modal analysis
results = modal.do_modal()
# Perform nonlinear static pushover analysis in X direction
dx, vx = nspa.do_nspa_x()
# Perform nonlinear static pushover analysis in Y direction
dy, vy = nspa.do_nspa_y()

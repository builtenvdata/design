from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf import StandardGeometry  # noqa


# Bay widths and storey heights
num_storeys = 4
storey_height = 3
num_bays_x = 4
num_bays_y = 4
bay_width_x = 5
bay_width_y = 3.5
# Grid ID of left bottom point (or bay ID in x and y)
stair_loc = (0, 0)
stairs_width_x = 2
stairs_width_y = 4
# Initialise the frame object
regular_frame = StandardGeometry(
    num_storeys, storey_height, num_bays_x, bay_width_x,
    num_bays_y, bay_width_y)
# Set stairs location
regular_frame.set_continuous_stairs_rectangles(
    stair_loc, stairs_width_x, stairs_width_y)
# Save the basic frame
path = Path(__file__).parents[1] / 'tmp/simple-uniform-geometry.xlsx'
regular_frame.write_mesh_to_xlsx(path=path)
# Add the new lines and points for stairs (For now do this in the end)
regular_frame.add_new_lines_and_points_for_stairs()
regular_frame.show_mesh()
path = Path(__file__).parents[1] / 'tmp/simple-uniform-geometry.html'
regular_frame.export_mesh_to_html(path=str(path))

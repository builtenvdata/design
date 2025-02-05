from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf import StandardGeometry  # noqa


# Initial bay widths and storey heights
num_storeys = 5
storey_height = 3
num_bays_x = 5
num_bays_y = 5
bay_width_x = 4
bay_width_y = 4
# Grid ID of left bottom point (or bay ID in x and y)
stairs_loc = (0, 0)
stairs_width_x = 4
stairs_width_y = 4
# Modify the ground floor height
h_floor = 4
floor_id = 1
# Initialise the frame object
regular_frame = StandardGeometry(
    num_storeys, storey_height, num_bays_x, bay_width_x,
    num_bays_y, bay_width_y)
# Remove rectangles by grid id (starts from 0)
grid_ids_to_remove = [
    [4, 4, 5], [4, 3, 5], [4, 2, 5],
    [3, 4, 5], [3, 3, 5], [3, 2, 5],
    [2, 4, 5], [2, 3, 5], [2, 2, 5],
    [4, 4, 4], [4, 3, 4], [4, 2, 4],
    [3, 4, 4], [3, 3, 4], [3, 2, 4],
    [2, 4, 4], [2, 3, 4], [2, 2, 4],
    [4, 4, 3], [4, 3, 3], [4, 2, 3],
    [3, 4, 3], [3, 3, 3], [3, 2, 3],
    [2, 4, 3], [2, 3, 3], [2, 2, 3],
    [4, 4, 2], [4, 3, 2], [4, 2, 2],
    [3, 4, 2], [3, 3, 2], [3, 2, 2],
    [2, 4, 2], [2, 3, 2], [2, 2, 2],
    [4, 4, 1], [4, 3, 1], [4, 2, 1],
    [3, 4, 1], [3, 3, 1], [3, 2, 1],
    [2, 4, 1], [2, 3, 1], [2, 2, 1]
]
for grid_ids in grid_ids_to_remove:
    regular_frame.remove_rectangle(grid_ids, remove_lines=True,
                                   remove_points=True)
# Set stairs location
regular_frame.set_continuous_stairs_rectangles(
    stairs_loc, stairs_width_x, stairs_width_y)
# Modifying a floor height (ground floors are usually modified)
regular_frame.modify_floor_height(floor_id, h_floor)
path = Path(__file__).parents[1] / 'tmp/irregular-geometry.xlsx'
regular_frame.write_mesh_to_xlsx(path=path)
# Add the new lines and points for stairs
regular_frame.add_new_lines_and_points_for_stairs()
# Show mesh
regular_frame.show_mesh()
path = Path(__file__).parents[1] / 'tmp/irregular-geometry.html'
regular_frame.export_mesh_to_html(path=str(path))

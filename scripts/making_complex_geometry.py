from pathlib import Path
import sys

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf import StandardGeometry  # noqa


# Initial bay widths and storey heights
num_storeys = 4
storey_height = 3
num_bays_x = 4
num_bays_y = 4
bay_width_x = 4
bay_width_y = 4
# Grid ID of left bottom point (or bay ID in x and y)
stairs_bay_loc = (0, 0)
stairs_width_x = 2
stairs_width_y = 4
# Modify the ground floor height
h_floor = 4
floor_id = 1
# Initialise the frame object
regular_frame = StandardGeometry(
    num_storeys, storey_height, num_bays_x, bay_width_x,
    num_bays_y, bay_width_y)
# Remove bays by grid id (starts from 0)
grid_ids_to_remove = [
    [1, 0, 1], [2, 0, 1]
]
for grid_ids in grid_ids_to_remove:
    regular_frame.remove_rectangle(grid_ids, remove_lines=False,
                                   remove_points=False)

grid_ids_to_remove = [
    [3, 3, 2],
    [3, 3, 1]
]
for grid_ids in grid_ids_to_remove:
    regular_frame.remove_rectangle(grid_ids, remove_lines=True,
                                   remove_points=True)

# # Add new stuff
x1 = regular_frame.system_grid_data.x.ord_by_id(4)
y1 = regular_frame.system_grid_data.y.ord_by_id(4)
z1 = regular_frame.system_grid_data.z.ord_by_id(0)
x2 = regular_frame.system_grid_data.x.ord_by_id(4)
y2 = regular_frame.system_grid_data.y.ord_by_id(4)
z2 = regular_frame.system_grid_data.z.ord_by_id(3)
point1 = regular_frame.add_new_point([x1, y1, z1])
point2 = regular_frame.find_point_by_coordinates([x2, y2, z2])
regular_frame.add_new_line([point1, point2])

# Set stairs location
regular_frame.set_continuous_stairs_rectangles(
    stairs_bay_loc, stairs_width_x, stairs_width_y)
# Add the new lines and points for stairs
regular_frame.add_new_lines_and_points_for_stairs()
# Modifying a floor height (ground floors are usually modified)
regular_frame.modify_floor_height(floor_id, h_floor)
regular_frame.show_mesh()
path = Path(__file__).parents[1] / 'tmp/complex-geometry.html'
regular_frame.export_mesh_to_html(path=str(path))

from src.geometry.frame import CustomFrame
from pathlib import Path

if __name__ == '__main__':

    tmp_folder = Path(__file__).parent / 'tmp'
    input_path = tmp_folder / 'example-custom-geometry.xlsx'
    custom_frame = CustomFrame(input_path)
    # # Making the bay widths and storey heights uniform
    # num_storeys = 4
    # storey_height = 3
    # num_bays_x = 4
    # num_bays_y = 4
    # bay_width_x = 4
    # bay_width_y = 4
    # custom_frame.uniformise(bay_width_x, bay_width_y, storey_height)
    # # Adding a continuous staircase (On top of existing one)
    # # Grid ID of left bottom point (or bay ID in x and y)
    # stairs_loc = (0, 0)
    # stairs_width_x = 2
    # stairs_width_y = 4
    # custom_frame.set_continuous_stairs_rectangles(
    #     stairs_loc, stairs_width_x, stairs_width_y)
    # # Modifying a floor height (ground floors are usually modified)
    # h_floor = 4
    # floor_id = 1
    # custom_frame.modify_floor_height(floor_id, h_floor)

    # Adding new lines and points for stairs
    # Note that rectangles are specified in custom geometry
    custom_frame.add_new_lines_and_points_for_stairs()
    # Show the mesh
    custom_frame.show_mesh()
    path = Path(__file__).parent/'tmp'/'example-custom-geometry.html'
    custom_frame.export_mesh_to_html(path=str(path))

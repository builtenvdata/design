"""
Plotter for OpenSeesPy models. The module is inspired by the vfo
package of Anurag Upadhyay. https://github.com/u-anurag
"""

import numpy as np
import pyvista as pv
import openseespy.opensees as ops
from typing import Literal, List, Optional, Tuple


# Set PyVista theme
# https://docs.pyvista.org/examples/02-plot/themes.html
pv.set_plot_theme("document")

# Base colours considered
base_colors = [
    "gray",
    "lightblue",
    "lightgreen",
    "blue",
    "magenta",
    "cyan",
    "gold",
    "green",
    "tomato",
]


def _get_node_index(node_tag: int, node_tags: np.ndarray) -> int:
    """Find the index of a node tag within the node tags array.

    Parameters
    ----------
    node_tag : int
        The tag of the node whose index is requested.
    node_tags : np.ndarray
        Array containing all node tags.

    Returns
    -------
    int
        The index of the node tag within the node tags array.
    """
    (node_index,) = np.where(node_tags[:] == int(node_tag))
    return int(node_index[0])


def _get_ele_class_tag(ele_tag: int, ele_class_tags: np.ndarray) -> np.ndarray:
    """Retrieve the class tag of an element based on its tag.

    Parameters
    ----------
    ele_tag : int
        The element tag.
    ele_class_tags : np.ndarray
        Array of element class tags where the first column contains the
        element tags and the second column contains the corresponding class
        tags.

    Returns
    -------
    np.ndarray
        The class tag of the element.
    """
    if ele_class_tags.ndim > 1:
        (i,) = np.where(ele_class_tags[:, 0] == int(ele_tag))
        return ele_class_tags[i[0], 1]
    else:
        return ele_class_tags[1]


def _get_pv_2node_ele(ele_arr: List[np.ndarray], node_tags: np.ndarray
                      ) -> np.ndarray:
    """Generate an array of 2-node elements for line plotting.

    Parameters
    ----------
    ele_arr : List[np.ndarray]
        List of elements, each represented by an array with its tag and node
        tags.
    node_tags : np.ndarray
        Array containing all node tags.

    Returns
    -------
    np.ndarray
        Array containing line elements in the format
        [2, node1_index, node2_index].
    """
    line_ele = np.empty(0, dtype=int)
    for ii in ele_arr:
        if len(ii) == 3:
            tmp_arr = np.array([
                2, _get_node_index(ii[1], node_tags),
                _get_node_index(ii[2], node_tags)
                ])
            line_ele = np.hstack((line_ele, tmp_arr))

    return line_ele.astype(int)


def _get_pv_surfaces(ele_arr: List[np.ndarray], node_tags: np.ndarray,
                     ele_class_tags: np.ndarray) -> np.ndarray:
    """Generate an array of surface elements for plotting.

    Parameters
    ----------
    ele_arr : List[np.ndarray]
        List of elements, each represented by an array with its tag and node
        tags.
    node_tags : np.ndarray
        Array containing all node tags.
    ele_class_tags : np.ndarray
        A 2D array where each row contains the element tag in the first column
        and the element's class tag in the second column.

    Returns
    -------
    np.ndarray
        Array containing surface elements formatted for plotting.
    """
    # Element class tags
    four_node_eles = [31, 32, 52, 53, 55, 156, 157, 173, 174, 203]
    tri_node_eles = [33, 167, 168, 204]
    eight_noed_brick_eles = [36, 38, 43, 44, 56]
    MVLEM_eles = [162, 164, 212, 213]
    tet_eles = [179]

    faces = np.empty(0, dtype=int)

    for ii in ele_arr:
        tmp_arr = np.empty(0, dtype=int)

        if _get_ele_class_tag(ii[0], ele_class_tags) in tri_node_eles:
            tmp_arr = np.array(
                [
                    3,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[3], node_tags),
                ]
            )

        if _get_ele_class_tag(ii[0], ele_class_tags) in four_node_eles:
            tmp_arr = np.array(
                [
                    4,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[3], node_tags),
                    _get_node_index(ii[4], node_tags),
                ]
            )

        if _get_ele_class_tag(ii[0], ele_class_tags) in MVLEM_eles:
            tmp_arr = np.array(
                [
                    4,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[4], node_tags),
                    _get_node_index(ii[3], node_tags),
                ]
            )

        if _get_ele_class_tag(ii[0], ele_class_tags) in tet_eles:
            tmp_arr = np.array(
                [
                    3,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[3], node_tags),
                    3,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[4], node_tags),
                    3,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[3], node_tags),
                    _get_node_index(ii[4], node_tags),
                    3,
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[3], node_tags),
                    _get_node_index(ii[4], node_tags),
                ]
            )

        if _get_ele_class_tag(ii[0], ele_class_tags) in eight_noed_brick_eles:
            tmp_arr = np.array(
                [
                    4,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[3], node_tags),
                    _get_node_index(ii[4], node_tags),
                    4,
                    _get_node_index(ii[5], node_tags),
                    _get_node_index(ii[6], node_tags),
                    _get_node_index(ii[7], node_tags),
                    _get_node_index(ii[8], node_tags),
                    4,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[6], node_tags),
                    _get_node_index(ii[5], node_tags),
                    4,
                    _get_node_index(ii[4], node_tags),
                    _get_node_index(ii[3], node_tags),
                    _get_node_index(ii[7], node_tags),
                    _get_node_index(ii[8], node_tags),
                    4,
                    _get_node_index(ii[1], node_tags),
                    _get_node_index(ii[4], node_tags),
                    _get_node_index(ii[8], node_tags),
                    _get_node_index(ii[5], node_tags),
                    4,
                    _get_node_index(ii[2], node_tags),
                    _get_node_index(ii[3], node_tags),
                    _get_node_index(ii[7], node_tags),
                    _get_node_index(ii[6], node_tags),
                ]
            )

        faces = np.hstack((faces, tmp_arr))


def _get_model_display(
    node_arr: np.ndarray, ele_arr: List[np.ndarray], ele_class_tags: np.ndarray
) -> Tuple[pv.PolyData, pv.PolyData, np.ndarray, np.ndarray]:
    """Generates the 3D model display data for plotting using PyVista.

    Parameters
    ----------
    node_arr : np.ndarray
        A 2D array representing all nodes in the model.
        Each row corresponds to a node with format [NodeID, x, y, z].
    ele_arr : List[np.ndarray]
        A list of all elements in the model, where each element is represented
        as an array. The first entry is the element tag, followed by the node
        tags that define the element.
    ele_class_tags : np.ndarray
        A 2D array where each row contains the element tag in the first column
        and the element's class tag in the second column.

    Returns
    -------
    mesh : pv.PolyData
        A PolyData object representing the surfaces of the elements for 3D
        visualization.
    mesh_lines : pv.PolyData
        A PolyData object representing the lines (2-node elements) for line
        visualization.
    vertices : np.ndarray
        A 2D array of the node coordinates [x, y, z] for each node in the
        model.
    node_tags : np.ndarray
        A 1D array containing the node tags for each node in the model.
    """
    # Extract node coordinates and tags
    vertices = node_arr[:, 1:]  # point coordinates (x, y, z)
    node_tags = node_arr[:, 0].astype(int)  # node tags as integers

    # Generate line elements (2-node elements) and surface elements
    # Line elements for plotting
    lines = _get_pv_2node_ele(ele_arr, node_tags)
    # Surface elements for plotting
    surf = _get_pv_surfaces(ele_arr, node_tags, ele_class_tags)

    # Create PyVista meshes
    mesh = pv.PolyData(vertices, surf)  # Surface mesh
    mesh_lines = pv.PolyData(vertices)  # Line mesh
    mesh_lines.lines = lines            # Assign line elements to the line mesh

    return mesh, mesh_lines, vertices, node_tags


def _node_coords(node_tag: int, node_arr: np.ndarray) -> np.ndarray:
    """Returns an array of node coordinates.

    Parameters
    ----------
    node_tag : int
        Tag of the node for which coordinates are requested.
    node_arr : np.ndarray
        A 2D-array of all nodes in the model.
        Returns nodes in the shape:
        [Nodes, 3] in 2d and [Nodes, 4]
        For each node the information is stored as follows:
        [NodeID, x, y] or [NodeID, x, y, z]
        [NodeID, x, y] or [NodeID, x, y, z]

    Returns
    -------
    np.ndarray
        1D array containing coordinates (x, y, z) of the node.
    """
    (i,) = np.where(node_arr[:, 0] == float(node_tag))
    return node_arr[int(i[0]), 1:]


def _get_ele_tag_coord(ele_arr: List[np.ndarray], node_arr: np.ndarray
                       ) -> np.ndarray:
    """Gets the average x, y, z coordinates for each element based on the node
    coordinates.

    Parameters
    ----------
    ele_arr : List[np.ndarray]
        A list of all elements in the model. Each element is represented as
        an array, with the first entry being the element tag and the subsequent
        entries being the node tags that define the element.
    node_arr : np.ndarray
        A 2D array of all nodes in the model. Each row contains the node tag
        and the node coordinates in the format:
        [NodeID, x, y] for 2D models or [NodeID, x, y, z] for 3D models.

    Returns
    -------
    np.ndarray
        A 2D array where each row contains the element tag and the average
        coordinates of the nodes that define the element in the format:
        [ele_tag, avg_xcoord, avg_ycoord, avg_zcoord].
        For 2D models, avg_zcoord will be 0.
    """
    # Initialize array to store element tag and average coordinates
    ele_tag_coord = np.empty([len(ele_arr), 4])  # Shape [num_elements, 4]

    count_ii = 0  # Element counter
    for ii in ele_arr:
        # Store coordinates of nodes for the current element
        tmp_coord_arr = np.empty([len(ii) - 1, 3])  # Shape [num_nodes, 3]

        count_jj = 0  # Node counter
        for jj in ii[1:]:
            # Get coordinates for each node and store in tmp_coord_arr
            tmp_coord_arr[count_jj] = _node_coords(jj, node_arr)
            count_jj += 1

        # Calculate average coordinates for the element
        ele_tag_coord[count_ii] = np.array([
            ii[0],  # Element tag
            np.average(tmp_coord_arr[:, 0]),  # Avg x-coordinate
            np.average(tmp_coord_arr[:, 1]),  # Avg y-coordinate
            np.average(tmp_coord_arr[:, 2])   # Avg z-coordinate (or 0 for 2D)
        ])

        count_ii += 1  # Move to next element

    return ele_tag_coord  # Return element tags with average coordinates


def _get_node_sand_ele() -> Tuple[np.ndarray, List[np.ndarray], np.ndarray]:
    """Retrieve node and element data for an active OpenSees model.

    This function extracts node and element information from the current
    OpenSees model. The model must be active for this function to work. It
    returns the nodes, elements, and element class tags in arrays suitable
    for further processing and visualization.

    Returns
    -------
    nodes : np.ndarray
        A 2D array where each row contains information about a node in the
        format: [NodeID, x, y] for 2D models or [NodeID, x, y, z] for 3D models
    elements : List[np.ndarray]
        A list where each entry is an array representing an element. The first
        value in each array is the element tag, followed by the node tags that
        define the element.
    ele_class_tags : np.ndarray
        A 2D array where each row contains the element tag and its
        corresponding element class tag.
    """
    # Get node and element tags from the OpenSees model
    node_list = ops.getNodeTags()
    ele_list = ops.getEleTags()

    # Determine if the model is 2D or 3D based on the first node's coordinates
    ndm = len(ops.nodeCoord(node_list[0]))

    # Initialize array for node coordinates and element class tags
    num_nodes = len(node_list)
    num_ele = len(ele_list)
    # [num_nodes, 3] for 2D or [num_nodes, 4] for 3D
    nodes = np.zeros([num_nodes, ndm + 1])
    # [num_ele, 2] for element tag and class tag
    ele_class_tags = np.zeros([num_ele, 2])

    # Fill the nodes array with node tags and coordinates
    for ii, node in enumerate(node_list):
        # First column stores node tags
        nodes[ii, 0] = node
        # Remaining columns store coordinates
        nodes[ii, 1:] = ops.nodeCoord(node_list[ii])

    # Initialize list to store elements
    elements = []

    # Loop through elements and store their tags and node tags
    for ii, ele in enumerate(ele_list):
        tmp_nodes = ops.eleNodes(ele)  # Get node tags for the current element
        tmp_num_nodes = len(tmp_nodes)  # Number of nodes in the element

        # Create an array where the first value is the element tag,
        # followed by node tags
        tmp_ele = np.zeros(tmp_num_nodes + 1)
        tmp_ele[0] = int(ele)  # Store the element tag
        tmp_ele[1:] = tmp_nodes  # Store the node tags

        elements.append(tmp_ele)  # Append element array to the elements list

    # Fill the element class tags array with element tags and class tags
    for ii, ele in enumerate(ele_list):
        ele_class_tags[ii, 0] = ele  # First column for element tag
        # Second column for class tag
        ele_class_tags[ii, 1] = ops.getEleClassTags(ele)[0]

    # Return nodes, elements, and element class tags
    return nodes, elements, ele_class_tags


def _get_mode_shape_data(mode_number: int) -> np.ndarray:
    """Get the mode shape data per node.

    Parameters
    ----------
    mode_number : int
        Number of the mode being shown.

    Returns
    -------
    np.ndarray
        Array containing modal displacements per node.
    """

    # Get nodes and elements
    node_list = ops.getNodeTags()

    # Check Number of dimensions and intialize variables
    ndm = len(ops.nodeCoord(node_list[0]))
    num_nodes = len(node_list)
    nodes_mode_shape = np.zeros([num_nodes, ndm + 1])

    # Set the modal displacements per node
    for ii, node in enumerate(node_list):
        nodes_mode_shape[ii, 0] = node
        tmp_data = ops.nodeEigenvector(node_list[ii], mode_number)
        nodes_mode_shape[ii, 1:] = tmp_data[0:ndm]

    return nodes_mode_shape


def plot_model(
    show_nodes: Literal["yes", "no"] = "no",
    show_nodetags: Literal["yes", "no"] = "no",
    show_eletags: Literal["yes", "no"] = "no",
    font_size: int = 10,
    set_view: Literal["xy", "yz", "xz", "3D"] | List[float] = "3D",
    ele_groups: Optional[List[List[int] | List[str]]] = None,
    line_width: int = 1,
    filename: Optional[str] = None,
    show: bool = True,
) -> None:
    """Plots the numerical model of the structure.

    Parameters
    ----------
    show_nodes : Literal["yes", "no"], optional
        Renders nodes as spheres, by default "no".
    show_nodetags : Literal["yes", "no"], optional
        Displays node tags if "yes", by default "no".
    show_eletags : Literal["yes", "no"], optional
        Displays element tags if "yes", by default "no".
    font_size : int, optional
        Size of tag font, by default 10.
    set_view : Literal["xy", "yz", "xz", "3D"] | List[float], optional
            Sets the camera view to predefined angles. Valid entries are
            "xy","yz","xz","3D", or a list with [x,y,z] unit vector,
            by default "3D".
    ele_groups : Optional[List[List[int]  |  List[str]]], optional
        List of lists of elements of groups and respective colors,
        by default None.
    line_width : int, optional
            Line thickness for the beam-column elements, by default 1.
    filename : str, optional
            Filename to save an image of the mode shape, by default None.
    show : bool, optional
            Flag for showing the figure in an interactive window,
            by default True.
    """
    # Get nodes, elements, and class tags for the active model
    this_node_array, element_array, ele_class_tags = _get_node_sand_ele()

    # Initialize a node array and check if the model is 2D or 3D
    node_array = np.zeros([len(this_node_array[:, 0]), 4])
    ndm = len(this_node_array[0, :]) - 1
    if ndm == 2:  # 2D model
        for ii in range(len(this_node_array[:, 0])):
            node_array[ii, 0:3] = this_node_array[ii, :]
    else:  # 3D model
        node_array = this_node_array

    # Generate mesh for plotting
    mesh_original, mesh_lines_original, vertices, nodeTags = \
        _get_model_display(node_array, element_array, ele_class_tags)

    # Initialize the PyVista plotter
    pl = pv.Plotter()

    # Set point size and sphere rendering if nodes are to be shown
    if show_nodes == "yes":
        point_size = 5.0
        spheres = True
    else:
        point_size = 0.0
        spheres = False

    # Get coordinates for element tags
    ele_tag_coord = _get_ele_tag_coord(element_array, node_array)

    # Plot the groups of elements if any are specified
    if ele_groups is not None:

        for gg, this_group in enumerate(ele_groups[0]):
            this_group_ele_arr = [None] * len(this_group)
            this_group_color = ele_groups[1][gg]

            for ii, ele in enumerate(this_group):
                (i,) = np.where(ele_tag_coord[:, 0] == float(ele))
                this_group_ele_arr[ii] = element_array[int(i[0])]

            # Get mesh for this group of elements
            mesh_this_group, mesh_lines_this_group, _, _ = \
                _get_model_display(
                    node_array, this_group_ele_arr, ele_class_tags)

            # Add group surface mesh to the plot
            pl.add_mesh(
                mesh_this_group,
                render_points_as_spheres=False,
                point_size=0.0,
                show_edges=False,
                color=this_group_color,
                opacity=1.0,
                render_lines_as_tubes=False,
                line_width=1,
            )

            # Add group line mesh to the plot
            pl.add_mesh(
                mesh_lines_this_group,
                render_points_as_spheres=False,
                point_size=0.0,
                show_edges=False,
                style='wireframe',
                color=this_group_color,
                opacity=1.0,
                render_lines_as_tubes=True,
                line_width=line_width,
            )

        # Add all points
        pl.add_mesh(
            mesh_original,
            show_edges=False,
            render_points_as_spheres=spheres,
            point_size=point_size,
            style='points',
            color="green",
            opacity=1.0,
            render_lines_as_tubes=False,
            line_width=0.0,
        )

    else:
        # Add the surface mesh to the plot
        pl.add_mesh(
            mesh_original,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            color="green",
            opacity=1.0,
            render_lines_as_tubes=False,
            line_width=1,
        )
        # Add the line mesh (beam-column elements) to the plot
        pl.add_mesh(
            mesh_lines_original,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            color="green",
            opacity=1.0,
            render_lines_as_tubes=False,
            line_width=line_width,
        )

    # Set the camera view
    if set_view == "xy":
        pl.view_xy()
    elif set_view == "yz":
        pl.view_yz()
    elif set_view == "xz":
        pl.view_xz()
    elif set_view == "3D":
        pl.view_isometric()
    else:
        pl.set_viewup(set_view)

    # Override the view if the model is 2D (always set to "xy" for 2D models)
    if ndm == 2:
        pl.view_xy()

    # Add node tags to the plot if specified
    if show_nodetags == "yes":
        pl.add_point_labels(
            vertices,
            nodeTags.astype(int),
            point_size=1,
            render_points_as_spheres=True,
            font_size=font_size,
            shape_color="white",
            shape_opacity=0.2,
            render=True,
            always_visible=True,
        )

    # Add element tags to the plot if specified
    if show_eletags == "yes":
        pl.add_point_labels(
            ele_tag_coord[:, 1:],
            ele_tag_coord[:, 0].astype(int),
            font_size=font_size,
            shape_color="gray",
            shape_opacity=0.2,
            render=True,
            always_visible=True,
        )

    # Export the plot to an HTML file if filename is provided
    if filename is not None:
        pl.export_html(filename)

    # Show the plot interactively if the 'show' flag is set to True
    if show:
        pl.show()
    else:
        pl.close()


def plot_mode_shape(
    mode_number: int = 1,
    scale: int = 10,
    contour: Literal["x", "y", "x", "none"] = "none",
    set_view: Literal["xy", "yz", "xz", "3D"] | List[float] = "3D",
    line_width: int = 1,
    contour_limits: Optional[List] = None,
    filename: Optional[str] = None,
    show: bool = True,
) -> None:
    """Plots the shape of specified mode.

    Parameters
    ----------
    mode_number : int, optional
            Number of the mode being shown, by default 1.
    scale : int, optional
            Scale factor to be applied to the deformed shape, by default 10.
    contour : Literal["x", "y", "x", "none"], optional
            Contours of displacement in x, y, or z. By default "none".
    set_view : Literal["xy", "yz", "xz", "3D"] | List[float], optional
            Sets the camera view to predefined angles. Valid entries are
            "xy","yz","xz","3D", or a list with [x,y,z] unit vector.
            by default "3D".
    line_width : int, optional
            Line thickness for the beam-column elements, by default 1.
    contour_limits : list, optional
            A list of minimum and maximum limits of the displacement contours,
            by default None.
    filename : str, optional
            Filename to save an image of the mode shape, by default None.
    show : bool, optional
            Flag for showing the figure in an interactive window,
            by default True.
    """
    # Perform eigenvalue analysis to get the mode shapes
    ops.wipeAnalysis()
    ops.eigen(mode_number + 1)  # Calculate eigenvalues and mode shapes
    this_node_array, ele_arr, ele_class_tags = _get_node_sand_ele()
    this_mode_node_array = _get_mode_shape_data(mode_number)
    ops.wipeAnalysis()  # Clear the analysis state

    # Check if the model is 2D or 3D and adjust node array accordingly
    node_array = np.zeros([len(this_node_array[:, 0]), 4])
    mode_node_array = np.zeros([len(this_mode_node_array[:, 0]), 4])
    ndm = len(this_node_array[0, :]) - 1
    if ndm == 2:  # Handle 2D models
        for ii in range(len(this_node_array[:, 0])):
            node_array[ii, 0:3] = this_node_array[ii, :]
        for ii in range(len(this_mode_node_array[:, 0])):
            mode_node_array[ii, 0:3] = this_mode_node_array[ii, :]
    else:  # Handle 3D models
        node_array = this_node_array
        mode_node_array = this_mode_node_array

    # Calculate the deflected node coordinates using the mode shape data
    deflected_node_coord_arr = (node_array[:, 1:] +
                                scale * mode_node_array[:, 1:])

    # Combine node IDs with their deflected coordinates
    deflected_node_arr = np.hstack(
        (
            node_array[:, 0].reshape(len(node_array[:, 0]), 1),
            deflected_node_coord_arr[:, 0:],
        )
    )

    # Get the mesh data for the deflected structure
    mesh_deflected, mesh_lines_deflected, _, _ = _get_model_display(
        deflected_node_arr, ele_arr, ele_class_tags
    )

    # Start plotting the mode shape
    pl = pv.Plotter()
    point_size = 0.0
    spheres = False

    # Plot the deflected structure without displacement contours
    if contour == "none":
        pl.add_mesh(
            mesh_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=1,
            color="green",
            opacity=1.0,
            name="thisMesh1",
        )
        pl.add_mesh(
            mesh_lines_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=line_width,
            color="green",
            opacity=1.0,
            name="thisMesh2",
        )
    # Plot the deflected structure with contours based on x displacement
    elif contour == "x":
        x = mode_node_array[:, 1]  # x-displacement values
        pl.add_mesh(
            mesh_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=1,
            scalars=x,
            clim=contour_limits,
            opacity=1.0,
            name="thisMesh1",
        )
        pl.add_mesh(
            mesh_lines_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=line_width,
            scalars=x,
            clim=contour_limits,
            opacity=1.0,
            name="thisMesh2",
        )
    # Plot the deflected structure with contours based on y displacement
    elif contour == "y":
        y = mode_node_array[:, 2]  # y-displacement values
        pl.add_mesh(
            mesh_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=1,
            scalars=y,
            clim=contour_limits,
            opacity=1.0,
            name="thisMesh1",
        )
        pl.add_mesh(
            mesh_lines_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=line_width,
            scalars=y,
            clim=contour_limits,
            opacity=1.0,
            name="thisMesh2",
        )
    # Plot the deflected structure with contours based on z displacement
    elif contour == "z":
        z = mode_node_array[:, 3]  # z-displacement values
        pl.add_mesh(
            mesh_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=1,
            scalars=z,
            clim=contour_limits,
            opacity=1.0,
            name="thisMesh1",
        )
        pl.add_mesh(
            mesh_lines_deflected,
            show_edges=True,
            render_points_as_spheres=spheres,
            point_size=point_size,
            line_width=line_width,
            scalars=z,
            clim=contour_limits,
            opacity=1.0,
            name="thisMesh2",
        )

    # Set the camera view based on user input
    if set_view == "xy":
        pl.view_xy()
    elif set_view == "yz":
        pl.view_yz()
    elif set_view == "xz":
        pl.view_xz()
    elif set_view == "3D":
        pl.view_isometric()
    else:
        pl.set_viewup(set_view)

    # Override the view to "xy" if the model is 2D
    if ndm == 2:
        pl.view_xy()

    # Add a label for the mode number
    pl.add_text("Mode = " + str(mode_number), color="black", font_size=12)

    # Export the plot as an HTML file if a filename is provided
    if filename is not None:
        pl.export_html(filename)

    # Show the plot interactively if the 'show' flag is set to True
    if show:
        pl.show()
    else:
        pl.close()

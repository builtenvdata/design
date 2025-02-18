"""
Miscellaneous utility methods.
"""

# Imports from installed packages
import errno
import numpy as np
import os
from pathlib import Path
from time import time, gmtime
from typing import Callable, Union, Any, Dict, List
import shutil
import sys
import stat

PRECISION = 8
"""Precision used in rounding of floating numbers."""


def update_nested_dict(d: Dict[str, Any], u: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively updates a nested dictionary with another dictionary.

    Parameters
    -----------
    d : Dict[str, Any]
        The original nested dictionary to be updated.
    u : Dict[str, Any]
        The dictionary containing updates.

    Returns
    -------
    Dict[str, Any]
        The updated nested dictionary.
    """
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = update_nested_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def run_time(start_time: int) -> str:
    """Prints the time passed between start_time and finish_time (now)
    in hours, minutes, seconds. startTime is a global variable.

    Parameters
    ----------
    start_time : int
        The initial time obtained via time().

    Returns
    -------
    str
        total run time (hr, min, sec).
    """

    finish_time = time()
    # Procedure to obtained elapsed time in Hr, Min, and Sec
    time_seconds = finish_time - start_time
    time_minutes = int(time_seconds / 60)
    time_hours = int(time_seconds / 3600)
    time_minutes = int(time_minutes - time_hours * 60)
    time_seconds = time_seconds - time_minutes * 60 - time_hours * 3600
    text = (f"Run time: {time_hours:.0f} hours: {time_minutes:.0f} "
            f"minutes: {time_seconds:.2f} seconds")
    print(text)
    return text


def handle_remove_read_only(func: Callable, path: str, exc: tuple) -> None:
    """Upon granting file the permission (# 0777),
    removes the file using given remove function.

    Parameters
    ----------
    func : Callable
        remove function.
    path : str
        file path.
    exc : tuple
        Exception tuple.

    Raises
    ------
    Warning
        Path is in use.
    """

    excvalue: OSError = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise Warning("Path is being used by at the moment.",
                      "It cannot be recreated.")


def remove_dir(dir_path: Union[str, Path]) -> None:
    """Removes a directory if it exists.

    Parameters
    ----------
    dir_path : Union[str, Path]
        Name of directory to remove.
    """
    if os.path.exists(dir_path):
        if sys.version_info < (3, 12):
            shutil.rmtree(path=dir_path, onerror=handle_remove_read_only)
        else:
            shutil.rmtree(path=dir_path, onexc=handle_remove_read_only)


def make_dir(dir_path: Union[str, Path]) -> None:
    """Makes a clean directory by deleting it if it exists.

    Parameters
    ----------
    dir_path : Union[str, Path]
        Name of directory to make.
    """

    if isinstance(dir_path, Path):
        dir_path = str(dir_path)

    if os.path.exists(dir_path):
        remove_dir(dir_path)

    os.makedirs(dir_path)


def signif(x: np.ndarray, p: int) -> np.ndarray:
    """Significant figure rounding for arrays

    Parameters
    ----------
    x : np.ndarray
        array to be rounded.
    p : int
        significant digits.

    Returns
    -------
    np.ndarray
        Rounded array.
    """

    x = np.asarray(x)
    x_positive = np.where(np.isfinite(x) & (x != 0), np.abs(x), 10**(p-1))
    mags = 10 ** (p - 1 - np.floor(np.log10(x_positive)))
    return np.round(x * mags) / mags


def check_parameters(parameters: dict, required_parameters: tuple) -> None:
    """Checks if all the required parameters are defined
    in the parameters dictionary.

    Parameters
    ----------
    parameters : dict
        user defined parameters.
    required_parameters : tuple
        parameters required by the application.

    Raises
    ------
    KeyError
        A parameter is missing.
    """

    # Check the user entries
    for name in required_parameters:
        if name in parameters.keys():
            continue
        else:
            raise KeyError(f"Required simulation parameter is missing: {name}")


def dot(a: List[float], b: List[float]) -> float:
    """Dot products of two lists containing float numbers.

    Parameters
    ----------
    a : List[float]
        The first list of floats.
    b : List[float]
        The second list of floats.

    Returns
    -------
    float
        Dot product
    """

    if len(a) != len(b):
        return 0.0

    return sum(i[0] * i[1] for i in zip(a, b))


def get_time_based_seed():
    """
    Determine the random number generator set based on the date and time

    Returns
    -------
    int
        Summation of numbers based on time date a number.
    """

    return sum(gmtime())


def convert_numpy_types(input_list: List[Any]) -> List[Any]:
    """
    Converts NumPy-specific types in a list to regular Python types
    (int or float).

    This function iterates over the provided list and checks if the items are
    of NumPy types such as `np.integer` or `np.floating`. If they are,
    it converts them to standard Python types (`int` for `np.integer` and
    `float` for `np.floating`). Any non-NumPy types are left unchanged.

    Parameters
    ----------
    input_list : List[Any]
        A list containing elements that may include NumPy-specific types or
        standard Python types.

    Returns
    -------
    List[Any]
        A new list with NumPy types converted to their corresponding Python
        types (`int` or `float`). Non-NumPy types are returned unchanged.

    Example
    -------
    >>> example_list = [np.float64(3.14), np.int32(10), 5, 7.2]
    >>> convert_numpy_types(example_list)
    [3.14, 10, 5, 7.2]
    """

    result = []
    for item in input_list:
        if isinstance(item, np.integer):  # Check for NumPy int type
            result.append(int(item))
        elif isinstance(item, np.floating):  # Check for NumPy float type
            result.append(float(item))
        else:
            result.append(item)  # Keep as is if it's not a NumPy type

    return result


def round_list(input_list: List[Union[int, float]],
               precision: int = PRECISION) -> List[float]:
    """
    Rounds each value in a list to the specified precision.

    Parameters:
    -----------
    input_list : List[float]
        A list of floating-point numbers to be rounded.
    precision: int, optional
        Specified precision, by default equal to the constant `PRECISION`.

    Returns:
    --------
    List[float]
        A new list with each value rounded to the specified precision.

    Example:
    --------
    >>> round_values([3.14159, 2.71828, 1.61803], 2)
    [3.14, 2.72, 1.62]
    """
    input_list = convert_numpy_types(input_list)
    return [round(value, precision) for value in input_list]

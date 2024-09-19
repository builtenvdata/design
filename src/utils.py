"""
Utility methods
"""

from scipy.stats import lognorm
import numpy as np
from time import gmtime, time
import os
import errno
import shutil
import stat
from scipy.stats import norm

def run_time(start_time):
    """
    Prints the time passed between start_time and finish_time (now)
    in hours, minutes, seconds. startTime is a global variable.

    Args:
        start_time (int): The initial time obtained via time()

    Returns:
        None
    """

    finish_time = time()
    # Procedure to obtained elapsed time in Hr, Min, and Sec
    time_seconds = finish_time - start_time
    time_minutes = int(time_seconds / 60)
    time_hours = int(time_seconds / 3600)
    time_minutes = int(time_minutes - time_hours * 60)
    time_seconds = time_seconds - time_minutes * 60 - time_hours * 3600
    print(f"Run time: {time_hours:.0f} hours: {time_minutes:.0f} minutes: {time_seconds:.2f} seconds")

def log_normal_truncated_ab_sample(n, mu, sigma, a, b):
    """
    Samples the truncated AB Log Normal CDF

    Args:
        n (int): sample size
        mu (float): mean of the log normal PDF
        sigma (float): standard deviation of the log normal PDF
        a (float): lower truncation limit
        b (float): upper truncation limit

    Raises:
        Exception: if b <= a or sigma <= 0

    Returns:
        numpy.ndarray: real X, a random sample
    """

    if sigma <= 0.0:
        raise Exception('log_normal_truncated_ab_sample - Fatal error: sigma <= 0.0')

    if b <= a:
        raise Exception('log_normal_truncated_ab_sample - Fatal error: b <= a')

    lncdf_a = lognorm(s=sigma, scale=np.exp(mu)).cdf(a)
    lncdf_b = lognorm(s=sigma, scale=np.exp(mu)).cdf(b)

    lncdf_x = lncdf_a + (lncdf_b - lncdf_a) * np.random.rand(n)
    x = lognorm(s=sigma, scale=np.exp(mu)).ppf(lncdf_x)

    return x


def log_normal_truncated_ab_cdf_inv(cdf, mu, sigma, a, b):
    """
    Inverts the truncated AB Log Normal CDF

    Args:
        cdf (float, numpy.ndarray): the value of the cumulative distribution function
        mu (float): mean of the log normal PDF
        sigma (float): standard deviation of the log normal PDF
        a (float): lower truncation limit
        b (float): upper truncation limit

    Returns:
        numpy.ndarray: real X, the argument of the PDF with the given CDF
    """

    lncdf_a = lognorm(s=sigma, scale=np.exp(mu)).cdf(a)
    lncdf_b = lognorm(s=sigma, scale=np.exp(mu)).cdf(b)

    lncdf_x = lncdf_a + cdf * (lncdf_b - lncdf_a)
    x = lognorm(s=sigma, scale=np.exp(mu)).ppf(lncdf_x)
    
    x = np.asarray(x)
    x[cdf <= 0.0] = a
    x[cdf >= 1.0] = b

    return x

def multivariate_normal_sample(m, k0, n, epsilon=0.0):
    """    
    Sample from a multivariate normal distribution following section 
    A.2 Gaussian Identities of the book Gaussian Processes for Machine Learning
    
    References:
    https://juanitorduz.github.io/multivariate_normal/
    https://gaussianprocess.org/gpml/chapters/

    Args:
        m (numpy.ndarray): mean vector
        k0 (numpy.ndarray): covariance matrix
        n (int): number of samples
        epsilon (float, optional):  perturbation value. Defaults to 0.0.

    Raises:
        ValueError: non-positive definite covariance matrix

    Returns:
        numpy.ndarray: Sample from a multivariate normal distribution with mean m and covariance k_0
    """
    # Make sure that eigenvalues covariance function are greater than 0
    if not np.all(np.linalg.eigvals(k0) > 0):
        raise ValueError('Covariance matrix is not positive definite!')
    
    # Define dimension
    d = len(m)
    # Make sure mean vector is 2d
    m = m.reshape(d, 1)

    # Step 1: Compute the Cholesky Decomposition
    # In practice it may be necessary to add a small multiple of the identity matrix
    # to the covariance matrix for numerical reasons. This is because the eigenvalues of the matrix k0
    # can decay very rapidly and without this stabilization the Cholesky decomposition fails.
    # The effect on the generated samples is to add additional independent noise of variance. 
    # From the context can usually be chosen to have inconsequential effects on the samples, while ensuring numerical stability.” (A.2 Gaussian Identities)

    # Add small perturbation to the covariance matrix
    k = k0 + epsilon*np.identity(d)
    # Cholesky decomposition
    l = np.linalg.cholesky(k)
    # Let us verify the desired property
    if not np.allclose(k, np.dot(l, np.transpose(l))):
        print('Cholesky decomposition is not verified! It might be better to reduce the perturbation (epsilon)!')
    # Step 2: Generate Independent Samples u∼N(0,1)
    u = norm.ppf(np.random.rand(d*n), loc=0, scale=1).reshape(d, n)
    # Step 3: Compute x = m + lu
    x = (m + np.dot(l, u)).T

    return x

def get_time_based_seed():
    """
    Determine the random number generator set based on the date and time

    Returns:
        int: summation of numbers based on time date a number
    """
    
    return sum(gmtime())

def make_dir(dir_path):
    """
    Make a clean directory by deleting it if it exists.

    Args:
        dir_path (str) : name of directory to create.
    
    Returns:
        None
    """

    def handle_remove_read_only(func, path, exc):
        excvalue = exc[1]
        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
            func(path)
        else:
            raise Warning("Path is being used by at the moment.",
                          "It cannot be recreated.")

    if os.path.exists(dir_path):
        shutil.rmtree(dir_path, ignore_errors=False, onerror=handle_remove_read_only)
    os.makedirs(dir_path)

def signif(x, p):
    """Significant figure rounding of numpy.arrays

    Args:
        x (numpy.ndarray): array to be rounded
        p (int): significant digits

    Returns:
        numpy.ndarray: rounded array
    """
    x = np.asarray(x)
    x_positive = np.where(np.isfinite(x) & (x != 0), np.abs(x), 10**(p-1))
    mags = 10 ** (p - 1 - np.floor(np.log10(x_positive)))
    return np.round(x * mags) / mags

def check_parameters(parameters:dict, required_parameters:tuple):
    """Checks if all the required parameters are defined in the parameters dictionary

    Args:
        parameters (dict): user defined parameters
        required_parameters (tuple): parameters required by the application

    Raises:
        KeyError: if a parameter is missing
    """
    # Check the user entries
    for name in required_parameters:
        if name in parameters.keys():
            continue
        else:
            raise KeyError(f"Required simulation parameter is missing: {name}")
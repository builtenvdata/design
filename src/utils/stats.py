"""
Statistics related utility methods.
"""

# Imports from installed packages
from scipy.stats import lognorm, norm
import numpy as np
from time import gmtime
from typing import Union, List


def log_normal_truncated(size: int, mu: float, sigma: float,
                         lower: float, upper: float) -> np.ndarray:
    """Samples the truncated (lower-upper) log-normal CDF.

    Parameters
    ----------
    size : int
        Sample size.
    mu : float
        Mean of the log normal PDF.
    sigma : float
        Standard deviation of the log normal PDF.
    lower : float
        Lower truncation limit.
    upper : float
        Upper truncation limit.

    Returns
    -------
    np.ndarray
        real X, a random sample.

    Raises
    ------
    Exception
        sigma <= 0
    Exception
        upper <= lower
    """

    if sigma <= 0.0:
        raise Exception('log_normal_truncated_ab_sample - '
                        'Fatal error: sigma <= 0.0')

    if upper <= lower:
        raise Exception(
            'log_normal_truncated_ab_sample - Fatal error: upper <= lower')

    lncdf_a = lognorm(s=sigma, scale=np.exp(mu)).cdf(lower)
    lncdf_b = lognorm(s=sigma, scale=np.exp(mu)).cdf(upper)

    lncdf_x = lncdf_a + (lncdf_b - lncdf_a) * np.random.rand(size)
    x = lognorm(s=sigma, scale=np.exp(mu)).ppf(lncdf_x)

    return x


def log_normal_truncated_cdf_inv(
    cdf: Union[float, np.ndarray], mu: float, sigma: float, lower: float,
    upper: float
) -> np.ndarray:
    """Inverts the truncated (lower-upper) log-normal CDF.

    Parameters
    ----------
    cdf : Union[float, np.ndarray]
        the value of the cumulative distribution.
    mu : float
        mean of the log normal PDF.
    sigma : float
        standard deviation of the log normal PDF.
    lower : float
        lower truncation limit.
    upper : float
        upper truncation limit.

    Returns
    -------
    np.ndarray
        Real X, the argument of the PDF with the given CDF.
    """

    lncdf_a = lognorm(s=sigma, scale=np.exp(mu)).cdf(lower)
    lncdf_b = lognorm(s=sigma, scale=np.exp(mu)).cdf(upper)

    lncdf_x = lncdf_a + cdf * (lncdf_b - lncdf_a)
    x = lognorm(s=sigma, scale=np.exp(mu)).ppf(lncdf_x)

    x = np.asarray(x)
    x[cdf <= 0.0] = lower
    x[cdf >= 1.0] = upper

    return x


def multivariate_normal(m: np.ndarray, k0: np.ndarray, size: int,
                        epsilon: float = 0.0) -> np.ndarray:
    """Sample from a multivariate normal distribution.

    It follows section A.2 Gaussian Identities of the book Gaussian Processes
    for Machine Learning.

    Parameters
    ----------
    m : np.ndarray
        Mean vector.
    k0 : np.ndarray
        Covariance matrix.
    size : int
        Sample size.
    epsilon : float, optional
        Perturbation value, by default 0.0.

    Returns
    -------
    np.ndarray
        Sample from a multivariate normal distribution with
        mean m and covariance k_0.

    Raises
    ------
    ValueError
        non-positive definite covariance matrix.

    References
    ----------
    https://juanitorduz.github.io/multivariate_normal/
    https://gaussianprocess.org/gpml/chapters/

    Notes
    -----
    In practice, it may be necessary to add a small multiple of the identity
    matrix to the covariance matrix for numerical reasons. This is because the
    eigenvalues of the matrix k0 can decay very rapidly and without this
    stabilization the Cholesky decomposition fails. The effect on the
    generated samples is to add additional independent noise of variance.
    From the context can usually be chosen to have inconsequential effects on
    the samples, while ensuring numerical stability (A.2 Gaussian Identities).
    For this purpose, epsilon value can be changed.
    """
    # Make sure that eigenvalues covariance function are greater than 0
    if not np.all(np.linalg.eigvals(k0) > 0):
        raise ValueError('Covariance matrix is not positive definite!')
    # Define dimension
    d = len(m)
    # Make sure mean vector is 2d
    m = m.reshape(d, 1)
    # Step 1: Compute the Cholesky Decomposition
    # Add small perturbation to the covariance matrix
    k = k0 + epsilon*np.identity(d)
    # Cholesky decomposition
    lower_triangular_matrix = np.linalg.cholesky(k)
    # Hermitian positive-definite matrix, A=L*L.T
    a = np.dot(lower_triangular_matrix, np.transpose(lower_triangular_matrix))
    # Let us verify the desired property
    if not np.allclose(k, a):
        print('Cholesky decomposition is not verified! '
              'It might be better to reduce the perturbation (epsilon)!')
    # Step 2: Generate Independent Samples u∼N(0,1)
    u = norm.ppf(np.random.rand(d*size), loc=0, scale=1).reshape(d, size)
    # Step 3: Compute x = m + lu
    x = (m + np.dot(lower_triangular_matrix, u)).T

    return x


def random_choice(q: List[str], size: int, p: List[float] = None
                  ) -> np.ndarray:
    """Randomly selects elements from the input list 'q' with replacement,
    optionally using specified probabilities.

    Parameters
    ----------
    q : List[str]
        Input list of strings from which elements will be randomly chosen.
    size : int
        Number of elements to be selected.
    p : List[float], optional
        The probabilities associated with each element in 'q'. If None,
        the probabilities are assumed to be uniform. By default None.

    Returns
    -------
    np.ndarray
        An array containing the randomly selected elements from 'q'.

    Examples
    --------
    >>> q = ['B01', 'B02', 'B03', 'B04', 'B05']
    >>> size = 3
    >>> random_choice(q, size)
    array(['B03', 'B02', 'B05'], dtype='<U4')
    """
    if p is None:
        p = [1/len(q)] * len(q)
    cumulative_probs = np.cumsum(p)
    ids = []
    for _ in range(size):
        r = np.random.rand()
        for idx, cp in enumerate(cumulative_probs):
            if r < cp:
                ids.append(idx)
                break
    x = np.array([q[i] for i in ids])
    return x


def get_time_based_seed() -> int:
    """Determines the random number generator set based on the date and time.

    Returns
    -------
    int
        Summation of numbers in time date.
    """

    return sum(gmtime())

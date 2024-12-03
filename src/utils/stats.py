"""
Statistics related utility methods.
"""

# Imports from installed packages
from scipy.stats import lognorm, norm, uniform
import numpy as np
from time import gmtime
from typing import List


def random_truncated_lognormal(size: int, mu: np.ndarray, sigma: np.ndarray,
                               lower: np.ndarray, upper: np.ndarray
                               ) -> np.ndarray:
    """
    Samples the truncated (lower-upper) log-normal CDF.

    Parameters
    ----------
    size : int
        Sample size (number of random samples to generate).
    mu : np.ndarray
        Mean of the log-normal distribution in log-space.
    sigma : np.ndarray
        Standard deviation of the log-normal distribution in log-space.
    lower : np.ndarray
        Lower truncation limit of the distribution.
    upper : np.ndarray
        Upper truncation limit of the distribution.

    Returns
    -------
    np.ndarray
        An array of random samples from the truncated log-normal distribution.

    Raises
    ------
    Exception
        If `sigma` is less than or equal to 0.
    Exception
        If `upper` is less than or equal to `lower`.

    Notes
    -----
    The truncated log-normal distribution is sampled by generating random
    probabilities within the cumulative distribution function (CDF) range
    defined by the lower and upper truncation limits.

    Example
    -------
    >>> random_truncated_lognormal(
            100, mu=1.0, sigma=0.5, lower=2.0, upper=10.0)
    array([2.35, 4.17, 8.22, ...])  # Example output
    """
    # Validate the standard deviation
    if np.any(sigma <= 0):
        raise Exception('random_truncated_lognormal - '
                        'Fatal error: sigma <= 0.0')
    # Validate the truncation limits
    if np.any(upper <= lower):
        raise Exception(
            'random_truncated_lognormal - Fatal error: upper <= lower')
    # Calculate the cumulative probabilities at the truncation limits
    lncdf_a = lognorm(s=sigma, scale=np.exp(mu)).cdf(lower)
    lncdf_b = lognorm(s=sigma, scale=np.exp(mu)).cdf(upper)
    # Generate uniform random values scaled to the truncated CDF range
    lncdf_x = lncdf_a + (lncdf_b - lncdf_a) * np.random.rand(size)
    # Transform the cumulative probabilities back to the log-normal domain
    x = lognorm(s=sigma, scale=np.exp(mu)).ppf(lncdf_x)
    return x


def truncated_lognormal_cdf_inv(
    cdf: np.ndarray, mu: np.ndarray, sigma: np.ndarray,
    lower: np.ndarray, upper: float
) -> np.ndarray:
    """Inverts the truncated (lower-upper) log-normal CDF.

    Parameters
    ----------
    cdf : np.ndarray
        the value of the cumulative distribution.
    mu : np.ndarray
        mean of the log normal PDF.
    sigma : np.ndarray
        standard deviation of the log normal PDF.
    lower : np.ndarray
        lower truncation limit.
    upper : np.ndarray
        upper truncation limit.

    Returns
    -------
    np.ndarray
        Real X, the argument of the PDF with the given CDF.
    """

    # Compute the truncated CDF bounds
    lncdf_a = lognorm(s=sigma, scale=np.exp(mu)).cdf(lower)
    lncdf_b = lognorm(s=sigma, scale=np.exp(mu)).cdf(upper)
    # Rescale the input CDFs to the truncated range
    lncdf_x = lncdf_a + cdf * (lncdf_b - lncdf_a)
    # Invert the log-normal CDF to get samples
    x = lognorm(s=sigma, scale=np.exp(mu)).ppf(lncdf_x)
    # Apply truncation limits for edge cases
    x = np.clip(x, lower, upper)

    return x


def random_multivariate_normal(m: np.ndarray, k0: np.ndarray, size: int,
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


def random_uniform(size: int, lower: float, upper: float) -> np.ndarray:
    """
    Generates an array of random samples uniformly distributed within
    a specified range.

    Parameters
    ----------
    size : int
        The number of random samples to generate.
    lower : float
        The lower bound of the uniform distribution.
    upper : float
        The upper bound of the uniform distribution.

    Returns
    -------
    np.ndarray
        An array of random samples uniformly distributed between
        `lower` and `upper`.

    Notes
    -----
    The function uses the inverse cumulative distribution function (CDF) of
    the uniform distribution to generate samples based on random probabilities.

    Examples
    --------
    >>> random_uniform(5, 0, 1)
    array([0.123, 0.456, 0.789, 0.234, 0.567])  # Example output
    """
    loc = lower
    scale = lower - upper
    prob = np.random.rand(size)
    sample = uniform.ppf(prob, loc=loc, scale=scale)
    return sample


def random_multivariate_truncated_lognormal(
    size: int, rho: np.ndarray, lower_bound: np.ndarray,
    upper_bound: np.ndarray, theta: np.ndarray, std_ln: np.ndarray,
) -> np.ndarray:
    """
    Sample from a multivariate truncated lognormal distribution.

    Parameters
    ----------
    size : int
        Number of samples to generate.
    rho : np.ndarray
        Correlation matrix (n x n) describing the relationships between
        variables.
    lower_bound : np.ndarray
        Lower bounds for the truncated log-normal distributions.
    upper_bound : np.ndarray
        Upper bounds for the truncated log-normal distributions.
    theta : np.ndarray
        Medians of the log-normal distributions.
    std_ln : np.ndarray
        Logarithmic standard deviations of the log-normal distributions.

    Notes
    -----
    ~LN(ln(theta), sigma)

    Returns
    -------
    np.ndarray
        Samples from the multivariate truncated log-normal distribution
        (size x n).
    """
    n = len(theta)  # Number of dimensions

    # Validate dimensions of inputs
    if not (rho.shape == (n, n)):
        raise ValueError("Correlation matrix must be square and match the "
                         "dimension of the input parameters.")
    if not (len(lower_bound) == len(upper_bound) == n):
        raise ValueError(
            "Bounds, theta, and std_ln must all have the same length.")

    # Mean vector and covariance matrix for the multivariate normal dist.
    mu = np.zeros(n)  # Standard normal distribution
    std = np.ones(n)  # Identity standard deviations
    cov = np.outer(std, std) * rho  # Covariance matrix
    # Realisations from multivariate normal distribution
    z = np.random.multivariate_normal(mu, cov, size=size)
    # Transform multivariate normal samples to cumulative probabilities
    u = norm.cdf(z, loc=0.0, scale=1.0)
    # Log-normal truncated distribution parameters
    mu_ln = np.log(np.array(theta))
    # Map cumulative probabilities to truncated log-normal samples
    samples = truncated_lognormal_cdf_inv(
        u, mu=mu_ln, sigma=std_ln, lower=lower_bound, upper=upper_bound
    )

    return samples


def get_time_based_seed() -> int:
    """Determines the random number generator set based on the date and time.

    Returns
    -------
    int
        Summation of numbers in time date.
    """

    return sum(gmtime())

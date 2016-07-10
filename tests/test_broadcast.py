import numpy as np
import dpmm
from test_utils import timer

@timer
def test_GaussianMeanKnownVariance():
    """Test broadcasting rules for GaussianMeanKnownVariance prior."""

    # Test sample() method:
    prior = dpmm.GaussianMeanKnownVariance(1.0, 1.0, 1.0)
    arr = prior.sample()
    assert isinstance(arr, float)

    arr = prior.sample(size=1)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float

    arr = prior.sample(size=(1,))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float

    arr = prior.sample(size=10)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10,)
    assert arr.dtype == float

    arr = prior.sample(size=(10, 20))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10, 20)
    assert arr.dtype == float

    # Test like1() method:
    prior = dpmm.GaussianMeanKnownVariance(1.0, 1.0, 1.0)
    x = 1.0
    mu = 1.0
    arr = prior.like1(x, mu)
    assert isinstance(arr, float)

    x = np.array([1.0])
    arr = prior.like1(x, mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.like1(x[0], mu)

    x = np.array([1.0, 2.0])
    arr = prior.like1(x, mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], mu)

    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior.like1(x, mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i, j], mu)

    x = np.array([1.0, 2.0])
    mu = np.array([2.0, 3.0])
    arr = prior.like1(x, mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], mu[i])

    x = np.array([1.0, 2.0])
    mu = np.array([1.0, 2.0, 3.0])
    arr = prior.like1(x[:, np.newaxis], mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], mu[j])
    arr = prior.like1(x, mu[:, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[j], mu[i])

    x = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    mu = np.array([10.0, 11.0, 12.0, 13.0])
    arr = prior.like1(x[:, :, np.newaxis], mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3, 4)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i, j], mu[k])
    arr = prior.like1(x, mu[:, np.newaxis, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (4, 2, 3)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[j, k], mu[i])

    # Test __call__() method:
    prior = dpmm.GaussianMeanKnownVariance(1.0, 1.0, 1.0)
    mu = 1.0
    arr = prior(mu)
    assert isinstance(arr, float)

    mu = np.array([1.0])
    arr = prior(mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior(mu[0])

    mu = np.array([1.0, 2.0])
    arr = prior(mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior(mu[i])

    mu = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior(mu)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(mu[i, j])

    # Should _post_params method do any broadcasting?

    # Test pred method():
    prior = dpmm.InvGamma(1.0, 1.0, 0.0)
    x = 1.0
    arr = prior.pred(x)
    assert isinstance(arr, float)

    x = np.array([1.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.pred(x[0])

    x = np.array([1.0, 2.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.pred(x[i])

    x = np.arange(6.0).reshape(3, 2)+1
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.pred(x[i, j])


@timer
def test_InvGamma():
    """Test broadcasting rules for InvGamma prior."""

    # Test sample() method:
    prior = dpmm.InvGamma(1.0, 1.0, 0.0)
    arr = prior.sample()
    assert isinstance(arr, float)

    arr = prior.sample(size=1)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float

    arr = prior.sample(size=(1,))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float

    arr = prior.sample(size=10)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10,)
    assert arr.dtype == float

    arr = prior.sample(size=(10, 20))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10, 20)
    assert arr.dtype == float

    # Test like1() method:
    prior = dpmm.InvGamma(1.0, 1.0, 0.0)
    x = 1.0
    var = 1.0
    arr = prior.like1(x, var)
    assert isinstance(arr, float)

    x = np.array([1.0])
    arr = prior.like1(x, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.like1(x[0], var)

    x = np.array([1.0, 2.0])
    arr = prior.like1(x, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], var)

    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior.like1(x, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i, j], var)

    x = np.array([1.0, 2.0])
    var = np.array([2.0, 3.0])
    arr = prior.like1(x, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], var[i])


    x = np.array([1.0, 2.0])
    var = np.array([1.0, 2.0, 3.0])
    arr = prior.like1(x[:, np.newaxis], var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], var[j])
    arr = prior.like1(x, var[:, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[j], var[i])

    x = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    var = np.array([10.0, 11.0, 12.0, 13.0])
    arr = prior.like1(x[:, :, np.newaxis], var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3, 4)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i, j], var[k])
    arr = prior.like1(x, var[:, np.newaxis, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (4, 2, 3)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[j, k], var[i])

    # Test __call__() method:
    prior = dpmm.InvGamma(1.0, 1.0, 0.0)
    var = 1.0
    arr = prior(var)
    assert isinstance(arr, float)

    var = np.array([1.0])
    arr = prior(var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior(var[0])

    var = np.array([1.0, 2.0])
    arr = prior(var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior(var[i])

    var = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior(var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(var[i, j])

    # Should _post_params method do any broadcasting?

    # Test pred method():
    prior = dpmm.InvGamma(1.0, 1.0, 0.0)
    x = 1.0
    arr = prior.pred(x)
    assert isinstance(arr, float)

    x = np.array([1.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.pred(x[0])

    x = np.array([1.0, 2.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.pred(x[i])

    x = np.arange(6.0).reshape(3, 2)+1
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.pred(x[i, j])


@timer
def test_InvGamma2D():
    """Test broadcasting rules for InvGamma2D prior."""

    # Test sample() method:
    prior = dpmm.InvGamma2D(1.0, 1.0, np.array([0.0, 0.0]))
    arr = prior.sample()
    assert isinstance(arr, float)

    arr = prior.sample(size=1)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float

    arr = prior.sample(size=(1,))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float

    arr = prior.sample(size=10)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10,)
    assert arr.dtype == float

    arr = prior.sample(size=(10, 20))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10, 20)
    assert arr.dtype == float

    # Test like1() method:
    prior = dpmm.InvGamma2D(1.0, 1.0, np.array([0.0, 0.0]))
    x = np.array([1.0, 2.0])  # Data is 2D, so trailing axis should always be len 2.
    var = 1.0
    arr = prior.like1(x, var)
    assert isinstance(arr, float)

    x = np.array([1.0])  # If trailing axis is not 2, then should get an AssertionError
    var = 1.0
    np.testing.assert_raises(AssertionError, prior.like1, x, var)

    x = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    var = 1.0
    arr = prior.like1(x, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], var)

    x = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    var = np.array([2.0, 3.0])
    arr = prior.like1(x, var[:, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[j], var[i])

    x = np.arange(24, dtype=float).reshape(3, 4, 2)
    var = np.array([2.0, 3.0])
    arr = prior.like1(x[:,:,np.newaxis,:], var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 4, 2)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i, j], var[k])

    x = np.arange(24, dtype=float).reshape(3, 4, 2)
    var = np.arange(12, dtype=float).reshape(3, 4) + 1  # add 1 so we don't divide by zero
    arr = prior.like1(x, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 4)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i, j], var[i, j])

    # Test __call__() method:
    prior = dpmm.InvGamma2D(1.0, 1.0, np.array([0.0, 0.0]))
    var = 1.0
    arr = prior(var)
    assert isinstance(arr, float)

    var = np.array([1.0])
    arr = prior(var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior(var[0])

    var = np.array([1.0, 2.0])
    arr = prior(var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior(var[i])

    var = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior(var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(var[i, j])

    # Should _post_params method do any broadcasting?

    # Test pred method():
    prior = dpmm.InvGamma2D(1.0, 1.0, np.array([0.0, 0.0]))
    x = 1.0
    np.testing.assert_raises(AssertionError, prior.pred, x)

    x = np.array([1.0, 2.0])
    arr = prior.pred(x)
    assert isinstance(arr, float)

    x = np.arange(24, dtype=float).reshape(3, 4, 2)
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 4)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.pred(x[i, j])


@timer
def test_NormInvGamma():
    """Test broadcasting rules for NormInvGamma prior."""

    # Test sample() method:
    prior = dpmm.NormInvGamma(1.0, 1.0, 1.0, 1.0)
    arr = prior.sample()
    assert isinstance(arr, np.void)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=1)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=(1,))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=10)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10,)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=(10, 20))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10, 20)
    assert arr.dtype == prior.model_dtype

    # Test like1() method:
    prior = dpmm.NormInvGamma(1.0, 1.0, 1.0, 1.0)
    x = 1.0
    mu = 1.0
    var = 1.0
    arr = prior.like1(x, mu, var)
    assert isinstance(arr, float)

    x = np.array([1.0])
    mu = 1.0
    var = 1.0
    arr = prior.like1(x, mu, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.like1(x[0], mu, var)

    x = np.array([1.0, 2.0, 3.0, 4.0])
    mu = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    var = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    arr = prior.like1(x[:, np.newaxis, np.newaxis], mu, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (4, 2, 3)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], mu[j, k], var[j, k])

    theta = np.zeros((2, 3), dtype=prior.model_dtype)
    theta['mu'] = mu
    theta['var'] = var
    arr = prior.like1(x[:, np.newaxis, np.newaxis], theta)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (4, 2, 3)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], theta['mu'][j, k], theta['var'][j, k])

    arr = prior.like1(x, mu[:, :, np.newaxis], var[:, :, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3, 4)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[k], mu[i, j], var[i, j])

    arr = prior.like1(x, theta[:, :, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3, 4)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[k], theta['mu'][i, j], theta['var'][i, j])

    # Test __call__() method:
    prior = dpmm.NormInvGamma(1.0, 1.0, 1.0, 1.0)
    mu = 1.0
    var = 1.0
    arr = prior(mu, var)
    assert isinstance(arr, float)

    mu = np.array([1.0])
    arr = prior(mu, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior(mu[0], var)

    mu = np.array([1.0, 2.0])
    var = np.array([10.0, 11.0, 12.0])
    arr = prior(mu[:, np.newaxis], var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(mu[i], var[j])

    theta = np.zeros((2, 3), dtype=prior.model_dtype)
    theta['mu'] = mu[:, np.newaxis]
    theta['var'] = var
    arr = prior(theta)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(theta['mu'][i, j], theta['var'][i, j])

    # Should _post_params method do any broadcasting?

    # Test pred method():
    prior = dpmm.NormInvGamma(1.0, 1.0, 1.0, 1.0)
    x = 1.0
    arr = prior.pred(x)
    assert isinstance(arr, float)

    x = np.array([1.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.pred(x[0])

    x = np.array([1.0, 2.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.pred(x[i])

    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.pred(x[i, j])


@timer
def test_NormInvChi2():
    """Test broadcasting rules for NormInvChi2 prior."""

    # Test sample() method:
    prior = dpmm.NormInvChi2(1.0, 1.0, 1.0, 1.0)
    arr = prior.sample()
    assert isinstance(arr, np.void)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=1)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=(1,))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=10)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10,)
    assert arr.dtype == prior.model_dtype

    arr = prior.sample(size=(10, 20))
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (10, 20)
    assert arr.dtype == prior.model_dtype

    # Test like1() method:
    prior = dpmm.NormInvChi2(1.0, 1.0, 1.0, 1.0)
    x = 1.0
    mu = 1.0
    var = 1.0
    arr = prior.like1(x, mu, var)
    assert isinstance(arr, float)

    x = np.array([1.0])
    mu = 1.0
    var = 1.0
    arr = prior.like1(x, mu, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.like1(x[0], mu, var)

    x = np.array([1.0, 2.0, 3.0, 4.0])
    mu = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    var = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    arr = prior.like1(x[:, np.newaxis, np.newaxis], mu, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (4, 2, 3)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], mu[j, k], var[j, k])

    theta = np.zeros((2, 3), dtype=prior.model_dtype)
    theta['mu'] = mu
    theta['var'] = var
    arr = prior.like1(x[:, np.newaxis, np.newaxis], theta)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (4, 2, 3)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[i], theta['mu'][j, k], theta['var'][j, k])

    arr = prior.like1(x, mu[:, :, np.newaxis], var[:, :, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3, 4)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[k], mu[i, j], var[i, j])

    arr = prior.like1(x, theta[:, :, np.newaxis])
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3, 4)
    assert arr.dtype == float
    for (i, j, k), r in np.ndenumerate(arr):
        assert r == prior.like1(x[k], theta['mu'][i, j], theta['var'][i, j])

    # Test __call__() method:
    prior = dpmm.NormInvChi2(1.0, 1.0, 1.0, 1.0)
    mu = 1.0
    var = 1.0
    arr = prior(mu, var)
    assert isinstance(arr, float)

    mu = np.array([1.0])
    arr = prior(mu, var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior(mu[0], var)

    mu = np.array([1.0, 2.0])
    var = np.array([10.0, 11.0, 12.0])
    arr = prior(mu[:, np.newaxis], var)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(mu[i], var[j])

    theta = np.zeros((2, 3), dtype=prior.model_dtype)
    theta['mu'] = mu[:, np.newaxis]
    theta['var'] = var
    arr = prior(theta)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 3)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior(theta['mu'][i, j], theta['var'][i, j])

    # Should _post_params method do any broadcasting?

    # Test pred method():
    prior = dpmm.NormInvChi2(1.0, 1.0, 1.0, 1.0)
    x = 1.0
    arr = prior.pred(x)
    assert isinstance(arr, float)

    x = np.array([1.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (1,)
    assert arr.dtype == float
    assert arr[0] == prior.pred(x[0])

    x = np.array([1.0, 2.0])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2,)
    assert arr.dtype == float
    for i, r in np.ndenumerate(arr):
        assert r == prior.pred(x[i])

    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    arr = prior.pred(x)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (2, 2)
    assert arr.dtype == float
    for (i, j), r in np.ndenumerate(arr):
        assert r == prior.pred(x[i, j])


if __name__ == '__main__':
    test_GaussianMeanKnownVariance()
    test_InvGamma()
    test_InvGamma2D()
    test_NormInvGamma()
    test_NormInvChi2()

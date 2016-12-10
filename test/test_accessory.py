import os
import sys
sys.path.insert(0, os.path.abspath('./src/'))


def test_get_iterable():
    from accessory import get_iterable
    import numpy as np

    vec = []
    actual = [ii for ii in get_iterable(vec)]
    expected = []

    assert np.array_equal(actual, expected)

    vec = 4
    actual = [ii for ii in get_iterable(vec)]
    expected = [vec]

    assert np.array_equal(actual, expected)

    vec = (0, 5)
    actual = [ii for ii in get_iterable(vec)]
    expected = vec

    assert np.array_equal(actual, expected)


def test_rgbstring2index():
    from accessory import rgbstring2index
    import numpy as np

    actual = rgbstring2index('rgb')
    expected = [0, 1, 2]

    assert np.array_equal(actual, expected)

    actual = rgbstring2index('rb')
    expected = [0, 2]

    assert np.array_equal(actual, expected)

    actual = rgbstring2index('b')
    expected = [2]

    assert np.array_equal(actual, expected)
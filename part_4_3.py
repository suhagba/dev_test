"""
The function `get_noisy_values` is hard to test because the values keep changing
every time you re-run the test.

Re-write `test_get_noisy_values` so that we still test some of the functionality
of `get_noisy_values`, but avoid the issue of tests failing randomly.

There are several acceptable solutions to this problem.

It should be possible to run the test in this file using PyTest
eg.
    pytest part_4_3.py

"""
import numpy as np


# set up a random seed value
np.random.seed(0)

def get_noisy_values():
    signal = np.array([1, 2, 3, 4, 5])
    noise = np.random.random(5)
    return signal + noise

def test_get_noisy_values():
    values = get_noisy_values()
    expected = np.array([[1.5488135,2.71518937,3.60276338,4.54488318,5.4236548]])
    # This will fail most of the time.
    assert (values.round(2) == expected.round(2)).all()

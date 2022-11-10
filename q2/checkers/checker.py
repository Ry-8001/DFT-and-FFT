import numpy as np


def rel_error(x, filename):
    y = np.load(filename)
    return  np.sum((x-y)**2)

def check_dtmf(x):
    print("TESTING DFT")
    error = rel_error(x, 'checkers/test_dtmf.npy')
    assert 1e-9 > error, "FAILED"
    print("PASSED")

def check_fft(x):
    print("TESTING RECURSIVE FFT 2D")
    error = rel_error(x, 'checkers/test_fft.npy')
    assert 1e-9 > error, "FAILED"
    print("PASSED")

def check_ifft(x):
    print("TESTING RECURSIVE IFFT 2D")
    error = rel_error(x, 'checkers/test_ifft.npy')
    assert 1e-9 > error, "FAILED"
    print("PASSED")
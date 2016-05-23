import sys
import os
import unittest

import numpy as np
import numpy.testing as npt

from oct2py import octave

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build', 'swig'))

import yafft


class TestSine(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')

        # Parameters
        N = 1000  # length of signal
        fs = 1000  # Hz, sampling frequency

        # Signals
        n = np.arange(0., N-1.)
        T = 1./fs  # s, sampling period
        t = n*T  # s, time vector

        x = np.sin(2.*np.pi*50.*t)
        self.x = x.astype(np.complex128)[None, :]

    def tearDown(self):
        octave.exit()

    def test_sine_using_octave_implementation(self):
        X = octave.my_fft(self.x)
        Y = np.fft.fft(self.x, 1024)
        npt.assert_almost_equal(X, Y, decimal=6)


if __name__ == '__main__':
    unittest.main()

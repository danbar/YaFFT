import sys
import os
import unittest

import numpy as np
import numpy.testing as npt

from oct2py import octave

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build', 'debug'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build', 'debug', 'swig'))

import yafft


def _create_sine(num_samples):
    fs = 1000  # Hz, sampling frequency

    n = np.arange(0., num_samples)
    T = 1./fs  # s, sampling period
    t = n*T  # s, time vector

    x = np.sin(2.*np.pi*50.*t)
    return x.astype(np.complex64)


class Test16SamplesSine(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        N = 16
        self.in1 = _create_sine(N)
        self.out1 = np.squeeze(octave.fft(self.in1, N))

    def tearDown(self):
        octave.exit()

    def test_octave_sine(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1, decimal=6)

    def test_dit_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1, decimal=6)

    def test_dif_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1, decimal=6)


class Test32SamplesSine(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        N = 32
        self.in1 = _create_sine(N)
        self.out1 = np.squeeze(octave.fft(self.in1, N))

    def tearDown(self):
        octave.exit()

    def test_octave_sine(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1, decimal=6)

    def test_dit_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1, decimal=6)

    def test_dif_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1, decimal=6)


class Test64SamplesSine(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        N = 64
        self.in1 = _create_sine(N)
        self.out1 = np.squeeze(octave.fft(self.in1, N))

    def tearDown(self):
        octave.exit()

    def test_octave_sine(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1, decimal=5)

    def test_dit_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1, decimal=5)

    def test_dif_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1, decimal=5)


class Test128SamplesSine(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        N = 128
        self.in1 = _create_sine(N)
        self.out1 = np.squeeze(octave.fft(self.in1, N))

    def tearDown(self):
        octave.exit()

    def test_octave_sine(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1, decimal=5)

    def test_dit_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1, decimal=5)

    def test_dif_sine(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1, decimal=5)


if __name__ == '__main__':
    unittest.main()

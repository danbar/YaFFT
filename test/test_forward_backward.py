import sys
import os
import unittest

import numpy as np
import numpy.testing as npt

from oct2py import octave

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build', 'debug'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build', 'debug', 'swig'))

import yafft


class Test2PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        self.in1 = np.ones(2, dtype=np.complex64)
        self.out1 = np.copy(self.in1)

    def tearDown(self):
        octave.exit()

#     def test_octave_2point_fft(self):
#         res = octave.my_fft(self.in1)
#         res = np.squeeze(res)
#         npt.assert_almost_equal(res, self.out1)

    def test_dit_2point_fft(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        yafft.ifft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1)

    def test_dif_2point_fft(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        yafft.ifft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1)


class Test4PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        self.in1 = np.ones(4, dtype=np.complex64)
        self.out1 = np.copy(self.in1)

    def tearDown(self):
        octave.exit()

#     def test_octave_4point_fft(self):
#         res = octave.my_fft(self.in1)
#         res = np.squeeze(res)
#         npt.assert_almost_equal(res, self.out1)

    def test_dit_4point_fft(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        yafft.ifft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1)

    def test_dif_4point_fft(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        yafft.ifft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1)


class Test8PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        self.in1 = np.ones(8, dtype=np.complex64)
        self.out1 = np.copy(self.in1)

    def tearDown(self):
        octave.exit()

#     def test_octave_8point_fft(self):
#         res = octave.my_fft(self.in1)
#         res = np.squeeze(res)
#         npt.assert_almost_equal(res, self.out1)

    def test_dit_8point_fft(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_TIME)
        yafft.ifft_radix2(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1)

    def test_dif_8point_fft(self):
        data = self.in1
        yafft.fft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        yafft.ifft_radix2(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1)


if __name__ == '__main__':
    unittest.main()

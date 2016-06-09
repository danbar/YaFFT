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
        self.in1 = np.array([1, 0], dtype=np.complex64)
        self.out1 = np.array([1, 1], dtype=np.complex64)

        self.in2 = np.array([0, 1], dtype=np.complex64)
        self.out2 = np.array([1, -1], dtype=np.complex64)

    def tearDown(self):
        octave.exit()

    def test_octave_2point_fft(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1)

        res = octave.my_fft(self.in2)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out2)

    def test_dit_2point_fft(self):
        data = self.in1
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1)

        data = self.in2
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out2)

    def test_dif_2point_fft(self):
        data = self.in1
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1)

        data = self.in2
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out2)


class Test4PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        self.in1 = np.array([1, 0, 0, 0], dtype=np.complex64)
        self.out1 = np.array([1, 1, 1, 1], dtype=np.complex64)

        self.in2 = np.array([0, 1, 0, 0], dtype=np.complex64)
        self.out2 = np.array([1, -1j, -1, 1j], dtype=np.complex64)

        self.in3 = np.array([0, 0, 1, 0], dtype=np.complex64)
        self.out3 = np.array([1, -1, 1, -1], dtype=np.complex64)

        self.in4 = np.array([0, 0, 0, 1], dtype=np.complex64)
        self.out4 = np.array([1, 1j, -1, -1j], dtype=np.complex64)

    def tearDown(self):
        octave.exit()

    def test_octave_4point_fft(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1)

        res = octave.my_fft(self.in2)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out2)

        res = octave.my_fft(self.in3)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out3)

        res = octave.my_fft(self.in4)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out4)

    def test_dit_4point_fft(self):
        data = self.in1
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1)

        data = self.in2
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out2)

        data = self.in3
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out3)

        data = self.in4
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out4)

    def test_dif_4point_fft(self):
        data = self.in1
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1)

        data = self.in2
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out2)

        data = self.in3
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out3)

        data = self.in4
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out4)


class Test8PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')  # load signal package

        # Test data
        v = 1/np.sqrt(2)

        self.in1 = np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype=np.complex64)
        self.out1 = np.array([1, 1, 1, 1, 1, 1, 1, 1], dtype=np.complex64)

        self.in2 = np.array([0, 1, 0, 0, 0, 0, 0, 0], dtype=np.complex64)
        self.out2 = np.array([1, v-1j*v, -1j, -v-1j*v, -1, -v+1j*v, 1j, v+1j*v], dtype=np.complex64)

        self.in3 = np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype=np.complex64)
        self.out3 = np.array([1, -1j, -1, 1j, 1, -1j, -1, 1j], dtype=np.complex64)

        self.in4 = np.array([0, 0, 0, 1, 0, 0, 0, 0], dtype=np.complex64)
        self.out4 = np.array([1, -v-1j*v, 1j, v-1j*v, -1, v+1j*v, -1j, -v+1j*v], dtype=np.complex64)

        self.in5 = np.array([0, 0, 0, 0, 1, 0, 0, 0], dtype=np.complex64)
        self.out5 = np.array([1, -1, 1, -1, 1, -1, 1, -1], dtype=np.complex64)

        self.in6 = np.array([0, 0, 0, 0, 0, 1, 0, 0], dtype=np.complex64)
        self.out6 = np.array([1, -v+1j*v, -1j, v+1j*v, -1, v-1j*v, 1j, -v-1j*v], dtype=np.complex64)

        self.in7 = np.array([0, 0, 0, 0, 0, 0, 1, 0], dtype=np.complex64)
        self.out7 = np.array([1, 1j, -1, -1j, 1, 1j, -1, -1j], dtype=np.complex64)

        self.in8 = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=np.complex64)
        self.out8 = np.array([1, v+1j*v, 1j, -v+1j*v, -1, -v-1j*v, -1j, v-1j*v], dtype=np.complex64)

    def tearDown(self):
        octave.exit()

    def test_octave_8point_fft(self):
        res = octave.my_fft(self.in1)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out1)

        res = octave.my_fft(self.in2)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out2)

        res = octave.my_fft(self.in3)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out3)

        res = octave.my_fft(self.in4)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out4)

        res = octave.my_fft(self.in5)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out5)

        res = octave.my_fft(self.in6)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out6)

        res = octave.my_fft(self.in7)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out7)

        res = octave.my_fft(self.in8)
        res = np.squeeze(res)
        npt.assert_almost_equal(res, self.out8)

    def test_dit_8point_fft(self):
        data = self.in1
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out1)

        data = self.in2
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out2)

        data = self.in3
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out3)

        data = self.in4
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out4)

        data = self.in5
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out5)

        data = self.in6
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out6)

        data = self.in7
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out7)

        data = self.in8
        yafft.fft(data, yafft.DECIMATION_IN_TIME)
        npt.assert_almost_equal(data, self.out8)

    def test_dif_8point_fft(self):
        data = self.in1
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out1)

        data = self.in2
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out2)

        data = self.in3
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out3)

        data = self.in4
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out4)

        data = self.in5
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out5)

        data = self.in6
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out6)

        data = self.in7
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out7)

        data = self.in8
        yafft.fft(data, yafft.DECIMATION_IN_FREQUENCY)
        npt.assert_almost_equal(data, self.out8)


if __name__ == '__main__':
    unittest.main()

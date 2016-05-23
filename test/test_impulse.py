import sys
import os
import unittest

import numpy as np
import numpy.testing as npt

from oct2py import octave

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'build', 'swig'))

import yafft


class Test2PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')

    def tearDown(self):
        octave.exit()

    def test_2point_fft_using_octave_implementation(self):
        test_in = np.array([[1, 0]], dtype=np.complex64)
        test_out = np.array([[1, 1]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 1]], dtype=np.complex64)
        test_out = np.array([[1, -1]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

    def test_2point_fft(self):
        data = np.array([1, 0], dtype=np.complex64)
        #
        yafft.fft(data)
        print(data)
        #
        #data = yafft.new_data(1)
        #yafft.fft(data, 1)
        #print(yafft.data_getitem(data, 0))
        #yafft.delete_data(data)


class Test4PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')

    def tearDown(self):
        octave.exit()

    def test_4point_fft_using_octave_implementation(self):
        test_in = np.array([[1, 0, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, 1, 1, 1]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 1, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, -1j, -1, 1j]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 1, 0]], dtype=np.complex64)
        test_out = np.array([[1, -1, 1, -1]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 0, 1]], dtype=np.complex64)
        test_out = np.array([[1, 1j, -1, -1j]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)


class Test8PointFFT(unittest.TestCase):

    def setUp(self):
        octave.restart()
        octave.addpath('./octave')
        octave.addpath('./test/octave')
        octave.eval('pkg load signal')

    def tearDown(self):
        octave.exit()

    def test_8point_fft_using_octave_implementation(self):
        v = 1/np.sqrt(2)

        test_in = np.array([[1, 0, 0, 0, 0, 0, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, 1, 1, 1, 1, 1, 1, 1]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 1, 0, 0, 0, 0, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, v-1j*v, -1j, -v-1j*v, -1, -v+1j*v, 1j, v+1j*v]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 1, 0, 0, 0, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, -1j, -1, 1j, 1, -1j, -1, 1j]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 0, 1, 0, 0, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, -v-1j*v, 1j, v-1j*v, -1, v+1j*v, -1j, -v+1j*v]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 0, 0, 1, 0, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, -1, 1, -1, 1, -1, 1, -1]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 0, 0, 0, 1, 0, 0]], dtype=np.complex64)
        test_out = np.array([[1, -v+1j*v, -1j, v+1j*v, -1, v-1j*v, 1j, -v-1j*v]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 0, 0, 0, 0, 1, 0]], dtype=np.complex64)
        test_out = np.array([[1, 1j, -1, -1j, 1, 1j, -1, -1j]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)

        test_in = np.array([[0, 0, 0, 0, 0, 0, 0, 1]], dtype=np.complex64)
        test_out = np.array([[1, v+1j*v, 1j, -v+1j*v, -1, -v-1j*v, -1j, v-1j*v]], dtype=np.complex64)

        test_res = octave.my_fft(test_in)
        npt.assert_almost_equal(test_res, test_out)


if __name__ == '__main__':
    unittest.main()

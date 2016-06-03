import unittest

import test_impulse
import test_signal


def suite():
    suite = unittest.TestSuite()
    # Impulse
    suite.addTest(unittest.makeSuite(test_impulse.Test2PointFFT))
    suite.addTest(unittest.makeSuite(test_impulse.Test4PointFFT))
    suite.addTest(unittest.makeSuite(test_impulse.Test8PointFFT))
    # Signal
    suite.addTest(unittest.makeSuite(test_signal.Test16SamplesSine))
    suite.addTest(unittest.makeSuite(test_signal.Test32SamplesSine))
    suite.addTest(unittest.makeSuite(test_signal.Test64SamplesSine))
    suite.addTest(unittest.makeSuite(test_signal.Test128SamplesSine))
    return suite

mySuite = suite()


def run():
    runner = unittest.TextTestRunner()
    runner.run(mySuite)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(mySuite)

import unittest
from calc.test.test import TestCalc

if __name__ == '__main':
    suite = unittest.TestSuite()
    tests = [TestCalc("test_multi"), TestCalc("test_add")]
    suite.addTest(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
#------------------------------------------------------------------------------
# TDD step-by-step example
#
# Adapted from Test-Driven Development By Example, Kent Beck.
#
# Robert Haines, University of Manchester, 2014
#------------------------------------------------------------------------------

import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(0, fibonacci(0), "fibonacci(0) should equal 0")
        self.assertEqual(1, fibonacci(1), "fibonacci(1) should equal 1")
        self.assertEqual(1, fibonacci(2), "fibonacci(2) should equal 1")
        self.assertEqual(2, fibonacci(3), "fibonacci(3) should equal 2")
        self.assertEqual(3, fibonacci(4), "fibonacci(4) should equal 3")

if __name__ == "__main__":
    unittest.main()

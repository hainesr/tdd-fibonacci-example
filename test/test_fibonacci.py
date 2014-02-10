#------------------------------------------------------------------------------
# COMP61542 TDD step-by-step example
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

if __name__ == "__main__":
    unittest.main()

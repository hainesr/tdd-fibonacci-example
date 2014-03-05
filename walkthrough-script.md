# COMP61542 TDD step-by-step example walkthrough script

## Adapted from Test-Driven Development By Example, Kent Beck.

## Robert Haines, University of Manchester, 2014

Each step in this script is related to the slide of the same name. All code is
designed to be copied directly into a shell terminal or text editor for
demonstration purposes.

------------------------------------------------------------------------------

### Setup

#### Terminal:

    mkdir src test

    export PYTHONPATH=`pwd`/src

------------------------------------------------------------------------------

### Step 1: Write a test

#### Editor (test/test_fibonacci.py):

    import unittest
    from fibonacci import fibonacci

    class TestFibonacci(unittest.TestCase):

        def test_fibonacci(self):
            self.assertEqual(0, fibonacci(0), "fibonacci(0) should equal 0")

    if __name__ == "__main__":
        unittest.main()

### Step 1: Run the test

#### Terminal:

    python test/test_fibonacci.py

### Step 1: Implement and re-test

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        return 0

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 2: Write a test

#### Editor (test/test_fibonacci.py):

    self.assertEqual(1, fibonacci(1), "fibonacci(1) should equal 1")

### Step 2: Run the tests

#### Terminal:

    python test/test_fibonacci.py

### Step 2: Implement and re-test

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        if n == 0: return 0
        return 1

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 3: Write a test

#### Editor (test/test_fibonacci.py):

    self.assertEqual(1, fibonacci(2), "fibonacci(2) should equal 1")

### Step 3: Run the tests

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 4: Write a test

#### Editor (test/test_fibonacci.py):

    self.assertEqual(2, fibonacci(3), "fibonacci(3) should equal 2")

### Step 4: Run the tests

#### Terminal:

    python test/test_fibonacci.py

### Step 4: Implement and re-test

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        if n == 0: return 0
        if n <= 2: return 1
        return 2

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 5: Write a test

#### Editor (test/test_fibonacci.py):

    self.assertEqual(3, fibonacci(4), "fibonacci(4) should equal 3")

### Step 5: Run the tests

#### Terminal:

    python test/test_fibonacci.py

### Step 5: Implement and re-test

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        if n == 0: return 0
        if n <= 2: return 1
        if n == 3: return 2
        return 3

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 6: Refactor and test

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        if n == 0: return 0
        if n <= 2: return 1
        if n == 3: return 2
        return 2 + 1

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 7: Refactor and test

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        if n == 0: return 0
        if n <= 2: return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

#### Terminal:

    python test/test_fibonacci.py

------------------------------------------------------------------------------

### Step 8: Refactor and test (and done)

#### Editor (src/fibonacci.py):

    def fibonacci(n):
        if n == 0: return 0
        if n == 1: return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

#### Terminal:

    python test/test_fibonacci.py

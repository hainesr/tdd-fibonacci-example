#------------------------------------------------------------------------------
# TDD step-by-step example
#
# Adapted from Test-Driven Development By Example, Kent Beck.
#
# Robert Haines, University of Manchester, 2014
#------------------------------------------------------------------------------

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

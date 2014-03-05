# COMP61542 TDD step-by-step example

## Adapted from Test-Driven Development By Example, Kent Beck.

## Robert Haines, University of Manchester, 2014

### Working through the steps

See walkthrough-slides.pdf and walkthough-script.md in this directory for the
individual steps.

In this repository each step is tagged so you can move through the example by
checking each step out as you get to it. For example:

    $ git checkout step-1

Tags are named `step-n`, where `1 <= n <= 8`.

### Running these examples
#### From a terminal

1.  Add the 'src' directory to the python library search path:

        $ export PYTHONPATH=`pwd`/src

1.  Run the tests:

        $ python test/test_fibonacci.py

#### Within Eclipse

1.  Open up the project properties and add the 'src' directory to its
    `PYTHONPATH`. How you do this will depend on which plugin you are using
    for python development within Eclipse.

1.  Right-click on 'test_fibonacci.py' in the 'test' directory and select
    'Run As -> Python Unit Test'. Again this may differ depending on which
    plugin you are using.

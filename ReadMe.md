# TDD step-by-step example

## Adapted from Test-Driven Development By Example, Kent Beck.

## Robert Haines, University of Manchester, 2014, 2015

### Working through the steps
#### In IPython/Jupyter Notebook

There is a [Docker
image](https://hub.docker.com/r/hainesr/tdd-fibonacci-example/) you can use so
that you don't need to install Jupyter on your own machine. Simply [install
Docker](http://docs.docker.com/windows/started/) and run:

```sh
docker run -d -p 8888:8888 --name tdd hainesr/tdd-fibonacci-example
```

This will download the image, if required, and then start the Jupyter notebook
server on port `8888`. Open your Web browser at http://localhost:8888 and then
click on the `walkthrough-notebook.ipynb` link to get started.

When you have finished, shut down the image with:

```sh
docker stop tdd
docker rm tdd
```

Alternatively you can load up `walkthrough-notebook.ipynb` into your favourite
IPython/Jupyter server.

Please see [the Jupyter
documentation](http://jupyter.readthedocs.org/en/latest/index.html) for more
information.

#### Using your local python setup

See walkthrough-slides.pdf or walkthough-script.md in this directory for the
individual steps.

In this repository each step is tagged so you can move through the example by
checking each step out as you get to it. For example:

```sh
git checkout step-1
```

Tags are named `step-n`, where `1 <= n <= 8`.

### Running these examples
#### From a terminal

1.  Add the 'src' directory to the python library search path:
    ```sh
    export PYTHONPATH=`pwd`/src
    ```

1.  Run the tests:
    ```sh
    python test/test_fibonacci.py
    ```

#### Within Eclipse

1.  Open up the project properties and add the 'src' directory to its
    `PYTHONPATH`. How you do this will depend on which plugin you are using
    for python development within Eclipse.

1.  Right-click on 'test_fibonacci.py' in the 'test' directory and select
    'Run As -> Python Unit Test'. Again this may differ depending on which
    plugin you are using.

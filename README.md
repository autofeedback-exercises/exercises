# Setting up python notebook exercises: QuickStart guide

## Basic notebooks 

1. Your notebooks will reside in [this GitHub repository](https://github.com/autofeedback-exercises/exercises). You need access to this repo to make changes, so either ask Andrew to add your GitHub username, or request access via GitHub. 
2. A basic notebook with no external dependencies (see below) can just be uploaded to the GitHub repository, preferably organised into an appropriately named module folder. 
3. Once the notebook is on GitHub, you can set up a link for your students. This link can be provided on Canvas, for instance, and when clicked, will spawn a fresh copy of the notebook on Google Colab. Take the url for your notebook file on GitHub, e.g.

`https://github.com/autofeedback-exercises/exercises/blob/main/MTH1025/intro/Calculation-Basics/Calculation-Basics.ipynb`

And replace `https://github.com` with `https://colab.research.google.com/github`

`https://colab.research.google.com/github/autofeedback-exercises/exercises/blob/main/MTH1025/intro/Calculation-Basics/Calculation-Basics.ipynb`

To make changes to that notebook, students have to save a copy. I usually just put this text either at the top of my notebook, or on canvas with the link: 

> **Remember to save a copy of the file so that you can edit it. (Click "File", then "Save a copy to Drive")**


## External dependencies

If you require the code in your notebook to load data from a file, the file can be hosted in the same directory as the notebook on GitHub. E.G if your script would ordinarily do something like

```python 
data = np.loadtxt('values.dat')
```

It will instead look like

```python
data = np.loadtxt('https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/New-SOR3012/Programming/values.dat')
```

Note that `github.com` has been replaced with `raw.githubusercontent.com`, and there is no `blob` in this url. 

You can do the same thing with images: 

`[alt-text](https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/MTH1025/intro/Debugging-Plotting-2/sinx.png)`

![alt-text](https://raw.githubusercontent.com/autofeedback-exercises/exercises/main/MTH1025/intro/Debugging-Plotting-2/sinx.png)


## AutoFeedback

To enable AutoFeedback tests, the directory structure must be as follows 

```bash
./exercise_notebook.ipynb
./setup.py
./testsrc/test_main.py
./testsrc/__init__.py
```

We'll address the contents of these files one by one

# `setup.py`

The `setup.py` tells python that the `testsrc` directory is a python package which can be installed (which we need to do later in the notebook). 

```python
from setuptools import setup, find_packages

setup(
    name='testsrc',
    version='1.0',
    description="Calculation-Basics",
    author="Andrew Brown",
    author_email='andrew.brown@qub.ac.uk',
    url="https://github.com/autofeedback-exercises/exercises.git",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['numpy']
)

```

You can change the description, author info and add any packages your tests require. If for instance you are using the `scipy` library in your tests, you would modify the last line to be `install_requires=['numpy', 'scipy']`. For simplicity, it's best that you leave the name as `testsrc`. 

# `./testsrc/__init__.py`

This is literally an empty file, but it needs to be present in the `testsrc` directory, and named correctly. Note that there are two underscores before and after the word `init`. 
# `./testsrc/test_main.py`

The best way to do this is to use another set of tests as a template. The links below will take you to simple example tests for 

1. [Checking variables](https://github.com/autofeedback-exercises/exercises/blob/main/MTH1025/intro/Calculation-Basics/testsrc/test_main.py)
2. [Checking functions](https://github.com/autofeedback-exercises/exercises/blob/main/MTH1025/intro/Functions/testsrc/test_main.py)
3. [Checking a plot](https://github.com/autofeedback-exercises/exercises/blob/main/MTH1025/intro/Debugging-Plots/testsrc/test_main.py)

The full documentation for each of the three main checking functions can be found [here](https://abrown41.github.io/AutoFeedback/usage.html)
# `exercise_notebook.ipynb`

You can name this file whatever you want, and into it you will put all the instructions and code that you want to provide to the students. To make AutoFeedback work you have to add the following:

## Boilerplate for loading testsrc

Add the following code cell to the top of your notebook

```python  highlight:"2-4,8,10"
# this code enables the automated feedback. If you remove this, you won't get any feedback
# so don't delete this cell!
try:
  import AutoFeedback
except (ModuleNotFoundError, ImportError):
  !pip install AutoFeedback
  import AutoFeedback

try:
  from testsrc import test_main
except (ModuleNotFoundError, ImportError):
  !pip install "git+https://github.com/autofeedback-exercises/exercises.git#subdirectory=MTH1025/algorithms/primes"
  from testsrc import test_main

def runtest(tlist):
  import unittest
  from contextlib import redirect_stderr
  from os import devnull
  with redirect_stderr(open(devnull, 'w')):
    suite = unittest.TestSuite()
    for tname in tlist:
      suite.addTest(eval(f"test_main.UnitTests.{tname}"))
    runner = unittest.TextTestRunner()
    try:
      runner.run(suite)
    except AssertionError:
      pass 
```

You will need to edit the line `!pip install "git+...` to point to the correct subdirectory on the github repository.

## testing cell

The boilerplate code imports all of the tests that you have defined in `test_main.py` so that you can execute them in the notebook to test student code. For instance, if I had set an exercise to define two variables `x` and `y`, and defined the corresponding tests `test_x` and `test_y` in `testsrc/test_main.py`, I would include two code cells in my notebook. One for the student to complete the exercise,
```python 
# Enter your code here:
import numpy as np

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

```
and one immediately following it which runs the tests:
``` python
# Test cell: run this to check your answer
runtest(['test_x', 'test_y'])
```
The names of the tests are provided to `runtest` as string variables in a list.

## testing figures

If you want to test a figure, AutoFeedback needs access to the current axes. It will look for the variable `fighand` (figure handle), which you should define at the end of the student's code block like this:
```python
# Enter your code here
import numpy as np
import matplotlib.pyplot as plt

plt.plot(x, y)


# This code is required for the autofeedback- don't delete it!
fighand = plt.gca()
```



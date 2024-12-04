class Exercise():
    def __init__(self, name='', location='./', types=[]):
        if not name:
            self._gather()
        else:
            self.name = name
            self.location = location 
            self.path = f"{self.location}/{self.name}"
            self.types = types


    def _gather(self):
        self.name = input('Enter exercise name: ')
        self.location = input('Enter exercise location (default ./): ')
        if not self.location:
            self.location = './'
        self.types = [1, 2, 3]


    def build(self):
        self._directories()
        self._setup()
        self._testing()
        open(f"{self.path}/testsrc/__init__.py", 'w').close()
            

    def _directories(self):
        from os.path import isdir, exists
        from os import mkdir

        assert isdir(self.location), f"Location {self.location} does not exist"
        assert not exists(f"{self.path}"), f"directory named {self.name} already exists"
        
        mkdir(f"{self.path}")
        mkdir(f"{self.path}/testsrc")

    def _testing(self):
        testTxt = """from AutoFeedback import check_vars, check_func, check_plot
import unittest


class UnitTests(unittest.TestCase) :
    def test_1(self):
        assert True
"""
        with open(f"{self.path}/testsrc/test_main.py", 'w') as f:
            f.write(testTxt)

    def _setup(self):
        import subprocess

        git_username = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE).stdout.strip().decode()
        git_email = subprocess.run(["git", "config", "user.email"], stdout=subprocess.PIPE).stdout.strip().decode()

        setupTxt=f"""from setuptools import setup, find_packages

setup(
    name='testsrc',
    version='1.0',
    description="{self.name}",
    author="{git_username}",
    author_email="{git_email}",
    url="https://github.com/autofeedback-exercises/exercises.git",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['numpy']
)
"""
        with open(self.path+"/setup.py", 'w') as f:
            f.write(setupTxt)

ex = Exercise('this', './')
ex.build()


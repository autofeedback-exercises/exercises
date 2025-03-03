class Exercise():
    def __init__(self, name='', location='./', types=[]):
        if not name:
            self._gather()
        else:
            self.name = name
            self.location = location 
            self.types = types
        self.path = f"{self.location}/{self.name}"


    def _gather(self):
        self.name = input('Enter exercise name: ')
        self.location = input('Enter exercise location (default ./): ')
        if not self.location:
            self.location = './'
        self.types = []
        for item in ['variables', 'functions', 'plots']:
            if input(f"Do you need to check {item}? (Y/N)").lower().startswith('y'):
                self.types.append(item)
            


    def build(self):
        self._directories()
        self._setup()
        self._testing()
        self._ipynb()
        open(f"{self.path}/testsrc/__init__.py", 'w').close()


    def _directories(self):
        from os.path import isdir, exists
        from os import mkdir

        goAhead = "y"
        if not(isdir(self.location)):
            goAhead = input(f"{self.location} does not exist, should I build it? (Y/N)")
        if goAhead.lower() == "y":
            mkdir(self.location)
        else:
            sys.exit(0, "operation cancelled")

        assert not exists(f"{self.path}"), f"directory named {self.name} already exists"
        
        mkdir(f"{self.path}")
        mkdir(f"{self.path}/testsrc")

    def _testing(self):
        allImports = ""
        importStr = "from AutoFeedback import"
        typeDict = {'variables': 'check_vars',
                    'functions': 'check_func',
                    'plots': 'check_plot, line',
                    'randomvars': 'randomvar'}

        for typ in self.types:
            allImports += f"{importStr} {typeDict[typ]} \n"

        testTxt = f"""{allImports}
import unittest


class UnitTests(unittest.TestCase):
    def test_1(self):
        assert True
"""
        with open(f"{self.path}/testsrc/test_main.py", 'w') as f:
            f.write(testTxt)


    def _ipynb(self):
        from importlib.resources import files
        nbfile = files('AutoFeedback_templater.data').joinpath('template.ipynb')
        with open(nbfile, 'r') as f:
            nbtext = f.readlines()

        with open(f"{self.path}/{self.name}.ipynb", 'w') as f:
            for line in nbtext:
                line = line.replace('_TEMPORARY_SUBDIRECTORY_', self.path)
                f.write(line)


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

def main():
    ex = Exercise()
    ex.build()


if __name__ == "__main__":
    main()

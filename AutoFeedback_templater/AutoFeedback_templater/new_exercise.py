def read_command_line():
    from argparse import ArgumentParser as AP
    parser = AP()
    parser.add_argument('-l', '--location', help="directory to build in",
                        default="./")
    parser.add_argument('-n', '--name', help='Name of new exercise',
                        default="New_Exercise")

    args = parser.parse_args()

    return args


def get_relative_to_exercises(full_path):
    """
    Finds an 'exercises' directory within the given path and returns
    the path relative to that 'exercises' directory.
    
    Args:
        full_path (str): The full path to analyze
        
    Returns:
        str: The path relative to the 'exercises' directory
        
    Raises:
        ValueError: If no 'exercises' directory is found in the path
        
    Example:
        >>> get_relative_to_exercises('/home/user/project/exercises/module1/task2')
        'module1/task2'
    """
    import os
    from pathlib import Path
    # Convert to absolute, normalized path
    abs_path = os.path.abspath(os.path.expanduser(full_path))
    path_parts = Path(abs_path).parts
    
    # Look for 'exercises' in the path
    if 'exercises' not in path_parts:
        raise ValueError("No 'exercises' directory found in the path")
    
    # Find the index of 'exercises' in the path
    exercises_index = path_parts.index('exercises')
    
    # Get the exercises directory path
    exercises_path = os.path.join(*path_parts[:exercises_index+1])
    
    # Get the relative path
    try:
        relative = Path(abs_path).relative_to(Path(exercises_path))
        return str(relative)
    except ValueError:
        # This shouldn't happen based on our logic, but just in case
        raise ValueError(f"Could not compute relative path from '{exercises_path}' to '{abs_path}'")

class Exercise():
    def __init__(self, args):
        from pathlib import Path
        self.name = args.name
        self.location = Path(args.location)
        self.path = self.location.joinpath(self.name)


    def build(self):
        self._directories()
        self._setup()
        self._testing()
        self._ipynb()
        open(f"{self.path}/testsrc/__init__.py", 'w').close()


    def _directories(self):
        from os.path import isdir, exists
        from os import makedirs, mkdir
        import sys

        goAhead = "y"
        if not(isdir(self.location)):
            goAhead = input(f"{self.location} does not exist, should I build it? (Y/N): ")
            if goAhead.lower() == "y":
                makedirs(self.location, exist_ok=True)
            else:
                sys.exit(0)

        assert not exists(f"{self.path}"), f"directory named {self.name} already exists"
        
        mkdir(self.path)
        mkdir(self.path.joinpath("testsrc"))

    def _testing(self):
        testTxt = f"""import unittest


class UnitTests(unittest.TestCase):
    def test_1(self):
        assert True
"""
        with open(self.path.joinpath("testsrc/test_main.py"), 'w') as f:
            f.write(testTxt)


    def _ipynb(self):
        from importlib.resources import files
        nbfile = files('AutoFeedback_templater.data').joinpath('template.ipynb')
        with open(nbfile, 'r') as f:
            nbtext = f.readlines()

        relative_loc = get_relative_to_exercises(self.path)

        with open(f"{self.path}/{self.name}.ipynb", 'w') as f:
            for line in nbtext:
                line = line.replace('_TEMPORARY_SUBDIRECTORY_', relative_loc)
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
        with open(self.path.joinpath("setup.py"), 'w') as f:
            f.write(setupTxt)

def main():
    args = read_command_line()
    ex = Exercise(args)
    ex.build()


if __name__ == "__main__":
    main()

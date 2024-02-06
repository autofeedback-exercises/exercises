from setuptools import setup, find_packages

setup(
    name='testsrc',
    version='1.0',
    description="Lists-1/",
    author="Andrew Brown",
    author_email='andrew.brown@qub.ac.uk',
    url="https://github.com/autofeedback-exercises/exercises.git",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['numpy']
)

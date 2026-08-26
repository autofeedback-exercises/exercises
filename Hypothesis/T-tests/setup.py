from setuptools import setup, find_packages

setup(
    name='testsrc',
    version='1.0',
    description="Exercises on doing hypothesis tests using Student's t-distribution",
    author="Gareth Tribello",
    author_email='g.tribello@qub.ac.uk',
    url="https://github.com/autofeedback-exercises/exercises.git",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['numpy','scipy']
)

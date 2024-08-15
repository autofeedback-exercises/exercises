from setuptools import setup, find_packages

setup(
    name='testsrc',
    version='1.0',
    description="Markov hitting times exercises for SOR3012",
    author="Gareth Tribello",
    author_email='g.tribello@qub.ac.uk',
    url="https://github.com/autofeedback-exercises/exercises.git",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['numpy']
)

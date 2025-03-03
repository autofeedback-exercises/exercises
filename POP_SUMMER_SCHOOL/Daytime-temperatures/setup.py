from setuptools import setup, find_packages

setup(
    name='testsrc',
    version='1.0',
    description="Daytime temperatures at the equator POP exercises",
    author="Gareth Tribello",
    author_email='g.tribello@qub.ac.uk',
    url="https://github.com/autofeedback-exercises/exercises.git",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=['numpy']
)

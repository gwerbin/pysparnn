from setuptools import setup, find_packages

with open("requirements.txt") as reqs_file:
    requirements = [line.strip() for line in reqs_file]

setup(
    name="pysparnn",
    version="0.4",
    description="Sparse (approximate) nearest neighbor search for python!",
    long_description="""Sparse (approximate) nearest neighbor search for python!""",
    author="Spencer Beecher",
    author_email="spencebeecher@gmail.com",
    packages=find_packges(exclude=['examples', 'examples.*', 'tests', 'tests.*']),
    install_requires=requirements
)

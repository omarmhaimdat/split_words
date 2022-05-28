from setuptools import setup
import setuptools

VERSION = "0.1.4"
DESCRIPTION = "A Python package for splitting text into sentences."

setup(
    name="split_words",
    version=VERSION,
    author="Omar MHAIMDAT",
    author_email="omarmhaimdat@gmail.com",
    url="https://github.com/omarmhaimdat/split_words",
    install_requires=[
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
#!/usr/bin/env python
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ntpl",
    version="0.0.3",
    author="Chris McCormick",
    author_email="chris@mccormick.cx",
    packages=["ntpl"],
    license="LICENSE.txt",
    description="Minimal library to modify and render HTML.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chr15m/ntpl",
    install_requires=[
        "beautifulsoup4==4.9.1",
        "pyhiccup==0.1",
    ],
)

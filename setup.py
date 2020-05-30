from setuptools import setup

setup(
    name="Un-template",
    version="0.0.1",
    author="Chris McCormick",
    author_email="chris@mccormick.cx",
    packages=["ntpl"],
    license="LICENSE.txt",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "beautifulsoup4==4.9.1",
        "pyhiccup==0.1",
    ],
)

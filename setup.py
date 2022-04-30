#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools.command.test import test as TestCommand
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

# Get the long description from the README file
with open(path.join(here, "README.md")) as in_file:
    long_description = in_file.read()

setup(
    name="jserve",
    version="0.0.2",
    description="A python server for production application support bidirectional communacation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="jcppython",
    author_email="jcppython@outlook.org",
    url="https://github.com/jcppython/jserve-python",
    packages=["jserve"],
    python_requires=">=3.6",
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

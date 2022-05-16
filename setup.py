#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools.command.test import test as TestCommand
from setuptools import setup

import os
import sys
import re
import codecs

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


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
with open(os.path.join(here, "README.md"), 'r') as in_file:
    long_description = in_file.read()


setup(
    name="jserve",
    version=find_version('jserve', '__init__.py'),
    description="A python server for production application support bidirectional communacation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="jcppython",
    author_email="jcppython@outlook.org",
    url="https://github.com/jcppython/jserve-python",
    packages=["jserve", "jserve/jsocketio", "jserve/jhttp"],
    python_requires=">=3.6",
    install_requires=[
        'python-socketio',
        'tornado',
        'eventlet'
    ],
    tests_require=[
        'tox',
        'python-dotenv'
    ],
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

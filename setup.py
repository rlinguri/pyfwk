#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pyfwk',
    version='0.0.8',
    description='Python Framework for MVC Applications',
    url='http://pyfwk.com',
    author='Roderic Linguri',
    author_email='rlinguri@mac.com',
    license='MIT',
    packages=['pyfwk'],
    py_modules = ['base','struc','utils'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License"
        ],
      )
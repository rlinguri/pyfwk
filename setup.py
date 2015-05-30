#!/usr/bin/env python

import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pyfwk',
      version='0.1.1',
      description='Python Framework for MVC Applications',
      url='http://pyfwk.com',
      author='Roderic Linguri',
      author_email='rlinguri@mac.com',
      license='MIT',
      packages=['pyfwk','pyfwk.base','pyfwk.struc','pyfwk.utils'],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Office/Business :: Financial",
          "License :: OSI Approved :: MIT License"
      ]
      )

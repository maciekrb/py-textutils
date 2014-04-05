#!/usr/bin/env python
from setuptools import setup

setup(
  name="textutils",
  version="0.1.2",
  author="Maciek Ruckgaber",
  author_email="maciekrb@gmail.com",
  description="Python module for sanitizing and transforming text",
  long_description=open('README.rst').read(),
  packages=["textutils"],
  license="BSD License",
  test_suite='nose.collector',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Text transformation in general',
    'License :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries'
  ]
)

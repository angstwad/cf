#!/usr/bin/env python

from setuptools import setup

setup(name='cf',
    version='0.40.1',
    description='A command line client to Rackspace Cloud Files',
    author='Paul Durivage',
    author_email='pauldurivage@gmail.com',
    license='Apache 2.0',
    url='https://github.com/angstwad/cf',
    install_requires = ['python-cloudfiles'],
    scripts = ['bin/cf']
)

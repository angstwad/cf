#!/usr/bin/env python

from setuptools import setup

setup(name='cf',
<<<<<<< HEAD
    version='0.20',
=======
    version='0.2.0',
>>>>>>> 5812b353482624694730085773a81de598a0111c
    description='A command line client to Rackspace Cloud Files',
    author='Paul Durivage',
    author_email='pauldurivage@gmail.com',
    license='Apache 2.0',
    url='https://github.com/angstwad/cf',
    install_requires = ['python-cloudfiles'],
    scripts = ['bin/cf']
)
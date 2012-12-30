#!/usr/bin/env python

from distutils.core import setup

setup(name='cf',
    version='0.1',
    description='cf -- A CLI to Cloud Files',
    author='Paul Durivage',
    author_email='pauldurivage@gmail.com',
    url='',
    modules = {'python-cloudfiles': 'cloudfiles'},
    scripts = ['bin/cf']
)
#!/usr/bin/env python

from setuptools import setup

setup(name='cf',
    version='0.1',
    description='cf -- A CLI to Cloud Files',
    author='Paul Durivage',
    author_email='pauldurivage@gmail.com',
    license='Apache 2.0',
    url='https://github.com/angstwad/cf',
    install_requires = ['python-cloudfiles'],
    scripts = ['bin/cf']
)
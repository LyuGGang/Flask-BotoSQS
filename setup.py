#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

setup(
    name="Flask-BotoSQS",
    version='0.2.0',
    py_modules=['flask_boto_sqs'],
    author='LyuGGang',
    author_email='me at lyuwonkyung dot com',
    url='https://github.com/LyuGGang/Flask-BotoSQS',
    description="Boto3 SQS integration for Flask",
    long_description=readme,
    install_requires=["Flask", "boto3"],
)
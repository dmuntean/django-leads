# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import leads

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = leads.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-leads',
    version=version,
    description='An easy, functional and customizable lead page for your next big thing, ready to use in your django project.',
    long_description=readme + '\n\n' + history,
    author='Diego Navarro Mellén',
    author_email='dnmellen@gmail.com',
    url='https://github.com/dnmellen/django-leads',
    packages=[
        'leads',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-leads',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)

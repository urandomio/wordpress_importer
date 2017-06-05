#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'docopt',
    'python-wordpress-xmlrpc',
    'requests',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='wordpress_importer',
    version='0.1.0',
    description="Utility to import data into wordpress from CSV using a template.",
    long_description=readme + '\n\n' + history,
    author="James Brink",
    author_email='brink.james@gmail.com',
    url='https://github.com/jamesbrink/wordpress_importer',
    packages=[
        'wordpress_importer',
    ],
    package_dir={'wordpress_importer':
                 'wordpress_importer'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='wordpress_importer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    scripts=['scripts/wordpress_importer', ],
    test_suite='tests',
    tests_require=test_requirements
)

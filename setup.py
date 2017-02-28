#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

exec(open('hl7/version.py').read())

setup(
    name='hl7',
    version=__version__,
    description='Python library parsing HL7 v2.x messages',
    long_description=__doc__,
    author=__author__,
    author_email=__email__,
    url=__url__,
    license=__license__,
    platforms=['POSIX', 'Windows'],
    keywords=['HL7', 'Health Level 7', 'healthcare', 'health care', 'medical record'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['hl7'],
    install_requires=['future', 'six'],
    setup_requires=['pytest-runner'],
    tests_require=['mock', 'pytest', 'unittest2'],
    entry_points={
        'console_scripts': [
            'mllp_send = hl7.client:mllp_send',
        ],
    },
    zip_safe=True,
)

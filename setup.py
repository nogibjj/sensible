#!/usr/bin/env python
"""
Setup script.
"""

from distutils.core import setup

setup(name = "Sensible",
    version = "0.2",
    description = "A sensible logging default",
    long_description = "A sensible logging default with env toggling",
    author = "Noah Gift",
    author_email = 'noah.gift@gmail.com',
    url = "https://noahgift@bitbucket.org/noahgift/sensible/",
    download_url = "https://bitbucket.org/noahgift/sensible/downloads/sensible-0.2.zip",
    platforms = ['any'],

    license = "GPLv3+",

    package_dir = {'sensible': 'src/sensible'},
    packages = ['sensible'],

    classifiers = [
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python'],
)

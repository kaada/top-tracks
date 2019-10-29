#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md") as readme_file:
    readme_data = readme_file.read()

setup(
    name="top-tracks",
    description="Generate top tracks for a given set of artists, using the spotify API.",
    long_description=readme_data,
    author="Olav Kaada",
    author_email="olav.kaada [æt] gmail.com",
    url="https://github.com/kaada/top-tracks",
    classifiers=[
        "Topic :: Software Development",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "tqdm",
        "spotipy"
    ]
)

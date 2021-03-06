#!/usr/bin/env python2

from setuptools import setup, find_packages
import glob

setup(name='FCChhAnalyses',
      version='0.1.0',
      description='Produce flat ROOT trees using FCCSW EDM in heppy',
      author='Clement Helsens',
      author_email='clement.helsens@cern.ch',
      url='https://github.com/HEP-FCC/FCChhAnalyses',
      requires=['heppy', 'ROOT'], # heppy is called heppyfwk if installed with pip
      packages=find_packages(),
      package_dir={"FCChhAnalyses": "../FCChhAnalyses"},
      scripts=glob.glob('scripts/*')
    )

#!/usr/bin/env python
from distutils.core import setup, find_packages

description = 'Dictionary of Obscure Words'
keywords = ['vocabulary', 'nlp', 'obscure']

setup(name='obscure_words',
      version='1.0',
      description=description,
      author='Giuseppe Vettigli',
      package_data={'': ['Readme.md']},
      include_package_data=True,
      py_modules=find_packages(),
      requires=['pandas'],
      url='https://github.com/JustGlowing/obscure_words',
      keywords=keywords)
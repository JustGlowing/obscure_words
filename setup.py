#!/usr/bin/env python
from distutils.core import setup

description = 'Dictionary of Obscure Words'
keywords = ['vocabulary', 'nlp', 'obscure']

setup(name='obscure_words',
      version='1.0',
      description=description,
      author='Giuseppe Vettigli',
      package_data={'': ['Readme.md']},
      data_files=[('words', ['obscure_words/data/obscure_dict.json'])]
      include_package_data=True,
      packages=['obscure_words', 'obscure_words.data'],
      requires=['pandas'],
      url='https://github.com/JustGlowing/obscure_words',
      keywords=keywords)

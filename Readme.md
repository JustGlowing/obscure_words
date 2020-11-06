Dictionary of Obscure Words
--------------------

This module allows you to use the Dictionary of Obscure Words in Python.

The original dictionary is available here: http://phrontistery.info

You can install this module using pip:

```
pip install git+https://github.com/JustGlowing/obscure_words
```

and use it as follows:

```python
>>> from obscure_words import scrape_obscure_words
>>> obscure_dict = scrape_obscure_words()
>>> obscure_dict['ophidiomancy']

'divination using snakes'
```
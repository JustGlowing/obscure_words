import importlib.resources as pkg_resources
import data
import json
import pandas as pd

def scrape_obscure_words(verbose=True):
	"""
	Scrapes the dictionary of obscure words from

		http://phrontistery.info
	"""
	url = 'http://phrontistery.info/{letter}.html'
	obscure_dictionary = {}
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		if verbose:
			print('Downloading letter %s' % letter)
		url_letter = url.format(letter=letter)
		words_table = pd.read_html(url_letter, attrs={'class': 'words'}, skiprows=1)[0]
		words_table.columns = ['word', 'definition']
		letter_dict = {w: d for w, d in zip(words_table.word, words_table.definition)}
		obscure_dictionary.update(letter_dict)
	if verbose:
		print('Congratulations, you downloaded %d obscure words.' % len(obscure_dictionary))
	return obscure_dictionary

def load_obscure_words():
	"""
	Returns the dictionary of obscure words.
	"""
	d = pkg_resources.open_text(data, 'obscure_dict.json')
	return json.load(d)
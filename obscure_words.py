import pandas as pd

def scrape_obscure_words(verbose=True):
	"""
	Thus function scrapes the dictionary of obscure words from

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
	return obscure_dictionary
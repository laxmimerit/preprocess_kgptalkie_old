from preprocess_kgptalkie import utils

__version__ = '0.10.3'

def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)

def get_mentions_counts(x):
	return utils._get_mentions_counts(x)

def get_digit_counts(x):
	return utils._get_digit_counts(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def cont_exp(x):
	return utils._cont_exp(x)

def get_emails(x):
	return utils._get_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def get_urls():
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_rt(x):
	return utils._remove_rt(x)

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_html_tags(x):
	return utils._remove_html_tags(x)

def remove_accented_chars(x):
	return utils._remove_accented_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils._make_base(x)

def get_value_counts(df, col):
	return utils._get_value_counts(df, col)

def get_word_freqs(df, col):
	return utils._get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return utils._remove_common_words(x, freq, n)

def remove_rarewords(x, freq, n=20):
	return utils._remove_rarewords(x, freq, n)

def spelling_correction(x):
	return utils._spelling_correction(x)

def remove_dups_char(x):
	return utils._remove_dups_char(x)

def get_basic_features(df):
	return utils._get_basic_features(df)

def get_ngram(df, col, ngram_range):
	return utils._get_ngram(df, col, ngram_range)

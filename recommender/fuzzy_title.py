""" Use fuzzy matching (= the process of finding similar results from search queries)
to insert title"""

from fuzzywuzzy import fuzz, process

def fuzzy_title(title):
    for title in movie_titles:
        process.extract(title, films)

from difflib import get_close_matches
from stemming.porter2 import stem
from string import capitalize
from bookadoc.redis_wrap import get_set
from django.db.models import Q

def clean_and_split(title):
    stops = ":;,.!/()\\&"
    words = [x.strip(stops) for x in title.split()]
    return [ word for word in words if len(word) > 0 ]

def stem_join(words):
    stemmed = map(stem, words)
    result = map(capitalize, stemmed)
    return '-'.join(result)

def correct(word):
    """
    Redis based implementation of a wordlist, which 'learns' the correct variations of misspelled words as more data is processed.
    It can however be extended to support any db system that supports concurrent read/writes.
    """
    wordlist = get_set('Wordlist')
    new_word = get_close_matches(word, wordlist, 1, 0.75)
    if new_word==[]:
        wordlist.add(word)
        new_word = word
    else:
        new_word = new_word[0]

    return new_word
    
def initialize_wordlist():
    """
    Initializes the wordlist with data in the models, can be called from a cron job or Celery
    """
    pass
     
def get_query(query_string, search_fields):
    """ 
    Returns a query, that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search fields.
    """
    query = None # Query to search for every search term        
    terms = clean_and_split(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

########################################################################
# Functions to process words and return list of words that can be
# formed from prefixes and suffixes
########################################################################


from typing import List
import json

func = lambda x: len(x) # Function to sort by length

# Open and load word_dictionary0634994.json into dictionary word_dictionary
json_file = open("word_dictionary0634994.json") 
word_dictionary = json.load(json_file)

def make_prefixes(word: str) -> List[str]:
    """
    Function to generate all the possible prefixes of a word
    """
    prefixes, prefix = set(), ""
    
    for char in word:
        prefix += char
        prefixes.add(prefix)
        
    return sorted(list(prefixes), key=func)


def make_suffixes(word: str) -> List[str]:
    """
    Function to generate all the possible suffixes of a word
    """
    suffixes, suffix = set(), ""
    
    for char in word[::-1]:
        suffix += char
        suffixes.add(suffix[::-1])
        
    return sorted(list(suffixes), key=func)


def generate(word1: str, word2: str) -> List[str]:
    """
    Function to generate all the possible valid words that can be
    formed with the prefixes of word1 and the suffixes of word2
    """
    prefixes, suffixes = make_prefixes(word1), make_suffixes(word2)
    valid_words = set()
    
    for prefix in prefixes:
        for suffix in suffixes:
            word = prefix + suffix
            if word in word_dictionary:
                valid_words.add(word)
                break

    return sorted(list(valid_words), key=func)
#!/usr/bin/env python

import nltk
import sys
import numpy
import string


def tokenise_strings(filename):
    nltk.download('popular')
    f = open(filename,"r")
    sentences = f.read().split(".")
    tokens = []
    for s in sentences:
        t = nltk.word_tokenize(s)
        tokens = t + tokens

    tokens_dict=set(tokens)
    new_words_set = []
    punc = string.punctuation

    for t in tokens_dict:
        t.lower()
        if t not in punc:
            new_words_set.append(t)
            
    return new_words_set

def tonkenise_w_repeating_words(filename):
    f = open(filename,"r")
    sentences = f.read().split(".")
    tokens = []
    for s in sentences:
        t = nltk.word_tokenize(s)
        tokens = t + tokens

    new_words_set = []
    punc = string.punctuation

    for t in tokens:
        t.lower()
        if t not in punc:
            new_words_set.append(t)

    return new_words_set



def file2prob(filename):
    words = tokenise_strings(filename)
    repreating_words = tonkenise_w_repeating_words(filename)
    words_dict  = { c: 0 for c in words}
    words_total = 0

    for c in repreating_words:
            if c.lower() not in words_dict:
                continue
            words_dict[c.lower()] += 1
            words_total += 1

    probs = { c: words_dict[c]/words_total for c in words_dict }
    return probs

def file2pairs(filename):
    """
    Read a file and return a dictionary of words and
    the probabilities of following word. That is, the
    conditional probability of a word given its
    predecessor.
    """
    words = tokenise_strings(filename)
    repeating_words = tonkenise_w_repeating_words(filename)
    words_dict  = { c: { a: 0 for a in words } for c in words }

    previous = None
    for c in repeating_words:
        if c.lower() not in words_dict:
            continue
        c = c.lower()
        if previous is None:
            previous = c
            continue
        words_dict[previous][c] += 1
        previous = c              
    probs = { c: { d: words_dict[c][d]/sum(words_dict[c].values()) if sum(words_dict[c].values()) != 0 else 0 for d in words } for c in words }
  
    return probs

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: %s filename letter" % sys.argv[0])
        sys.exit(-1)
        
    filename = sys.argv[1]
    letter = sys.argv[2]

    probs = file2prob(filename)
    print(probs[letter])

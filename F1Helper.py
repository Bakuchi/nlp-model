#!/usr/bin/python
# -*- coding: utf-8 -*-
import mmap
import codecs
import sys
import unicodedata
import nltk
from nltk.probability import LidstoneProbDist, SimpleGoodTuringProbDist
from nltk.stem import SnowballStemmer

__author__ = 'Rustem'

default_stopwords = set(nltk.corpus.stopwords.words('russian'))

tbl = dict.fromkeys(i for i in xrange(sys.maxunicode)
                    if unicodedata.category(unichr(i)).startswith('P'))


def remove_punctuation(text):
    return text.translate(tbl)


def surface_no_pm(text):
    corpus = remove_punctuation(text)
    return clear(nltk.WordPunctTokenizer().tokenize(corpus))


def stemmed(text):
    stemmer = SnowballStemmer("russian")
    nonstemmed = surface_no_pm(text)
    return clear([stemmer.stem(w) for w in nonstemmed])


def suffix_x(x, text):
    sym = "%"
    tokens = surface_no_pm(text)
    newtok = []
    for word in tokens:
        if len(word) < x:
            mult = x - len(word)
            newtok.append((mult * sym + word))
        elif len(word) > x:
            newtok.append(word[-x:])
        else:
            newtok.append(word)
    return newtok


def clear(tokenlist):
    print "LOWERCASING AND CLEARING tokenlist from stop words"
    tokens = tokenlist
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in default_stopwords]
    return tokens


def process_tokenization(word_type, text):
    print "NOW TOKENIZING"
    if word_type == "surface_all":
        tokens = clear(nltk.WordPunctTokenizer().tokenize(text))
    elif word_type == "surface_no_pm":
        tokens = surface_no_pm(text)
    elif word_type == "stem":
        tokens = stemmed(text)
    else:
        tokens = suffix_x(int(word_type[7:]), text)

    return tokens


def process_frequency(tokens, frequency):
    print "Processing frequency"
    fdist = nltk.FreqDist(tokens)
    newtokens = []
    tlen = str(len(tokens))
    line = 0
    for word in tokens:
        line = line + 1
        print "Now on token " + str(line) + " out of " + tlen
        if fdist[word] > frequency:
            newtokens.append(word)
        else:
            newtokens.append("<UNK>")
    return newtokens


def process_smoothing(laplace, gt):
    if laplace:
        return lambda fdist, bins: LidstoneProbDist(fdist, 1)
    elif gt:
        return lambda fdist, bins: SimpleGoodTuringProbDist(fdist)
    else:
        return lambda fdist, bins: LidstoneProbDist(fdist, 0)


def build_model(root, encoding, word_type, n, laplace, good_turing, frequency):
    tokens = []
    line = 0

    with open(root, 'r') as f:
        # Size 0 will read the ENTIRE file into memory!
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)  # File is open read-only

        # Proceed with your code here -- note the file is already in memory
        # so "readine" here will be as fast as could be
        data = m.readline()
        while data:
            line = line + 1
            tokens.extend(process_tokenization(word_type, data.decode(encoding)))
            print "Reading  " + str(line) + " line of the corpus file"

            # Do stuff
            data = m.readline()

    # with codecs.open(root, encoding=encoding) as f:
    #     data = f.readline()
    #     while data:
    #         line = line + 1
    #         tokens.extend(process_tokenization(word_type, data))
    #         print "Reading  " + str(line) + " line of the corpus file"
    #         data = f.readline()
    tokens = process_frequency(tokens, frequency)
    est = process_smoothing(laplace, good_turing)
    print "Now making model"
    model = nltk.NgramModel(n=n, train=tokens, estimator=est)
    return model

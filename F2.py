#!/usr/bin/python
# -*- coding: utf-8 -*-
import getopt
import pickle
import sys
import nltk
from tabulate import tabulate
from F2Helper import recursive_sentence

__author__ = 'admin-r'


def main(argv):
    lm = 'path to model'
    tokens = ""
    try:
        opts, args = getopt.getopt(argv, "ho:",
                                   ["lm=", "tokens="])
    except getopt.GetoptError:
        print 'F2.py --lm </full/path/to/model> --tokens'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'F2.py --lm </full/path/to/model> --tokens divided by whitespace'
            sys.exit()
        elif opt in "--lm":
            lm = arg
        elif opt in "--tokens":
            tokens = arg.decode('utf-8')
    print tabulate([['Source model: ', lm], ['Tokens: ', tokens]],
                   headers=['Argument', 'User Input'])

    tokens = nltk.WordPunctTokenizer().tokenize(tokens)
    print "Now loading model"
    model = load_model(lm)
    print "Sentence: "
    recursive_sentence(model, tokens)


def load_model(path):
    with open(path, 'rb') as pickle_file:
        content = pickle.load(pickle_file)
    return content


if __name__ == "__main__":
    main(sys.argv[1:])

# python F2.py --lm=/home/admin-r/nlp/pickled/m08gtnpm2wf20.pickle --tokens "президент владимир россии путин"

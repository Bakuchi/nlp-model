#!/usr/bin/python
# -*- coding: utf-8 -*-
import getopt
import pickle
import sys
from F3Helper import ml_words
from tabulate import tabulate

__author__ = 'admin-r'


def main(argv):
    lm = 'path to model'
    guess = 0
    sentence = ""
    try:
        opts, args = getopt.getopt(argv, "ho:",
                                   ["lm=", "guess-num=", "sentence="])
    except getopt.GetoptError:
        print 'F3.py --lm </full/path/to/model> --guess-num --sentence= " your sentence" '
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'F3.py --lm </full/path/to/model> --guess-num --sentence= " your sentence" '
            sys.exit()
        elif opt in "--lm":
            lm = arg
        elif opt in "--guess-num":
            guess = arg
        elif opt in "--sentence":
            sentence = arg.decode('utf-8')
    print tabulate([['Source model: ', lm], ['Guess num: ', guess], ['Sentence: ', sentence]],
                   headers=['Argument', 'User Input'])
    print "Now loading model"
    model = load_model(lm)
    ml_words(model, int(guess), sentence)


def load_model(path):
    with open(path, 'rb') as pickle_file:
        content = pickle.load(pickle_file)
    return content


if __name__ == "__main__":
    main(sys.argv[1:])

# python F3.py --lm /home/admin-r/nlp/pickled/m08gtnpm2wf20.pickle --guess-num 2 --sentence "Я люблю <SKIP>"

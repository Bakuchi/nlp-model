#!/usr/bin/python
# -*- coding: utf-8 -*-
import getopt
import pickle
import sys
import codecs
from tabulate import tabulate

__author__ = 'Rustem'


def main(argv):
    lm = 'path to model'
    src = 'path to collection'
    try:
        opts, args = getopt.getopt(argv, "ho:",
                                   ["lm=", "src="])
    except getopt.GetoptError:
        print 'F2.py --lm </full/path/to/model> '
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'F2.py --lm </full/path/to/model> '
            sys.exit()
        elif opt in "--lm":
            lm = arg
        elif opt in "--src":
            src = arg
    print tabulate([['Source model: ', lm]],
                   headers=['Argument', 'User Input'])
    collection = codecs.open(src, encoding='utf-8')
    model = load_model(lm)

    print model.perplexity(collection)


def load_model(path):
    with open(path, 'rb') as pickle_file:
        content = pickle.load(pickle_file)
    return content


if __name__ == "__main__":
    main(sys.argv[1:])

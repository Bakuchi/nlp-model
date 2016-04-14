#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'admin-r'

import sys
import getopt
import pickle
from tabulate import tabulate


def main(argv):
    lm = 'path to model'
    wn = 10
    try:
        opts, args = getopt.getopt(argv, "ho:",
                                   ["lm=","wn="])
    except getopt.GetoptError:
        print 'F4.py --lm </full/path/to/model> --wn how many words in sentence(10 by default) '
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'F4.py --lm </full/path/to/model> --wn how many words in sentence(10 by default)  '
            sys.exit()
        elif opt in "--lm":
            lm = arg
        elif opt in "--wn":
            wn = arg
    print tabulate([['Source model: ', lm],['Wordnum: ', wn]],
                   headers=['Argument', 'User Input'])
    print "Now loading model"
    model = load_model(lm)
    print " ".join(model.generate(int(wn)))


def load_model(path):
    with open(path, 'rb') as pickle_file:
        content = pickle.load(pickle_file)
    return content


if __name__ == "__main__":
    main(sys.argv[1:])

# python F4.py --lm=/home/admin-r/nlp/pickled/m08gtsuf4n2wf10.pickle --wn=5
# python F4.py --lm=/home/admin-r/nlp/pickled/1.pickle --wn=5
#!/usr/bin/python
# -*- coding: utf-8 -*-
import getopt
import pickle
import sys
import F1Helper
import dill
from tabulate import tabulate

__author__ = 'Rustem'


def main(argv):
    src_texts = 'N\A'
    text_encoding = 'N\A'
    word_type = 'N\A'
    n = 1
    laplace = False
    good_turing = False
    unk_word_freq = 0
    output = "/home/admin-r/nlp/pickled/new.pickle"
    try:
        opts, args = getopt.getopt(argv, "ho:n:",
                                   ["src-texts=", "text-encoding=", 'word-type=', "laplace", "good-turing",
                                    "unknown-word-freq="])
    except getopt.GetoptError:
        print 'F1.py --src-texts </full/path/to/corpus> -o <outputfile>.pickle'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print 'F1.py --src-texts </full/path/to/corpus> --text-encoding "encoding" ' \
                  '--word-type <surface_all | surface_no_pm | stem | suffix_X>  -n 1-.. ' \
                  '--laplace  --good-turing  --unknown-word-freq 1-..' \
                  '  -o <outputfile>.pickle'
            sys.exit()
        elif opt in "--src-texts":
            src_texts = arg
        elif opt in "--text-encoding":
            text_encoding = arg
        elif opt in "--word-type":
            word_type = arg
        elif opt in "-n":
            n = arg
        elif opt in "--laplace":
            laplace = True
        elif opt in "--good-turing":
            good_turing = True
        elif opt in "--unknown-word-freq":
            unk_word_freq = arg
        elif opt in "-o":
            output = arg
    print tabulate([['Source text: ', src_texts], ['Text encoding: ', text_encoding],
                    ['Word type: ', word_type], ['N gramm: ', n],
                    ['Laplace: ', laplace], ['Good-Turing: ', good_turing],
                    ['Unknown word frequency: ', unk_word_freq], ['Output model file: ', output]],
                   headers=['Argument', 'User Input'])

    model = F1Helper.build_model(src_texts, text_encoding, word_type, int(n), laplace, good_turing, int(unk_word_freq))
    print "Dumping model"
    dump_model(model, output)
    print "DONE, now get your model at: " + output


def dump_model(model, output):
    f = open(output, 'wb')
    pickle.dump(model, f)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])

# python F1.py --src-texts /home/admin-r/nlp/corpus/news.2008.ru.shuffled --text-encoding utf-8 --word-type "stem" -n 2 -o /home/admin-r/nlp/pickled/model2008.pickle
# python F1.py --src-texts /home/admin-r/nlp/corpus/news.2008.ru.shuffled --text-encoding utf-8 --word-type "stem" --good-turing -n 2 -o /home/admin-r/nlp/pickled/model2008gt.pickle
# python F1.py --src-texts /home/admin-r/nlp/corpus/news.2008.ru.shuffled --text-encoding utf-8 --word-type "suffix_4" --good-turing -n 2  --unknown-word-freq 10 -o /home/admin-r/nlp/pickled/m08gtsuf4n2wf10.pickle
# python F1.py --src-texts /home/admin-r/nlp/corpus/news.2013.ru.shuffled --text-encoding utf-8 --word-type "surface_no_pm" --good-turing -n 2  --unknown-word-freq 20 -o /home/admin-r/nlp/pickled/m13gtnpm2wf20.pickle
# python F1.py --src-texts /home/admin-r/nlp/corpus/news.2013.ru.shuffled --text-encoding utf-8 --word-type "surface_no_pm" --good-turing -n 2  --unknown-word-freq 20 -o /home/admin-r/nlp/pickled/m13gtnpm2wf20.pickle
# python F1.py --src-texts /home/admin-r/nlp/corpus/news.2008.ru.shuffled --text-encoding utf-8 --word-type "surface_no_pm" --good-turing -n 2  --unknown-word-freq 10 -o /home/admin-r/nlp/pickled/m08gtnpm2wf20.pickle

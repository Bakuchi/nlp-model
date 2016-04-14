#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'admin-r'


def ml_words(model, guess_n, sentence):
    parts = sentence.split(u"<SKIP>")
    parts.remove(u"")
    words = []
    for gn in range(0, guess_n):
        word2 = []
        for part in parts:
            word = model.choose_random_word(part)
            word2.append(word)
        words.append(word2)

    mk_sentences(parts, words)


def mk_sentences(initsent, words):
    sentences = []
    for word1 in words:
        sent = []
        for i in range(0, len(word1)):
            sent.append(initsent[i])
            sent.append(word1[i])
        sentences.append(sent)
    pr_sentences(sentences)


def pr_sentences(sentences):
    for sentence in sentences:
        print " ".join(sentence)

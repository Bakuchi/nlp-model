#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'admin-r'


def recursive_sentence(model, tokens):
    tk = tokens
    tok = tokens
    for i in range(0, len(tok)):
        tok = recc_step(model, tok)
        for t in tk:
            if tok.count(t) < 1:
                tok.append(t)

    print " ".join(tok)


def recc_step(model, tokens):
    maximum_phrase = []
    max_prob = 0
    for i in range(0, len(tokens)):
        for j in range(0, len(tokens)):
            prtok = []
            if (tokens[i] != tokens[j]):
                prtok.append(tokens[j])
                nowprob = model.prob(tokens[i], prtok)
                if nowprob > max_prob:
                    max_prob = nowprob
                    maximum_phrase.insert(0, tokens[i])
                    maximum_phrase.insert(1, tokens[j])
    return maximum_phrase

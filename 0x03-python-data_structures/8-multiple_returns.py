#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tupl = (0, None)
        return tupl
    lenth = len(sentence)
    tupl = (lenth, sentence[0])
    return tupl

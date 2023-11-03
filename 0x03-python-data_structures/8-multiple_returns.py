#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        firstletter = None
    else:
        firstletter = sentence[0]
    return (length, firstletter)

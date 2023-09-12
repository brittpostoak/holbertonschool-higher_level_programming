#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        x = None
    else:
        x = sentence[0]
    e = (a, x)
    return(e)

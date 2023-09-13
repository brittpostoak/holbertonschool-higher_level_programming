#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
        return (0)
    Roma = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roma = roman_string
    ilist = [Roma[i[0]] if Roma[i[0]] >= Roma[i[1]] else (-1*Roma[i[0]])
             for i in zip(roma, roma[1:] + roma[-1])]
    dec = sum(ilist)
    return (dec)

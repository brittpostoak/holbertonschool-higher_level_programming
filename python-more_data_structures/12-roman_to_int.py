#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
    return 0

  roman_numeral_dict = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
  }

  total = 0
  i = 0
  while i < len(roman_string):
    current_value = roman_numeral_dict[roman_string[i]]
    next_value = None
    if i + 1 < len(roman_string):
      next_value = roman_numeral_dict[roman_string[i + 1]]

    if next_value and current_value < next_value:
      total -= current_value
    else:
      total += current_value
    i += 1

  return total

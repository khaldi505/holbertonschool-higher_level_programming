#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None\
            or roman_string == "":
        return 0
    result = 0
    a_dictionary = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    for x in range(len(roman_string)):
        if x > 0 and a_dictionary[roman_string[x]]\
                > a_dictionary[roman_string[x - 1]]:
            result += a_dictionary[roman_string[x]]\
                - 2 * a_dictionary[roman_string[x - 1]]
        else:
            result += a_dictionary[roman_string[x]]
    return result

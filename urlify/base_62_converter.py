#
# Adapted from bhelx base_62_converter gist (https://gist.github.com/bhelx/778542)
#
# Made changes to the alphabet ordering, ord() removal and adapted for python3
# Changes made in a attempt to hide direct correlation to Django id's
#
# saturate()  takes the base 62 key, as a string, and turns it back into an integer
# dehydrate() takes an integer and turns it into the base 62 string
#
import math
import string


ALPHABET = list(string.ascii_letters + string.digits)
BASE = len(ALPHABET)


def alphabet_index(char):
    if char in ALPHABET:
        return ALPHABET.index(char)
    else:
        raise ValueError('The character "{}" is not in the alphabet.'.format(char))


def saturate(key):
    """
    Turn the base [BASE] number [key] into an integer
    """
    int_sum = 0
    reversed_key = key[::-1]
    for idx, char in enumerate(reversed_key):
        int_sum += alphabet_index(char) * int(math.pow(BASE, idx))
    return int_sum


def dehydrate(integer):
    """
    Turn an integer [integer] into a base [BASE] number
    in string representation
    """

    # we won't step into the while if integer is 0
    # so we just solve for that case here
    if integer == 0:
        return ALPHABET[integer]

    string = ""
    while integer > 0:
        remainder = integer % BASE
        string = ALPHABET[remainder] + string
        integer //= BASE
    return string
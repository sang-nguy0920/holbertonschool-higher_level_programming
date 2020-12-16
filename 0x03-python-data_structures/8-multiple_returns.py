#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    first_character = ""
    if sentence_length == 0:
        first_character = None
    else:
        first_character = sentence[0]
    return (sentence_length, first_character)

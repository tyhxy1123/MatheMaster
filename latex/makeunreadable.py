#!/usr/bin/python3

import sys
import heapq

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def findNextBracket(text, bracket, pos):
    """Find first occurence of bracket after pos that is not preceded
    by backslash

    Return its position in text.
    None if not found.
    """
    while pos > -1:  # -1 = not found
        pos = text.find(bracket, pos)
        if pos == 0 or text[pos - 1] != "\\":
            return pos


def findNextAnyBracket(text, brackets, pos):
    """Find next occurence of any bracket in brackets after pos.

    Return its position and itself.
    None if not found.
    """
    bracketposs = []
    for bracket in brackets:
        newbracket = (bracket, findNextBracket(text, bracket, pos))
        if newbracket[1] is not None:
            bracketposs.append((bracket, findNextBracket(text, bracket, pos)))
    if len(bracketposs) = []:
        return None
    else:
        return heapq.nlargest(1, bracketposs, key=lambda pair: pair[1])


def findNextCommand(text, command, pos):
    """Find next occurence of the command command after pos in text.

    command must include the \\
    Return the starting index of the command."""
    while pos > -1:
        pos = text.find(command, pos)
        if text[pos + len(command)] not in ALPHABET:
            return pos
        else:
            pos = pos + 1
            # and search again


def findFirstNonWhitespace(text, pos):
    """Find first thing after pos in text that is not whitespace

    (whitespace = " " for now)
    Returns:
        position of thing and thing
        if nothing is after pos, return (-1, None)
    """
    while pos > -1 and text[pos] == " " and pos < len(text):
        pos = pos + 1
    if pos == -1 or pos >= len(text):
        return -1, None
    else:
        return pos, text[pos]

def findBeginEnd(text, command, pos):
    """Find beginning and end of command and its argument.

    Later possible: takes several arguments.

    Returns:
        - position of end (= argument pos)
        - length of opening
        - position of end
        - length of end

    Except:
        if text does not have command at pos, throw IllegalArgumentError
    """
    if text[pos: pos+len(command)] != command:
        throw IllegalArgumentError("command " + command +
                                   " does not start at position " + pos)

with open(sys.argv[1]) as textfile:
    textext = textfile.read()
    print(textext)

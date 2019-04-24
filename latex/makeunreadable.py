#!/usr/bin/python3

import sys
import heapq

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*"
# * is part of commands

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
    -1, None if not found.
    """
    bracketposs = []
    for bracket in brackets:
        newbracket = (bracket, findNextBracket(text, bracket, pos))
        if newbracket[1] is not None:
            bracketposs.append((bracket, findNextBracket(text, bracket, pos)))
    if len(bracketposs) == 0:
        return -1, None
    else:
        print("debug findNextAnyBracket list:", bracketposs)
        returnvalue = heapq.nsmallest(1, bracketposs, key=lambda pair: pair[1])[0]
        print("debug returnvalue", returnvalue)
        return heapq.nsmallest(1, bracketposs, key=lambda pair: pair[1])[0]


def findNextCommand(text, command, pos):
    """Find next occurence of the command command after pos in text.

    command must include the backslash
    Return the starting index of the command.
    Return -1 if not found.
    """
    while True:
        pos = text.find(command, pos)
        if pos == -1:
            return -1
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
        - position of start (= argument pos)
        - length of start
        - position of end
        - length of end

    Except:
        if text does not have command at pos, throw IllegalArgumentError
    """
    try:
        print(command + " should be " + text[pos: pos+len(command)])
        if text[pos: pos+len(command)] != command:
            raise IndexError()
    except IndexError:
            raise ValueError("command " + str(command)
                             + " does not start at position " + str(pos))
    openingPos, opening = findFirstNonWhitespace(text, pos + len(command))
    if openingPos == -1:
        raise ValueError("no argument found for command " + command
                         + " starting at position " + pos)
    print("debug openingPos=", openingPos, "opening=", opening)
    if opening == "{":
        bracketLevel = 1
        bracketPos = openingPos
        while bracketLevel > 0:
            print("debug bracketLevel=", bracketLevel, "bracketPos=",
                  bracketPos)
            bracket, bracketPos = findNextAnyBracket(
                text, "{" + "}", bracketPos + 1)
            if bracket is None:
                raise ValueError("no suitable bracket found"
                                 + " for command " + str(command)
                                 + " at position " + str(position)
                                 + " with last bracketlevel "
                                 + str(bracketLevel) + ".")
            elif bracket == "{":
                bracketLevel = bracketLevel + 1
            elif bracket == "}":
                bracketLevel = bracketLevel - 1
            else:
                raise ValueError(
                    "output of findNextAnyBracket is invalid")
        return pos, openingPos - pos + 1, bracketPos, 1
    else:
        return pos, openingPos - pos, openingPos + 1, 0


def replaceCommand(text, openingPos, openingLength, closingPos,
                   closingLength, newOpening, newClosing):
    """Replace command with the symbols.

    Returs:
        altered text
    """
    if openingPos == -1 or closingPos == -1:
        print("Warning")
        print("-------")
        print("the following replacement is invalid:")
        print("openingPos=", openingPos, "openingLength=", openingLength,
              "closingPos=", closingPos, "closingLenght=", closingLenght,
              "newOpening=", newOpening, "newClosing=", newClosing)
        print("-----------")
    else:
        return (text[:openingPos] + newOpening
                + text[openingPos + openingLength:closingPos] # argument
                + newClosing
                + text[closingPos + closingLength:])


def replaceAllOfOneCommand(text, command, newOpening, newClosing):
    """Clean text of command.

    Replace all occurances of the commmand command with
    the newOpening and newClosing.

    Returns altered text.
    """
    pos = 0
    while True:
        pos = findNextCommand(text, command, pos)
        if pos == -1:
            return text
        pos, openingLength, closingPos, closingLength = findBeginEnd(
            text, command, pos)
        text = replaceCommand(text, pos, openingLength, closingPos,
                              closingLength, newOpening, newClosing)


def replaceArgumentLessCommand(text, command, replacement):
    """Clean text of commmand.

    Command cannot have arguments.
    Replace with replacement.

    Returns:
        altered text
    """
    pos = 0
    print("old text:\n", text)
    while True:
        pos = findNextCommand(text, command, pos)
        text = text[:pos] + replacement + text[pos + len(command):]
        if pos == -1:
            return text


if __name__ == "__main__":
    with open(sys.argv[1]) as textfile:
        textext = textfile.read()
        toBeReplacedWithArgument = [
            (r"\norm*", r"\|", r"\|"),
            (r"\abs*", r"|", r"|"),
            (r"\halfnorm*", r"|", r"|"),
            (r"\set*", r"\{", r"\}"),
            (r"\norm", r"\left\|", r"\right\|"),
            (r"\abs", r"\left|", r"\right|"),
            (r"\halfnorm", r"\left|", r"\right|"),
            (r"\set", r"\left\{", r"\right\}")
        ]
        toBeReplacedWithoutArgument = [
            (r"\coloneqq", ":="),
            (r"\eqqcolon", "=:"),
            (r"\abschluss", r"\bar"),
            (r"\rand", r"\boundary")
        ]
        for myCommand, myOpening, myClosing in toBeReplacedWithArgument:
            textext = replaceAllOfOneCommand(textext, myCommand, myOpening,
                                             myClosing)
            print("newtext after replacing ", myCommand, "\n", textext)

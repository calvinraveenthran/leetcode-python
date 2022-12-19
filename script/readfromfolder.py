#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join


def readandprintfolder(folder):
    onlyfiles = listdir(folder)
    print("{}".format(onlyfiles))

def readandprintfile(file):
    with open(infile) as f:
    f = f.readlines()
    print("{}".format(f))

def main():
    """Read from folder"""
    folder = "/Users/calvinraveenthran/Documents/code/python/leetcode-python/files"
    readandprintfolder(folder)
    file = "/Users/calvinraveenthran/Documents/code/python/leetcode-python/files/calvin.txt"

if __name__ == "__main__":
    main()
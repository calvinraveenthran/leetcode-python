#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def avg(data):
    """Returns the average of the specified list"""
    total = 0
    for elt in data:
        total += elt
    return total/len(data)

def main():
	"""Launcher."""
	print(avg([1, -2, 3, 4]))

if __name__ == "__main__":
	main()
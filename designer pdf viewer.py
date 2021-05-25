import math
import os
import random
import re
import sys

h = list(map(int, input().rstrip().split()))
word = input()


def designer_pdf_viewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_heights = {}
    for i in range(len(h)):
        alphabet_heights[alphabet[i]] = h[i]
    max_height = max([alphabet_heights.get(letter) for letter in word])
    width = len(word)
    return width * max_height


print(designer_pdf_viewer(h, word))

import os
import sys
import csv
from frbb.Adafruit_Thermal import *



def text_format(text, length=30):
    strings = text.split()
    char_count = 0
    line = ""
    output = ""
    for counter, string in enumerate(strings):
        char_count += len(string)+1
        if char_count > length:
            char_count = len(string);
            output += line
            output += '\n'
            line = ""
            
        line += " " + string
        
        if counter == len(strings)-1:
            output += line
            output += '\n'
    
    return output

#printer = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=15)

poem="""Stamens are lovely; saps are of a daffodil hue. Drake is foolish. May I watch Showgirls with you?"""
#printer.println(text_format(poem))
print(text_format(poem))

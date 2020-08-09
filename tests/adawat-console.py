#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Arabic NLP console tools
most tools can be accessed on console
"""
import sys
import getopt
import os
import argparse
from io import open 
import pprint
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../')) # used for core
  
import pyarabic.araby
import adawat.adaat              
utf8repr = pyarabic.arabrepr.ArabicRepr() 
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
def grabargs():
    parser = argparse.ArgumentParser(description='Test Asmai analyzer.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=False,
    help="input file to convert", metavar="FILE")
    parser.add_argument("-t", dest="text", required=False,
    help="input text to convert", metavar="TEXT")
    parser.add_argument("-c", dest="command", nargs='?',default="", metavar="COMMAND",
        help="""Command to run : (view more by --doc) """,)    
    parser.add_argument("-o", dest="outfile", nargs='?', 
        help="Output file to convert", metavar="OUTFILE")
   
    parser.add_argument("--limit", type=int, nargs='?',default = 1000,
                        help="Limit line to treat", metavar="LIMIT")

    parser.add_argument("--progress", type=bool, nargs='?',default = False, const = True,
                        help="show progress bar", metavar="PROGRESS")
    parser.add_argument("--doc", type=bool, nargs='?',default = False, const = True,
                        help="Show help", metavar="DOC")
    args = parser.parse_args()
    return args
scriptversion = '0.1'
AuthorName = "Taha Zerrouki"


def test():
    
    args = grabargs()
    docme = args.doc
    action = args.command

    if docme or not action:
        print(adawat.adaat.help())
        sys.exit()
    text = args.text 
    filename = args.filename
    progress = args.progress

    limit    = args.limit
    progress = args.progress

    if not text and not filename:
        print("No argument given")
        sys.exit(0)
        
    if not text:
        try:
            myfile = open(filename, encoding="utf8")
        except:
            print(" Can't Open the given File ", filename)
            sys.exit()
    else:
        lines = text.split('\n')
    counter = 1
    if not limit : 
        limit = 100000000

    nolimit = False
    if not text:
        line = myfile.readline()
    else:
        if len(lines)>0:
            line = lines[0]
    while line and (nolimit or counter <= limit):
        if progress and not nolimit:
            sys.stderr.write("\r[%d%%]%d/%d lines" %(counter * 100/ limit, counter, limit))
            sys.stderr.flush()
        if not line.startswith('#'):
            result = adawat.adaat.DoAction(line, action)
            counter += 1
            print(utf8repr.repr(result))
        #get the next line
        if not text:
            line = (myfile.readline())
        else:
            if counter<len(lines):
                line = lines[counter]
            else:
                line = None
if __name__ == '__main__':
    test()

#!/usr/bin/env python3

"""
collate-trump.py

The CSVs from the Obama administration, i.e. for the years 2017-2018, are produced using ABBYY
FineReader, which converts PDF to XLSX and places them in data/raw/abbyy. The respective CSVs are
the result of using Excel 2016's conversion from xlsx to csv (Save As...).

The PDF->Excel conversion keeps many non-data elements, such as the page header/footers and graphics.
Some characters may also be irregular. Luckily, the data format and its 5 columns are the same
as they were for the Obama administration.

This script uses some simple logic to extract the data rows we care about from the ABBYY+Excel-created CSVs.

It reads filenames as arguments and outputs to stdout
"""


import csv
from os.sys import args, stddout
from pathlib import Path

def count_pages(rawtext):
    """
    Args:
        rawtext is a <str> consisting of the entire contents of a raw/messy CSV file
    Returns:
        <int> representing the expected number of pages

    Looks for the page number metainfo, which could look like:

            Page 1 of 12,,,
            Pagel of 12,,,,
            Page l of 12,,,,
    """



def parse_data_pages(rawtext):
    """
    Args:
        rawtext is a <str> consisting of the entire contents of a raw/messy CSV file
    Returns:
        <list> a list of strings, each string representing a "page" of data, as the text existed
          in PDF form. Headers and footers are stripped. Data headers are omitted

    This function throws an error if there's an anomaly in the raw text and expected page numbers
    """





def process_raw_text(filepath):
    fp = Path(filepath)
    text = fp.read_text()









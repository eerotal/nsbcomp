#!/bin/python

import re
import sys
import argparse
import symbols
import compiler

# Define the command line arguments.
ap = argparse.ArgumentParser('nsbcomp - A compiler for compiling TI '
				'NSpire Basic code from a more sane and '
				'portable syntax.');
ap.add_argument('--in', '-i', action='store', nargs=1, required=False,
		help='specify the input source file.');
ap.add_argument('--out', '-o', action='store', nargs=1, required=False,
		help='specify the compiled output file.');
ap.add_argument('--symbols', '-s', action='store_true',
		required=False,
		help='display a list of valid symbols and exit.');

# Parse the command line arguments and run the compiler.
args = ap.parse_args();
if (vars(args)['symbols'] == True):
	symbols.symbols_dump();
	sys.exit(0);
else:
	if (vars(args)['in'] != None and vars(args)['out'] != None):
		compiler.compile("test/in.nssrc", "out.nsmin");
	else:
		print("No input or output file specified. Exiting.");
		sys.exit(1);

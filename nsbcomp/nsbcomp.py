#!/bin/python

import re
import sys
import argparse
import symbols
import compiler
import preprocessor

# Define command line arguments.
ap = argparse.ArgumentParser('nsbcomp');
ap.add_argument('--in', '-i', action='store', nargs='?',
		help='specify the input source file.');
ap.add_argument('--out', '-o', action='store', nargs='?',
		help='specify the output file.');
ap.add_argument('--symbols', '-s', action='store_true',
		help='display a list of valid symbols and exit.');

# Parse the command line arguments and run the compiler.
args = ap.parse_args();
if (args.symbols == True):
	symbols.symbols_dump();
	sys.exit(0);
else:
	if (vars(args)['in']):
		defs = preprocessor.prep(vars(args)['in']);
		ret = compiler.compile(defs.tmp_path,
				vars(args)['out'], defs);
		defs.destroy();
		sys.exit(ret);
	else:
		print("No input file specified. Exiting.");
		sys.exit(1);

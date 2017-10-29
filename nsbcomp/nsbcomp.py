#!/bin/python

import re
import sys
import argparse
import compiler
import preprocessor

# Define command line arguments.
ap = argparse.ArgumentParser('nsbcomp');
ap.add_argument('--in', '-i', action='store', nargs='?',
		help='specify the input source file.');
ap.add_argument('--out', '-o', action='store', nargs='?',
		help='specify the output file.');

# Parse the command line arguments and run the compiler.
args = ap.parse_args();
if (vars(args)['in']):
	defs = preprocessor.PrepDefs();

	data = preprocessor.file_process(vars(args)['in'], defs);
	tmp = preprocessor.store_tmp_data(data);

	ret = compiler.compile(tmp, vars(args)['out'], defs);
	preprocessor.remove_tmp_data(tmp);
	sys.exit(ret);
else:
	print("No input file specified. Exiting.");
	sys.exit(1);

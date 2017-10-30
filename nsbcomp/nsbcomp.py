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
ap.add_argument('--preserve-tmp', '-p', action='store_true',
		help='preserve tmp files on exit. Debug flag.');
ap.add_argument('--dump-defines', '-d', action='store_true',
		help='dump the defined constants. Debug flag.');

# Parse the command line arguments and run the compiler.
args = ap.parse_args();
if (vars(args)['in']):
	defs = preprocessor.PrepDefs();

	try:
		data = preprocessor.file_process(vars(args)['in'], defs);
	except Exception as e:
		sys.exit(e.errno);

	tmp = preprocessor.store_tmp_data(data);

	ret = compiler.compile(tmp, vars(args)['out'], defs);

	if args.preserve_tmp == False:
		preprocessor.remove_tmp_data(tmp);
	if args.dump_defines == True:
		defs.dump();

	sys.exit(ret);
else:
	print("No input file specified. Exiting.");
	sys.exit(1);

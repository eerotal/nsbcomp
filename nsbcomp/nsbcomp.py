#!/bin/python

import re
import sys
import argparse
import compiler
import preprocessor
import config
import cli

# Load the configuration file.
config.conf_load();
config.conf_dump();

# Define command line arguments.
ap = argparse.ArgumentParser('nsbcomp');
ap.add_argument('--in', '-i', action='store', nargs='?',
		help='specify the input source file.');
ap.add_argument('--out', '-o', action='store', nargs='?',
		help='specify the output file.');
ap.add_argument('--verbose', '-v', action='store_true',
		help='print verbose messages to STDOUT.');
ap.add_argument('--preserve-tmp', '-p', action='store_true',
		help='preserve tmp files on exit. Debug flag.');
ap.add_argument('--dump-defines', '-d', action='store_true',
		help='dump the defined constants. Debug flag.');

# Parse the command line arguments and run the compiler.
args = ap.parse_args();

cli.verbose(args.verbose);

if (vars(args)['in']):
	if 'INCLUDE_PATHS' in config.config:
		preprocessor.set_include_paths(
			config.config['INCLUDE_PATHS']
		);

	defs = preprocessor.PrepDefs();
	try:
		data = preprocessor.file_process(vars(args)['in'], defs);
	except (IOError, OSError) as e:
		sys.exit(e.errno);

	tmp = None;
	try:
		tmp = preprocessor.store_tmp_data(data);
	except (IOError, OSError) as e:
		cli.printe(str(e));

		if args.preserve_tmp == False and tmp:
			preprocessor.remove_tmp_data(tmp);

		sys.exit(e.errno);

	ret = compiler.compile(tmp, vars(args)['out'], defs);

	if args.preserve_tmp == False:
		preprocessor.remove_tmp_data(tmp);
	if args.dump_defines == True:
		defs.dump();

	sys.exit(ret);
else:
	cli.printm("No input file specified. Exiting.");
	sys.exit(1);

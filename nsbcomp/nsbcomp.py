#!/bin/python

import re
import sys
import argparse
import compiler
import preprocessor
import config
import cli
import errno

def read_cli_args():
	cli.printv("Read CLI arguments.");

	# Define command line arguments.
	ap = argparse.ArgumentParser('nsbcomp');
	ap.add_argument('--input', '-i', action='store', nargs='+',
			help='specify the input source files. STDIN if omitted');
	ap.add_argument('--output', '-o', action='store', nargs='?',
			help='specify the output file. STDOUT if omitted.');
	ap.add_argument('--verbose', '-v', action='store_true',
			help='print verbose messages to STDOUT.');
	ap.add_argument('--preserve-tmp', '-p', action='store_true',
			help='preserve tmp files on exit. Debug flag.');

	# Parse and return the command line arguments.
	return ap.parse_args();

def config_setup():
	# Load the configuration file.
	try:
		config.conf_load();
	except IOError as e:
		if e.errno == errno.ENOENT:
			cli.printe('Failed to load config file: ' + str(e));
			return;

	config.conf_dump();

	if 'INCLUDE_PATHS' in config.config:
		preprocessor.set_include_paths(
			config.config['INCLUDE_PATHS']
		);
	if 'DIR_TMP' in config.config:
		preprocessor.set_tmp_dir(
			config.config['DIR_TMP'][0]
		);

def main():
	tmp_path = '';
	args = read_cli_args();
	cli.verbose(args.verbose);

	config_setup();

	cli.printv("Preprocessing input files.");
	try:
		tmp_path = preprocessor.multifile_process(args.input);
	except (IOError, OSError) as e:
		sys.exit(e.errno);

	cli.printv("Compiling tmp file: " + tmp_path);

	try:
		compiler.compile(tmp_path, args.output);
	except (IOError, OSError) as e:
		if args.preserve_tmp == False:
			preprocessor.remove_tmp_data(tmp_path);

		if e.errno == errno.ENOENT:
			cli.printe(str(e));
			sys.exit(e.errno);

	if args.preserve_tmp == False:
		preprocessor.remove_tmp_data(tmp_path);

if __name__ == '__main__':
	main();

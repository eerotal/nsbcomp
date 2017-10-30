#!/bin/python

import os
import re
import sys

def unicode_regex_repl(match):
	# Return the unicode character corresponding to
	# the match argument 1 from 'match'.
	return unichr(int(match.group(1), 16));

def ln_repl_by_list(ln, symbols, prefix):
	# Replace the symbols defined in 'symbols' with the
	# corresponding character(s).
	ret = ln;
	for s in symbols:
		ret = re.sub(prefix + s, symbols[s], ret);
	return ret;

def line_repl(ln, defs):
	ret = ln.decode('utf-8');

	# Whitespace replacement.
	ret = re.sub(r'\s*(\r\n|\n|\r)', ':', ln);
	ret = re.sub(r'^\s*', '', ret);
	ret = re.sub(r'\s+', ' ', ret);

	return ret.encode('utf-8');

def compile(input, output, defs):
	ln_min = "";
	lines = 0;

	# Open the output file. Errors are passed to the caller.
	if output:
		if not os.path.exists(os.path.dirname(output)):
			try:
				os.makedirs(os.path.dirname(output));
			except OSError as e:
				if e.errno != errno.EEXIST:
					raise;
		outfile = open(output, 'w');
	else:
		outfile = sys.stdout;

	# Open the input file. Errors are passed to the caller.
	try:
		with open(input, 'r') as infile:
			for ln in infile:
				ln_min = line_repl(ln, defs);
				outfile.write(ln_min);
				lines += 1;
	except IOError as e:
		if outfile != sys.stdout:
			outfile.close();
		raise;

	if outfile != sys.stdout:
		outfile.close();

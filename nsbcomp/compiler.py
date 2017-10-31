#!/bin/python

import os
import re
import sys
import errno

directives = {
	'_UNICODE': {
		'regex': r'_UNICODE\(0x([A-Fa-f0-9]{4})\)',
		'parser': lambda m:
			unichr(int(m.group(1), 16))
	}
}

def line_repl(ln, defs):
	ret = ln.decode('utf-8');

	# Whitespace replacement.
	ret = re.sub(r'\s*(\r\n|\n|\r)', ':', ln);
	ret = re.sub(r'^\s*', '', ret);
	ret = re.sub(r'\s+', ' ', ret);

	# Compiler directive replacement.
	for d in directives:
		ret = re.sub(directives[d]['regex'],
			directives[d]['parser'],
			ret);

	return ret.encode('utf-8');

def compile(input, output, defs):
	ln_min = "";
	lines = 0;

	# Open the output file. Errors are passed to the caller.
	if output:
		dir_out = os.path.dirname(output);
		if dir_out != '' and not os.path.exists(dir_out):
			try:
				os.makedirs(dir_out);
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

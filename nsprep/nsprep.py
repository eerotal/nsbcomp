#!/bin/python

import re
from symbols import *

def unicode_regex_repl(match):
	# Return the unicode character corresponding to
	# the match argument 1 from 'match'.
	return unichr(int(match.group(1), 16));

def line_repl(ln):
	ret = ln.decode('utf-8');

	# Whitespace replacement.
	ret = re.sub(r'(\r\n|\n|\r)\s*', ':', ln);
	ret = re.sub(r'^\s*', '', ret);

	# Logic symbol replacement.
	for s in symbols_logic:
		ret = re.sub(s, symbols_logic[s], ret);

	# Greek symbol replacement.
	for s in symbols_greek:
		if (re.search(sym_greek_prefix + s + 'u', ret)):
			# Replace uppercase symbol.
			ret = re.sub(sym_greek_prefix + s + 'u', symbols_greek[s][1], ret);
		else:
			# Replace lowercase symbol.
			ret = re.sub(sym_greek_prefix + s, symbols_greek[s][0], ret);

	# Assignment symbol replacement.
	for s in symbols_assignment:
		ret = re.sub(s, symbols_assignment[s], ret);

	# Misc symbol replacement.
	for s in symbols_misc:
		ret = re.sub(sym_misc_prefix + s, symbols_misc[s], ret);

	# Generic unicode symbol replacement.
	ret = re.sub(r'_u_\[([A-Fa-f0-9]{4})\]', unicode_regex_repl, ret);

	return ret.encode('utf-8');

def process(input, output):
	ln_min = "";
	lines = 0;
	print("Processing '" + input + "'.");
	with open(input, 'r') as infile:
		with open(output, 'w') as outfile:
			for ln in infile:
				ln_min = line_repl(ln);
				outfile.write(ln_min);
				lines += 1;
	print("Stats: ");
	print("  LOC=" + str(lines));

process("test/in.nssrc", "out.nsmin");

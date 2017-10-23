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

def compile(input, output):
	ln_min = "";
	lines = 0;

	try:
		outfile = open(output, 'w');
	except IOError as e:
		print(str(e));
		return e.errno;

	for inpath in input:
		try:
			with open(inpath, 'r') as infile:
				for ln in infile:
					ln_min = line_repl(ln);
					outfile.write(ln_min);
					lines += 1;
		except IOError as e:
			print(str(e));
			outfile.close();
			return e.errno;
	outfile.close();

	print("Done. LOC=" + str(lines));

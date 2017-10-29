#!/bin/python

import re
import sys
from symbols import *

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

def line_repl(ln):
	ret = ln.decode('utf-8');

	# Whitespace replacement.
	ret = re.sub(r'\s*(\r\n|\n|\r)\s*', ':', ln);
	ret = re.sub(r'^\s*', '', ret);

	# Logic symbol replacement.
	ret = ln_repl_by_list(ret, symbols_logic, '');

	# Misc symbol replacement.
	ret = ln_repl_by_list(ret, symbols_misc, '_s_');

	# Greek symbol replacement.
	for s in symbols_greek:
		if (re.search(sym_greek_prefix + s + 'u', ret)):
			# Replace uppercase symbol.
			ret = re.sub(sym_greek_prefix + s + 'u',
				symbols_greek[s][1], ret);
		else:
			# Replace lowercase symbol.
			ret = re.sub(sym_greek_prefix + s,
				symbols_greek[s][0], ret);


	# Generic unicode symbol replacement.
	ret = re.sub(r'_u_\[([A-Fa-f0-9]{4})\]', unicode_regex_repl, ret);

	return ret.encode('utf-8');

def compile(input, output):
	ln_min = "";
	lines = 0;

	try:
		if output:
			outfile = open(output, 'w');
		else:
			outfile = sys.stdout;
	except IOError as e:
		print(str(e));
		raise;

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
			raise;

	if outfile != sys.stdout:
		outfile.close();

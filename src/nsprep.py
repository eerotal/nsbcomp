#!/bin/python

import re

symbols_misc = {
	'->': u'\u2192'
}

symbols_logic = {
	'!=': u'\u2260',
	'==': u'\u003D',
	'<=': u'\u2264',
	'>=': u'\u2265'
}

sym_greek_prefix = '_g_';
symbols_greek = {
	'lpha': 	[u'\u03b1', u'\u0391'],
	'beta': 	[u'\u03b2', u'\u0392'],
	'gamma': 	[u'\u03b3', u'\u0393'],
	'delta': 	[u'\u03b4', u'\u0394'],
	'epsilon': 	[u'\u03b5', u'\u0395'],
	'zeta': 	[u'\u03b6', u'\u0396'],
	'eta': 		[u'\u03b7', u'\u0397'],
	'theta': 	[u'\u03b8', u'\u0398'],
	'iota': 	[u'\u03b9', u'\u0399'],
	'kappa': 	[u'\u03ba', u'\u039a'],
	'lambda': 	[u'\u03bb', u'\u039b'],
	'mu': 		[u'\u03bc', u'\u039c'],
	'nu': 		[u'\u03bd', u'\u039d'],
	'xi': 		[u'\u03be', u'\u039e'],
	'omicron': 	[u'\u03bf', u'\u039f'],
	'pi': 		[u'\u03c0', u'\u03a0'],
	'rho': 		[u'\u03c1', u'\u03a1'],
	'sigma': 	[u'\u03c3', u'\u03a3'],
	'tau': 		[u'\u03c4', u'\u03a4'],
	'upsilon': 	[u'\u03c5', u'\u03a5'],
	'phi': 		[u'\u03c6', u'\u03a6'],
	'chi': 		[u'\u03c7', u'\u03a7'],
	'psi': 		[u'\u03c8', u'\u03a8'],
	'omega': 	[u'\u03c9', u'\u03a9']
}

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

	# Misc symbol replacement.
	for s in symbols_misc:
		ret = re.sub(s, symbols_misc[s], ret);

	# Generic unicode symbol code replacement.
	ret = re.sub(r'_u_\[([A-Fa-f0-9]{4})\]', unicode_regex_repl, ret);

	return ret.encode('utf-8');

def process(input, output):
	print("Processing '" + input + "'.");
	ln_min = "";
	with open(input, 'r') as infile:
		with open(output, 'w') as outfile:
			for ln in infile:
				ln_min = line_repl(ln);
				outfile.write(ln_min);

process("test/in.nssrc", "out.nsmin");

#!/bin/python

import cli

symbols_assignment = {
	'->':		u'\u2192',
	'~=':		u'\u2248'
}

symbols_logic = {
	'!=':		u'\u2260',
	'==':		u'\u003D',
	'<=':		u'\u2264',
	'>=':		u'\u2265'
}

sym_misc_prefix = '_s_';
symbols_misc = {
	'inf': 		u'\u221e',
	'plusminus': 	u'\u00b1',
	'minusplus': 	u'\u2213',
	'cross': 	u'\u00d7',
	'sqrt': 	u'\u221a',
	'cubebrt':	u'\u221b',
	'fourthrt':	u'\u221c',
	'integral':	u'\u222b',
	'therefore':	u'\u2234',
	'because':	u'\u2235',
	'hdots':	u'\u2026',
	'vdots':	u'\u22ee',
	'drdots':	u'\u22f1',
	'urdots':	u'\u22f0',
	'box': 		u'\u220e'
}

sym_greek_prefix = '_g_';
symbols_greek = {         # LOWER      UPPER
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

def symbols_dump():
	# Dump a symbol table to STDOUT.

	for s in symbols_assignment:
		cli.print_table_ln([s + ' :',
			symbols_assignment[s].encode('utf-8')], 20);

	for s in symbols_logic:
		cli.print_table_ln([s + ' :',
			symbols_logic[s].encode('utf-8')], 20);

	for s in symbols_misc:
		cli.print_table_ln([sym_misc_prefix + s + ' :',
			symbols_misc[s].encode('utf-8')], 20);

	for s in symbols_greek:
		cli.print_table_ln([sym_greek_prefix + s + ' :',
			(symbols_greek[s][0] + ' / '
			+ symbols_greek[s][1]).encode('utf-8')], 20);

	cli.print_table_ln(["_u_[XXXX] :", "U+XXXX"], 20);

#!/bin/python

# This file contains a C-like preprocessor implementation for the
# nsbcomp compiler.

import os.path
import time
import re

DIR_TMP = "tmp";
DEFINE_KEYWORD = "#define";

class PrepDefs():
	scope = '';
	defs = {};
	tmp_path = '';

	def reset_defs(self):
		self.defs = {};

	def dump(self):
		# Dump a string represenation of this
		# PrepDefs object to STDOUT.
		print('PrepDefs:');
		print("\tScope:\n\t\t" + self.scope)
		print("\tDefs:");
		for id in self.defs:
			print("\t\t" + id + '=' + self.defs[id]);

	def destroy(self):
		# Free resources.
		if os.path.exists(self.tmp_path):
			try:
				os.remove(self.tmp_path);
			except OSError as e:
				print(str(e));
				raise;

def parse_def(ln):
	# Parse a definition line of the form
	# DEFINE_KEYWORD <identifier> <value>
	# Returns an array with the identifier as
	# the first item and the value as the
	# second one.

	tmp_ln = re.sub(r'(\r\n|\n|\r)$', '', ln);
	p = tmp_ln.split(' ');
	return [p[1], ' '.join(str(p[s]) for s in range(2, len(p)))];

def prep(in_path):
	# Preprocess the file 'in_path'.

	tmp_file = None;
	in_file = None;

	defs = PrepDefs();
	defs.scope = in_path;
	defs.tmp_path = os.path.join(DIR_TMP, str(round(time.time())));

	print("Creating tmp file: " + defs.tmp_path);
	if not os.path.exists(os.path.dirname(defs.tmp_path)):
		try:
			os.makedirs(os.path.dirname(defs.tmp_path));
		except OSError as e:
			if (e.errno != errno.EEXIST):
				raise;

	try:
		tmp_file = open(defs.tmp_path, 'w');
		in_file = open(in_path, 'r');
	except IOError as e:
		print(str(e));
		raise;

	for ln in in_file:
		if (ln.startswith(DEFINE_KEYWORD)):
			ret = parse_def(ln);
			defs.defs[ret[0]] = ret[1];
		else:
			tmp_file.write(ln);

	in_file.close();
	tmp_file.close();
	return defs;

#!/bin/python

# This file contains a C-like preprocessor implementation for the
# nsbcomp compiler.

import os.path
import time
import re
import strutils

DIR_TMP = "tmp";
KEYWORD_DEFINE = "#define";
KEYWORD_INCLUDE = "#include";

class PrepDefs():
	root = None;
	defs = {};

	def reset_defs(self):
		self.defs = {};

	def dump(self):
		# Dump a string represenation of this
		# PrepDefs object to STDOUT.
		print('PrepDefs:');
		print("\tRoot:\n\t\t" + self.root)
		print("\tDefs:");
		for id in self.defs:
			print("\t\t" + id + '=' + self.defs[id]);

def ln_parse(ln, defs):
	# Attempt to parse a line in case it contains
	# a preprocessor statement. Returns the string to
	# be written into the output file or an empty
	# string if no string needs to be written.

	ret = None;
	if ln.startswith(KEYWORD_DEFINE):
		ret = ln_define_parse(ln, defs);
		return '';
	elif ln.startswith(KEYWORD_INCLUDE):
		return ln_include_parse(ln, defs);
	else:
		return strutils.repl_list(ln, defs.defs);

def ln_define_parse(ln, defs):
	# Parse a preprocessor define statement.
	tmp_ln = re.sub(r'\s*(\r\n|\n|\r)', '', ln);
	tmp_ln = re.sub(r'\s+', ' ', tmp_ln);
	p = tmp_ln.split(' ');
	defs.defs[p[1]] = ' '.join(str(p[s]) for s in range(2, len(p)));

def ln_include_parse(ln, defs):
	# Parse a preprocessor include statement.
	tmp_ln = re.sub(r'(\r\n|\n|\r)$', '', ln);
	p = tmp_ln.split(' ');

	if os.path.exists(p[1]) and defs.root != p[1]:
		return file_process(p[1], defs)
	else:
		return '';

def file_process(in_path, defs):
	# Process the file 'in_path' using the preprocessor.
	buffer = '';
	in_file = None;

	if defs.root == None:
		defs.root = in_path;

	try:
		in_file = open(in_path, 'r');
	except IOError as e:
		print(str(e));
		raise;

	for ln in in_file:
		ret = ln_parse(ln, defs);
		if not ret == '':
			buffer += ret;

	in_file.close();
	return buffer;

def store_tmp_data(data):
	# Store the string 'data' into a tmp file.
	tmp_path = os.path.join(DIR_TMP, str(round(time.time())));

	if not os.path.exists(os.path.dirname(tmp_path)):
		try:
			os.makedirs(os.pathdirname(tmp_path));
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise;

	with open(tmp_path, 'w') as tmpf:
		tmpf.write(data);

	return tmp_path;

def remove_tmp_data(path):
	# Remove a tmp file at 'path'.
	if os.path.exists(path):
		try:
			os.remove(path);
		except OSError as e:
			print(str(e));
			raise;

#!/bin/python

# This file contains a C-like preprocessor implementation for the
# nsbcomp compiler.

import os.path
import time
import re
import strutils

def init():
	global DIR_TMP, PRE_KEYWORDS;
	DIR_TMP = 'tmp';
	PRE_KEYWORDS = {
		'define': ['#define', _ln_define_parse],
		'include': ['#include', _ln_include_parse]
	};

class PrepDefs():
	root = None;
	included = [];
	defs = {};

	def set_included(self, name):
		self.included.append(name);

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

def _ln_parse(ln, defs):
	# Parse a line using the preprocessor system. Returns
	# the string to be written into the output file or an empty
	# string if no string needs to be written.

	ret = None;
	for k in PRE_KEYWORDS:
		if ln.startswith(PRE_KEYWORDS[k][0]):
			return PRE_KEYWORDS[k][1](ln, defs);
	else:
		return strutils.repl_list(ln, defs.defs);

def _ln_define_parse(ln, defs):
	# Parse a preprocessor define statement.
	tmp_ln = re.sub(r'\s*(\r\n|\n|\r)', '', ln);
	tmp_ln = re.sub(r'\s+', ' ', tmp_ln);
	p = tmp_ln.split(' ');
	defs.defs[p[1]] = ' '.join(str(p[s]) for s in range(2, len(p)));
	return '';

def _ln_include_parse(ln, defs):
	# Parse a preprocessor include statement.
	tmp_ln = re.sub(r'(\r\n|\n|\r)$', '', ln);
	p = tmp_ln.split(' ');

	if os.path.exists(p[1]):
		if not p[1] in defs.included:
			print('[Info] Including \'' + p[1] + '\'.');
			defs.set_included(p[1]);
			return file_process(p[1], defs);
		else:
			print('[Warning] Prevented circular or ' +
				'redundant include while attempting ' +
				'to include \'' + p[1] + '\'.');
			return '';

def file_process(in_path, defs):
	# Process the file 'in_path' using the preprocessor.
	buffer = '';
	in_file = None;

	if defs.root == None:
		defs.root = in_path;
		defs.set_included(defs.root);

	try:
		in_file = open(in_path, 'r');
	except IOError as e:
		print(str(e));
		raise;

	for ln in in_file:
		ret = _ln_parse(ln, defs);
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

init();

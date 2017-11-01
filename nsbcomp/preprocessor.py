#!/bin/python

# This file contains a C-like preprocessor implementation for the
# nsbcomp compiler.

import os
import errno
import os.path
import time
import re
import strutils
import cli

DIR_TMP_FALLBACK = 'tmp';

def init():
	global DIR_TMP, PRE_KEYWORDS, INCLUDE_PATHS;

	DIR_TMP = DIR_TMP_FALLBACK;
	PRE_KEYWORDS = {
		'define': ['#define', _ln_define_parse],
		'include': ['#include', _ln_include_parse]
	};
	INCLUDE_PATHS = [
		os.getcwd()
	];

def set_tmp_dir(dir):
	global DIR_TMP;
	if dir:
		DIR_TMP = dir;

def set_include_paths(paths):
	global INCLUDE_PATHS;
	if paths:
		INCLUDE_PATHS += paths;

class PrepDefs(object):
	root = None;
	included = [];
	defs = {};

	def set_included(self, name):
		self.included.append(name);

	def reset(self):
		self.root = None;
		self.included = [];
		self.defs = {};

	def dump(self):
		# Dump a string represenation of this
		# PrepDefs object to STDOUT.
		cli.printv('PrepDefs:');
		cli.printv("\tRoot:");
		if self.root:
			cli.printv("\t\t" + self.root);
		cli.printv("\tDefs:");
		for id in self.defs:
			cli.printv("\t\t" + id + '=' + self.defs[id]);

def _ln_parse(ln, defs):
	# Parse a line using the preprocessor system. Returns
	# the string to be written into the output file or an empty
	# string if no string needs to be written.

	global PRE_KEYWORDS;
	ret = None;
	for k in PRE_KEYWORDS:
		if ln.startswith(PRE_KEYWORDS[k][0]):
			# Run parser function. Possible
			# errors are passed on.
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

def _get_include_abs_path(p):
	# Get the absolute include path of 'p' by
	# joining 'p' to the paths in the INCLUDE_PATHS
	# array and returning the first path that exists.
	# 'p' itself is returned in case it already is an
	# absolute path. 'None' is returned if no generated
	# path exists.

	global INCLUDE_PATHS;
	fullpath = '';
	if p.startswith('/'):
		if os.path.isfile(p):
			return p;
		else:
			return None;

	for ipath in INCLUDE_PATHS:
		fullpath = os.path.join(ipath, p);
		if os.path.isfile(fullpath):
			return fullpath;
	return None;

def _ln_include_parse(ln, defs):
	# Parse a preprocessor include statement.
	tmp_ln = re.sub(r'(\r\n|\n|\r)$', '', ln);
	p = tmp_ln.split(' ');

	fpath = _get_include_abs_path(p[1]);

	if fpath != None:
		if not fpath in defs.included:
			cli.printv('Including \'' + fpath + '\'.');
			defs.set_included(fpath);
			return file_process(fpath, defs);
		else:
			cli.printw('Prevented circular or ' +
				'redundant include while attempting ' +
				'to include \'' + fpath + '\'.');
			return '';
	else:
		# File not found, raise IOError.
		cli.printe('File ' + p[1] + ' not found!');
		raise IOError(errno.ENOENT,
			os.strerror(errno.ENOENT), p[1]);

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
		cli.printe(str(e));
		raise;

	for ln in in_file:
		# Parse a line from the input file.
		# In case an error occurs, cleanup
		# routines are called and the error
		# is re-raised afterwards.
		try:
			ret = _ln_parse(ln, defs);
		except:
			in_file.close();
			raise;

		if not ret == '':
			buffer += ret;

	in_file.close();
	return buffer;

def multifile_process(in_paths):
	# Process the files in the array 'in_paths' using
	# the preprocessor. A file path to a tmp file containing
	# the processed data is returned.

	tmp_path = make_tmp_path();
	data = '';
	defs = PrepDefs();

	for i in in_paths:
		cli.printv("Preprocessing: " + i);
		defs.reset();
		data = file_process(i, defs);
		write_tmp_data(data, tmp_path, append=True);

	return tmp_path;

def make_tmp_path():
	global DIR_TMP;
	return os.path.join(DIR_TMP, str(round(time.time())));

def write_tmp_data(data, path, append=False):
	# Store the string 'data' into a tmp file.

	if not os.path.exists(os.path.dirname(path)):
		try:
			os.makedirs(os.path.dirname(path));
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise;

	with open(path, 'a' if append else 'w') as tmpf:
		if append:
			tmpf.seek(0, 2);
		tmpf.write(data);

def remove_tmp_data(path):
	# Remove a tmp file at 'path'.
	if os.path.exists(path):
		try:
			os.remove(path);
		except OSError as e:
			cli.printe(str(e));
			raise;

init();

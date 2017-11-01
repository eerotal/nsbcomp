#!/bin/python

flag_verbose = False;

def printm(str):
	# Print a message to STDOUT.
	print('[Info]: ' + str);

def printw(str):
	# Print a warning message to STDOUT.
	print('[Warning]: ' + str);

def printe(str):
	# Print an error message to STDOUT.
	print('[Error]: ' + str);

def printv(str):
	# Print a verbose message to STDOUT.
	global flag_verbose;
	if flag_verbose:
		print('[Verbose]: ' + str);

def verbose(flag):
	# Enable/Disable verbose printing.
	global flag_verbose;
	flag_verbose = flag;

def print_table_ln(items, offset):
	# Print an evenly spaced line of a table.
	# The table column elements are stored in 'items'
	# and there's 'offset' number of characters between
	# the start of each item. If the length of an item
	# is greater than offset, the line is not printed.

	outstr = '';
	for i in range(len(items)):
		if (len(items[i]) > offset):
			return;

		outstr += items[i];
		outstr += ' '*(offset - len(items[i]));
	print(outstr);

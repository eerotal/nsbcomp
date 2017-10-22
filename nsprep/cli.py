#!/bin/python

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
	print outstr;

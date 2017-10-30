#!/bin/python

import re
import cli

CONFIG_FILE = 'nsbcomp.conf';
config = {}

def conf_dump():
	cli.printv("Configuration:");
	for k in config:
		cli.printv('\t' + k + ': ' + str(config[k]));

def _conf_parse_ln(ln):
	tmp_ln = re.sub(r'(\r\n|\n|\r)', '', ln);
	tmp_ln = re.sub(r'\s*', '', tmp_ln);
	parts = tmp_ln.split('=');
	config[parts[0]] = parts[1].split(',');

def conf_load():
	cli.printv('Loading config from \'' + CONFIG_FILE + '\'.');

	try:
		with open(CONFIG_FILE, 'r') as conf:
			for ln in conf:
				_conf_parse_ln(ln);
	except IOError as e:
		cli.printe(str(e));
		raise;
	return config;

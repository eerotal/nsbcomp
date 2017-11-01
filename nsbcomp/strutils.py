#!/bin/python

import re

def repl_list(string, repl):
        # Replace all occurences of repl's keys in 'string'
        # with the corresponding value in 'repl'.
        ret = string;
        for s in repl:
                ret = re.sub(s, repl[s], ret);
        return ret;

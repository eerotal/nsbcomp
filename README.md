# nsbcomp - A compiler for compiling TI NSpire Basic code from a more portable syntax.

This Python program is an attempt at creating a more portable
syntax for writing programs for the TI NSpire CX CAS
calculator. The reason I made this simple compiler is that the
original NSpire Basic syntax is not too great, since it uses
mathematical symbols not included in the standard ASCII character
set. There's also a problem with the default NSpire Basic editor:
There's no way to paste human readable code that's not originally
copied from the default editor without breaking the code and messing
up the indentation in the process.  

This compiler tries to solve these problems by:
 1. Defining a set of symbol shortcuts, such as _s_alpha for the
    greek letter alpha, that are replaced in the compiled output.
 2. Generating the output file in a format that, while virtually
    unreadable, can be pasted straight into the TI NSpire program
    editor. Note that the pasted version doesn't include any kind
    of indentation, but since the source files for this compiler can
    include indentation, the code can just be edited using a normal
    text editor or IDE.  

## Command Line Arguments

|     Option     |                            Explanation                            |
| :------------- | :---------------------------------------------------------------  |
|   --in/-i      | Input file(s). Multiple files produce a concatenated output file. |
|   --out/-o     | Output file. STDOUT is used if this is omitted.                   | 
|   --symbols/-s | Display a list of valid symbol codes.                             |
|   --help/-h    | Display a help message.                                           |  

## Usage examples

`python nsbcomp/nsbcomp.py -i examples/example.nssrc`
* This command compiles the file `examples/example.nssrc` and outputs
  the result to STDOUT.  

`python nsbcomp/nsbcomp.py -i examples/example.nssrc -o out.nsmin`
* This command compiles the file `examples/example.nssrc` and outputs
  the result to the file `out.nsmin`.  

## License information

This program is licensed under the BSD 3-clause license. You can find
the whole license text in the file LICENSE.txt.  

Copyright 2017 Eero Talus

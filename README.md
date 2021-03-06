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
    These symbol shortcuts can be used by including definition files
    using the preprocessor system provided by this compiler.
 2. Generating the output file in a format that, while virtually
    unreadable, can be pasted straight into the TI NSpire program
    editor. Note that the pasted version doesn't include any kind
    of indentation, but since the source files for this compiler can
    include indentation, the code can just be edited using a normal
    text editor or IDE.  

## Installing

The installation (or configuration) procedure is quite simple. The
steps to take are listed below.  

1. Install git, Python 2 and GNU Make. On Debian Stretch these can be
   installed by running the command `sudo apt update && sudo apt install git python2.7 make`.
1. Download the nsbcomp sources with git by running
   `git clone https://github.com/eerotal/nsbcomp.git` in your home directory
   or in a directory where you want the sources to be placed. This command
   will create a subdirectory called `nsbcomp.git` where it downloads the
   sources.
2. Run `cd nsbcomp.git` to switch into the downloaded source directory and
   run `make configure`.
3. `nsbcomp` is now ready to be used. There are some usage examples in the
   section `Usage examples` in this file.

## Command Line Arguments

|     Option        |                                   Explanation                                     |
| :---------------- | :-------------------------------------------------------------------------------- |
| --in/-i           | Input file(s). STDIN is used if this is omitted. Multiple files are concatenated. |
| --out/-o          | Output file. STDOUT is used if this is omitted.                                   |
| --verbose/-v      | Print verbose messages to STDOUT.                                                 |
| --preserve-tmp/-p | Preserve created temporary files on exit. Debug flag.                             |
| --help/-h         | Display a help message.                                                           |

## Usage examples

`python nsbcomp/nsbcomp.py -i examples/example.nssrc`
* This command compiles the file `examples/example.nssrc` and outputs
  the result to STDOUT.  

`python nsbcomp/nsbcomp.py -i examples/* -o out.nsmin`
* This command compiles all of the files in the `examples` directory
  and outputs the concatenated result to the file `out.nsmin`.  

## License information

This program is licensed under the BSD 3-clause license. You can find
the whole license text in the file LICENSE.txt.  

Copyright 2017 Eero Talus

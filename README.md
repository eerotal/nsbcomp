# nsbcomp - A compiler for compiling TI NSpire Basic code from a more sane and portable syntax.

This Python program is an attempt at creating a more sane and
portable syntax for writing programs for the TI NSpire CX CAS
calculator. The rationale behind this compiler is that the
original NSpire Basic editor is absolutely horrible and the
language syntax is not great either, since it uses mathematical
symbols not included in the standard ASCII character set. Another
problem with the editor is that there's no way to properly paste
(human readable!) code into it if the code isn't originally copied
from the editor itself, and even then all the indentations are
wrong in the pasted version.

This compiler tries to solve these problems by:
 1. Defining a set of symbol shortcuts, such as _s_alpha for the
    greek letter alpha, that are replaced in the compiled output.
 2. Generating the output file in a format that, while virtually
    unreadable, can be pasted straight into the TI NSpire program
    editor. Note that the pasted version doesn't include any kind
    of indentation, but since the source file for this compiler can
    include indentation, the code can just be edited using a normal
    (actually usable) text editor or IDE.

TL;DR: The TI NSpire program editor is awful. This is an attempt at
creating an easy way of writing NSpire Basic programs.

This program is licensed under the BSD 3-clause license. You can find
the whole license text in the file LICENSE.txt.

Copyright 2017 Eero Talus

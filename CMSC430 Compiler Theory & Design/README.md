# CMSC430 Compiler Theory and Design # 

This Compiler Theory and Design project in 2024, led to the creation of a compiler in C. Dependencies included flex and bison. This project is Linux exclusive, but can be emulated on Windows with different dependencies. I created my own grammar that compiles its own programming language. The language handles standard programming math operators and various logic pieces including ternaries, quaternaries, and other boolean operations (and/or/not). See test code folder for program examples in the new language. Values.cc shows how the logic is evaluated. Scanner.l shows all supported keywords. Parser.y shows the semantics of the grammar in Backus–Naur form.  

Use make to set up the compiler
.compile / [path to test file] 
---
title: Efficient Workflow in Linux
...



(Comprehensive) Intro to Vim
----------------------------

See [the guide](../../vim/index.md) to Vim. Keep the cheatsheet up and work
through Exercise 1.

Compiling in Vim
----------------

- LaTeX
- C / makefiles

LaTeX tips, tricks, and templates
---------------------------------

LaTeX is widely used, and accordingly has extensive documentation for nearly
every need. In general, (as with most things) the fastest way to learn how to
use LaTeX is google: en.wikibooks.org/wiki/LaTeX/ is an excellent resource for
basic issues, and StackExchange typically has solutions to any more advanced or
specific questions.

### LaTeX report template with BibTeX

A skeleton report file is in `bibtex_file.tex`, which uses the BibTex file
`bibtex_file.bib`. Each of these files are comprised of text, and are compiled
with LaTeX. The commands necessary to compile this article are in
`compile_article`; you can either run this bash script (chmod u+x
compile_article; ./compile_article) or you can type out each command in the bash
script.

### Beamer template

Beamer is an open-source presentation software, which allows for LaTeX to be
used as a presentation tool. An example presentation is `beamer_template.tex`,
which can be compiled by executing `compile_beamer` in the same manner as above. 

The magic of markdown and pandoc
--------------------------------

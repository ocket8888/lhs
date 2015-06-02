---
title: Integrating Latex with Vim
...


Vim LaTeX Macros
================

Auto-compile
------------

We want to be able to compile LaTeX documents without leaving Vim, so we'll
record a [Vim macro](vim.wikia.com/wiki/Macros) which does this compilation for
us. I like to use the macro `@w`, because to me this is like a 'deep' write -
not only am I writing the document, I'm compiling it to produce the output.

Place these lines in your '.vimrc':

```vim
autocmd BufRead,BufNewFile *.tex
    \ let @w=':wa:!pdflatex %:r; bibtex %:r; pdflatex %:r; pdflatex %:r'
```

Here, we're telling Vim to run the command in quotes (`:wa...r`) every time we
press the key `@` then `w` (not together). The command calls `pdflatex`, then
`bibtex`, then `pdflatex` twice again - which is how `pdflatex` must be called
to build a document. The `autocmd BufRead,BufNewFile *.tex` tells Vim to use
this definition for `@w` whenever a `tex` file is opened.

Notice the `` in the command string - that is not just a `Shift+6+M`, it's
actually a special character which means `newline` - get that character by
pressing `Ctrl+v` in insert mode, then pressing `Enter`. You can get similar
special characters which mean `Escape` or other special keys using the same
process.

This command will literally be fed into Vim character-by-character. When you
press `@w`, first a `:` will be passed to Vim, putting it in command mode, then
a `wa` will be fed to it, typing the command `wa` for you. When it reaches the
``, the `Enter` key is fed to Vim, running that command for you. So we are
writing out all open files with the first `:wa`.

The second bit of the command opens up command mode again, `:`, then uses the
`!` to tell Vim that the rest of the command is a shell command, not a Vim
command. The `%:r` will be replaced with the filename minus the exstension
('report.tex' -> 'report').

If you have some other command or script which compiles LaTeX for you, put that
in quotes after the exclamation point instead. For example, if you have a script
`build_tex` which compiles LaTeX how you like, put `:wa:!build_tex %:r`.

Open PDF file
-------------

Opening the resulting PDF is similar to compiling to PDF, we need some macro
which does it for us. I use `@o`.

```vim
autocmd BufRead,BufNewFile *.tex
    \ let @w=':wa:!pdflatex %:r; bibtex %:r; pdflatex %:r; pdflatex %:r'
    \ | let @o=':!mupdf %:r.pdf &>/dev/null &'
```

Here, we've simply added another macro for Vim to use when we open `.tex` files.
This macro calls the command `mupdf %:r.pdf &>/dev/null &`. `mupdf` is a pdf
viewer (you may have `okular` or `evince` - check by running those commands in
your terminal). The `&>/dev/null` tells the shell to throw away output (any
minor errors that `mupdf` has, etc), and the final `&` tells `mupdf` to run in
the background, so that Vim will stay open and visible.

Print a PDF
-----------

Once again, we'll create a macro which prints pdfs for us. We'll use `@p` for
this one, perhaps unsurprisingly.

```vim
 autocmd BufRead,BufNewFile *.tex
    \ let @w=':wa:!pdflatex %:r; bibtex %:r; pdflatex %:r; pdflatex %:r'
    \ | let @o=':!mupdf %:r.pdf &>/dev/null &'
    \ | let @p=':wa:!print_file_command %:r.pdf'
```

Here, it's assumed you have a `print_file_command` which can take a pdf file and
print it. If not, you can check out the [shell](../shell) directory for one.

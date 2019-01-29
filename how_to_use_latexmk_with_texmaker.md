How to set up latexmk with Texmaker and Miktex under Windows:

1. Download and install perl ActivePerl
2. Install latexmk via Miktex
3. Use different latexmk command in the texmaker configuration:
	Instead of
	latexmk -e "$pdflatex=q/pdflatex -synctex=1 -interaction=nonstopmode/" -pdf %.tex
	use
	latexmk -e "$pdflatex=q/pdflatex -synctex=1 -interaction=nonstopmode/"
4. Click on "Latexmk" to build it.

It will build the files successfully but display errors like the errors you get if you compile the non-master file using the normal way.
I don't know how to fix this, but you can just ignore the errors.
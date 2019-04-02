$pdf_mode = 1;
@default_files = ('STOCHP.tex');
$out_dir = '../bin';
$pdflatex = "pdflatex -synctex=1 -halt-on-error %O %S"

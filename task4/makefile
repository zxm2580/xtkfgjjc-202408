paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@

.PHONY: clean
clean:
	mkdir -p Untrack
	rm -f *~ .*~
	git ls-files -o | grep -v Untrack | xargs -r mv -u -t Untrack

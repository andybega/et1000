
.PHONY: docs/index.html docs/simple.css

docs/index.html: template/index.html
	Rscript make-index.R

docs/simple.css: template/simple.css
	cp template/simple.css docs/



.PHONY: docs/index.html docs/simple.css

docs/index.html: template/index.html
	Rscript make-index.R

docs/simple.css: template/simple.css
	cp template/simple.css docs/

docs/about.html: template/about.html
	cp template/about.html docs/

docs/pos.html: template/pos.html
	cp template/pos.html docs/

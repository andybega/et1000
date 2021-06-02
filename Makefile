
.PHONY: docs/index.html docs/simple.css

docs/index.html: src/index.html
	Rscript make-index.R

docs/simple.css: src/simple.css
	cp src/simple.css docs/

docs/about.html: src/about.html
	cp src/about.html docs/

docs/pos.html: src/pos.html
	cp src/pos.html docs/

docs/favicon.ico: src/favicon.png
	convert -resize x16 -gravity center -crop 16x16+0+0 src/favicon.png -flatten -colors 256 -background transparent docs/favicon.ico

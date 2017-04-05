Make presentation with `markdown`+`pandoc`+`revealjs`.

``` vi
git clone https://github.com/hakimel/reveal.js.git

pandoc -t revealjs -s slides.md -o slides.html -V theme:sky
```

Open `slides.html` in chrome and append `?print-pdf` on the end and reload, then print.
See [reveal.js#pdf-export](https://github.com/hakimel/reveal.js#pdf-export) for more info.

See [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) for how to list different images with specified size.(Attention, we don't involve the `pandoc-crossref` in the command above, just check the grammar, `pandoc` ships with some support listed in `pandoc-crossref`.)

Enjoy!
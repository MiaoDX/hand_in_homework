It surprised myself a lot when realized there is no repository for my homework, so here it is.

Some hand in materials will saved here for quick access and unified management.


## Markdown to HTML slides

### convert

``` vi
# proposal.md is the markdown file we want to convert
pandoc -f markdown -t revealjs --standalone --self-contained proposal.md -o proposal.html -V theme=serif2 -V revealjs-url=H:/class_material/hand_in_homework/pandoc_markdown_revealjs/reveal.js -i
```

`--standalone` generate a standalone HTML file, `--self-contained` make all things in it, we use a modified `serif` theme (i.e. `serif2`), `-i` means to display lists incrementally (one item at a time).

### save as pdf

[As the reveal.js' instruction](https://github.com/hakimel/reveal.js#instructions-1), append `?print-pdf` at the end of the url and use **CHROME** to `print` it as a pdf file.

## Remove `\tightlist`

``` vi
\newcommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```


## Figure reference

According to [pandoc-crossref
](https://github.com/lierdakil/pandoc-crossref), to make a label for image and set width at the same time, just type:

``` vi
![caption a](coolfiga.png){#fig:cfa width=30%}
```

NOTE that without `pandoc-crossref`, the markdown file convert to html or tex nicely, it seems that `pandoc` itself already has **some** support to references, but not so much compared with `pandoc-crossref`. (In fact, I failed to covert to html or tex with `pandoc-crossref`, not so sure why this happened).
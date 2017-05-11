It surprised myself a lot when realized there is no repository for homework, so here it is.

Some hand in materials will saved here for quick access and unified management.


## remove `\tightlist`

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

NOTE that without `pandoc-crossref`, the markdown file convert to html or tex nicely, it seems that `pandoc` itself already has some support to references, but not so much compared with `pandoc-crossref`. (In fact, I failed to covert to html or tex successfully with `pandoc-crossref`, not so sure why this happen).
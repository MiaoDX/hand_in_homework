It surprised myself a lot when realized there is no repository for homework, so here it is.

Some hand in materials will saved here for quick access and unified management.


## remove `\tightlist`

``` vi
\newcommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```


## Figure reference

At present, according to [How do I make a reference to a figure in markdown using pandoc?](http://stackoverflow.com/questions/9434536/how-do-i-make-a-reference-to-a-figure-in-markdown-using-pandoc)

``` vi
![This is the caption\label{mylabel}](/url/of/image.png)
See figure \ref{mylabel}.
```

However, will port to [pandoc-crossref
](https://github.com/lierdakil/pandoc-crossref) for more constant usage.
# Yaml2ProbaTree

Converts a yaml data such as : 
*(see test/input_tree.yaml)*
```yaml
root:
  $A_1$:
    _v: 85/100
    $A_2$:
      _v: 85/100
    $\bar{A_2}$:
      _v: 15/100
  $\bar{A_1}$:
    _v: 15/100
    $A_2$:
      _v: 1/10
    $\bar{A_2}$:
      _v: 9/10
```

Into a legit tikz tree : 
*(needs the tikz tree library, please add \usetikzlibrary{trees} to your preambule)*
```latex
% Set the overall layout of the tree
\tikzstyle{level 1}=[level distance=3.5cm, sibling distance=3.5cm]
\tikzstyle{level 2}=[level distance=3.5cm, sibling distance=2cm]
% Define styles for mytree and leafs
\tikzstyle{mytree} = [text width=4em, text centered]
\tikzstyle{end} = [circle, minimum width=3pt,fill, inner sep=0pt]

\begin{tikzpicture}[grow=right, sloped]
\node[mytree] {}
        child {
                node[mytree] {$\bar{A_1}$}
                child {
                        node[end, label=right:
                                {$\bar{A_2}$}] {}

                        edge from parent
                        node[above]  {$\frac{9}{10}$}
                }
                child {
                        node[end, label=right:
                                {$A_2$}] {}

                        edge from parent
                        node[above]  {$\frac{1}{10}$}
                }
                edge from parent
                node[above]  {$\frac{15}{100}$}
        }
        child {
                node[mytree] {$A_1$}
                child {
                        node[end, label=right:
                                {$\bar{A_2}$}] {}

                        edge from parent
                        node[above]  {$\frac{15}{100}$}
                }
                child {
                        node[end, label=right:
                                {$A_2$}] {}

                        edge from parent
                        node[above]  {$\frac{85}{100}$}
                }
                edge from parent
                node[above]  {$\frac{85}{100}$}
        };
\end{tikzpicture}
```

License
----
Yaml2ProbaTree is delivered as it is under the well known MIT License


**References that helped**
 - [probability tree example] : <https://texample.net/tikz/examples/probability-tree>

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)



   [probability tree example]: <https://texample.net/tikz/examples/probability-tree>


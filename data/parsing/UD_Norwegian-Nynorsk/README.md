# Summary

The Norwegian UD treebank is based on the Nynorsk section of the Norwegian
Dependency Treebank (NDT), which is a syntactic treebank of Norwegian. 
NDT has been automatically converted to the UD
scheme by Lilja Øvrelid at the University of Oslo.

# Introduction

NDT was developed 2011-2014 at the National Library of Norway in collaboration
with the Text Laboratory and the Department of Informatics at the
University of Oslo.
NDT contains around 300,000 tokens taken from a variety of genres.
The treebank texts have been manually annotated for morphosyntactic
information. The morphological annotation mainly follows
the [Oslo-Bergen Tagger](http://tekstlab.uio.no/obt-ny/).  The syntactic
annotation follows, to a large extent, the Norwegian Reference
Grammar, as well as a dependency annotation scheme formulated at the
outset of the annotation project and iteratively refined throughout
the construction of the treebank. For more information, see the
references below.

### DATA SPLITS

In creating the data splits, care has been taken to preserve
contiguous texts in the different splits and also to keep a fair
balance of genres in each of the splits. Petter Hohle created the
splits for the Norwegian UD treebank. The splits were created by
concatenating the following files (available with the distribution of
NDT):

Train:

blogg-nn001_0000 -- blogg-nn003_0001
dot001_0000 -- dot014_0007
firda-nn001_0000 -- firda-nn004_0005
kk-nn001_0000 -- kk-nn006_0002
mom001_0000 -- mom003_0004
st-nn001_0000 -- st-nn002_0000
vtb-nn001_0000 -- vtb-nn006_0004

Dev:

blogg-nn003_0002
dot014_0008 -- dot015_0002
firda-nn004_0006 -- firda-nn005_0002
kk-nn006_0003 -- kk-nn007_0002
mom003_0005
st-nn002_0001
vtb-nn006_0005 -- vtb-nn007_0001

Test:

blogg-nn003_0003
dot015_0003 -- dot016_0004
firda-nn005_0003 -- firda-nn005_0006
kk-nn007_0003 -- kk-nn007_0006
mom003_0006
st-nn002_0002
vtb-nn007_0002 -- vtb-nn007_0004

### BASIC STATISTICS


### TOKENIZATION
White space always indicates a token boundary and punctuation constitute separate tokens, except:

* numbers with periods, commas or colons, e.g. *1.3*, *0,6*, *10:13*
* abbreviations, e.g. *f.eks.*, *Carl J. Hambro*
* URLs, e.g. *http://www.ifi.uio.no*

The treebank does not contain multiword tokens.

### MORPHOLOGY
The PoS-tags follow the universal tag set and does not add any
language-specific PoS-tags. The morphological features follow the
Oslo-Bergen Tagger scheme (Hagen et. al., 2000). PoS-tags and
morphological features were converted automatically to the UD scheme.

### SYNTAX
The syntactic annotation in the Norwegian UD treebank conforms to the
UD guidelines, adding a language-specific relation for relative clauses (`acl:relcl`).
The annotation has been automatically converted to
UD from the original dependency scheme described in Solberg
et. al. (2014) and further described in the NDT guidelines (Kinn
et. al.).
The conversion has not been manually checked. There are a few known discrepancies from UD:

* no mwe analysis in the treebank. This is also information that is not present in the original data.


### REFERENCES

Kristin Hagen, Janne Bondi Johannessen and Anders Nøklestad: "A
Constraint-based Tagger for Norwegian". 2000. Proceedings of the 17th
Scandinavian Conference in Linguistics.

Kari Kinn, Per Erik Solberg and Pål Kristian Eriksen. "NDT Guidelines
for Morphological Annotation". National Library Tech Report.

Per Erik Solberg, Arne Skjærholt, Lilja Øvrelid, Kristin Hagen and
Janne Bondi Johannessen. 2014."The Norwegian Dependency Treebank",
Proceedings of LREC 2014, Reykjavik

Velldal, Erik; Øvrelid, Lilja & Hohle, Petter (2017). Joint UD Parsing of Norwegian Bokmål and Nynorsk , In Jörg Tiedemann (ed.),  Proceedings of the 21st Nordic Conference on Computational Linguistics (NoDaLiDa).  Linköping University Electronic Press.  ISBN 978-91-7685-601-7.  Article no. 001.  s 1 - 10 

# Acknowledgements

NDT has been automatically converted to the UD scheme by Lilja Øvrelid at the University of Oslo. Petter Hohle created the data splits and Fredrik Jørgensen aligned the treebank to the original texts.
We thank the annotators of the original NDT: Pål Kristian Eriksen, Kari Kinn and Per Erik Solberg.


### CHANGELOG

--> UD 2.12

* The conversion is completely rewritten using [Grew](https://grew.fr/) by the Norwegian Language Bank at the National Library of Norway. The conversion is to a large
extent based on the guidelines of the previous version.
* *som* in relative clauses is not longer treated as pronouns, but complementizers with the postag SCONJ and the label mark.
* There is no longer an explicit analysis of verbal particles. The postag has changed from ADP to ADV and the label is advmod.
* [The changes in 2.10 and 2.12](https://universaldependencies.org/changes.html) are implemented.

=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.0
License: CC BY-SA 4.0
Includes text: yes
Genre: news blog nonfiction
Lemmas: converted from manual
UPOS: converted from manual
XPOS: not available
Features: converted from manual
Relations: converted from manual
Contributors: Øvrelid, Lilja; Jørgensen, Fredrik; Hohle, Petter; Dale, Ingerid Løyning; Solberg, Per Erik; Kåsen, Andre
Contributing: elsewhere
Contact: per.solberg@nb.no
===============================================================================

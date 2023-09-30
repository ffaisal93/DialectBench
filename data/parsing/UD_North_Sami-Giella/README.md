# Summary

This is a North Sámi treebank based on a manually disambiguated and function-labelled gold-standard
corpus of North Sámi produced by the Giellatekno team at UiT Norgga árktalaš universitehta.

# Introduction

The corpus was first analysed using a finite-state morphological analyser for North Sámi, and then
disambiguated using a constraint-grammar-based disambiguator. The constraint grammar disambiguator
also annotated syntactic function labels. The analyses and the function labels were manually
corrected to produce a gold standard, and then a rule-based dependency parser was run on top
of the gold data. On top of those parsers a series of tree-rewrite rules were used to convert
the corpus to Universal Dependencies. Please see the paper below for details.

# Acknowledgements

We are immensely grateful to the Giellatekno team, and especially to Trond Trosterud and Lene Antonsen
for annotating the original data and for producing the rule-based parser on which the treebank is
based. Their comments and help were invaluable.

If you use this data in your work, please cite:

@inproceedings{sheyanova:2017,
    author = {Mariya Sheyanova and Francis M. Tyers},
    title = {Annotation schemes in North Sámi dependency parsing},
    booktitle = {Proceedings of the 3rd International Workshop for Computational Linguistics of Uralic Languages},
    pages = {66--75},
    year = 2017
}

# Changelog

* 2021-05-15 v2.8
  * Undocumented PronType=Coll should actually be NumType=Coll (still language-specific).
* 2018-04-15 v2.2
  * Repository renamed from UD_North_Sami to UD_North_Sami-Giella.
* 2017-11-15 v2.1
  * First official release after it was used as a surprise dataset in the
    CoNLL 2017 shared task.

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.1
License: CC BY-SA 4.0
Includes text: yes
Genre: nonfiction news
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Trosterud, Trond; Antonsen, Lene; Tyers, Francis
Contributing: elsewhere
Contact: ftyers@prompsit.com
===============================================================================
</pre>

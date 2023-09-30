# Summary


_UD\_Swiss\_German-UZH_ is a tiny manually annotated treebank of 100 sentences in different Swiss German dialects and a variety of text genres.



# Introduction

This repository presents work on Universal Dependency Parsing for Swiss German, which has been done as part of the Master’s Thesis _Parsing Approaches for Swiss German_ at the [Institute for Computational Linguistics](www.cl.uzh.ch) at the University of Zurich.

The provided resources consist of 100 Swiss German sentences (from different sources), manually annotated with part-of-speech tags and universal dependencies.

[NOAH’s Corpus of Swiss German Dialects](https://noe-eva.github.io/NOAH-Corpus/corpus.html) was used as a resource for the Swiss German part-of-speech tagging process - a process preliminary to parsing.

## Annotation

In general, we follow the German guidelines [UD for German](https://universaldependencies.org/de/index.html).

The POS annotations are generally based on the German guidelines, namely the [Stuttgart-Tübingen-TagSet (STTS)](http://www.sfs.uni-tuebingen.de/resources/stts-1999.pdf) and some changes according to the [TIGER annotation scheme](https://files.ifi.uzh.ch/cl/siclemat/lehre/papers/tiger-annot.pdf). Furthermore, dealing with Swiss German, there is the need for an additional POS tag `PTKINF`, not present in the STTS tagset, as well as for the "meta tag" `TAG+`. 

* `PTKINF` is an infinitive particle which does not exist in Standard German but is frequently used in dialects. It comes in the form of _go_, _cho_, _goge_, _lo_ to name a few, as in _Si gönd go poschte_. (_They go shopping._) In the Standard German translation, _Sie gehen einkaufen._, we can see that there is no equivalent. 
* `TAG+` is used to handle merged words; we introduced the “+“-sign which can be added to any PoS tag. In the STTS there is one tag like this: the `APPRART`, used for combinations of articles and prepositions like _im_ consisting of _in + dem_ (_in the_). However, in Swiss German these kind of merges are performed with any kind of words and just merging the tags would result in a big tagset. Therefore we decided to use the "head" of the word or the first word as tag and simply add a plus to show that this word incorporates another one [Hollenstein and Aepli, 2014](). Like this, they can easily be found and, if needed, manually expanded. Frequent examples of such words include _hemmer_ (_haben + wir_), _häts_ (_hat + es_), and _sinz_ (_sind + sie_), for _we have_, _it has_ and _they are_.


The Universal Dependency POS (UPOS) tags are converted according to the mapping provided by the Universal Dependency. Additionaly:

* `PTKINF` are converted to `PART`
* the plus sign in `TAG+` are disgarded




# Acknowledgments

This work has been performed at the University of Zurich by Noëmi Aepli with the help of Simon Clematide.

## References

* Citation:

```
@inproceedings{aepli2018parsing,
  title={{Parsing Approaches for Swiss German}},
  author={No\"emi Aepli and Simon Clematide},
  booktitle={{Proceedings of the 3rd Swiss Text Analytics Conference (SwissText), Winterthur, Switzerland}},
  year={2018}
}
```

* [Download Paper](https://www.zora.uzh.ch/id/eprint/159152/1/paper1.pdf) 
* [Download Master's Thesis](http://www.cl.uzh.ch/dam/jcr:cdad4255-ddd4-4071-a706-491e75085339/aepli_noemi_1990.pdf)


# Changelog

* 2019-11-15 v2.5
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.5
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction news blog wiki nonfiction
Lemmas: not available
UPOS: converted with corrections
XPOS: manual native
Features: not available
Relations: manual native
Contributors: Aepli, Noëmi
Contributing: here
Contact: naepli@cl.uzh.ch
===============================================================================
</pre>

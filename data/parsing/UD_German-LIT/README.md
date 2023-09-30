# Summary

This treebank aims at gathering texts of the German literary history. Currently, it hosts Fragments of the early Romanticism, i.e. aphorism-like texts mainly dealing with philosophical issues concerning art, beauty and related topics.

# Introduction

In a long-term perspective, this treebank aims at gathering texts from different genres and different authors of the German literary history. Currently, it exclusively hosts Fragments of the early Romanticism (end of the 18th century, modern German), i.e. really short texts, often in aphorism-like form, that deal with philosophical issues in a witty and cryptic way. They mainly deal with aesthetics, i.e. philosophy concerning art and beauty.
This treebank is mainly intended for corpus-based stylistic analysis that can benefit from the dependency relations as well as from all the other levels of annotation (currently LEMMA and both UPOs and XPOS).

The version 2.5 hosts the following texts (each text is followed by the reference to the original edition from which it  was digitized, as well as by the permalink to the online source of the digital raw text):

- Friedrich Schlegel, Kritische Fragmente [Lyceum-Fragmente].
Source: Kritische Friedrich-Schlegel-Ausgabe. Erste Abteilung: Kritische Neuausgabe, Band 2, München, Paderborn, Wien, Zürich 1967, S. 147-164.
Erstdruck in: Lyceum der schönen Künste (Berlin), 1. Bd., 2. Teil, 1797.
Permalink: http://www.zeno.org/nid/20005618886

- Friedrich Schelgel, Athenäums-Fragmente [fragments from 1 to 421].
Source: Kritische Friedrich-Schlegel-Ausgabe. Erste Abteilung: Kritische Neuausgabe, Band 2, München, Paderborn, Wien, Zürich 1967, S. 165-256.
Erstdruck in: Athenäum (Berlin), 1. Bd., 2. Stück, 1798.
Permalink: http://www.zeno.org/nid/20005618908

- Novalis, Blüthenstaub.
Source: Novalis: Schriften. Die Werke Friedrich von Hardenbergs. Band 2, Stuttgart 1960–1977, S. 413-464.
Entstanden 1797/98. Erstdruck in: Athenäum (Berlin), 1. Bd., 1. Stück, 1798. Vier Fragmente stammen von Friedrich Schlegel.
Permalink: http://www.zeno.org/nid/20005446929

Each sentence in the treebank is preceded by some comments introduced by '#', through which the following information is respectively encoded:
- Genre
- Author
- Work
- Number of the fragment. It is based upon the classification adopted in the source raw text. Each time a new fragemnt begins, it is preceded by the comment 'newpar id = [name]', and the number of the fragment is incorporated into the 'sent_id' field as well, followed by the numer of the sentence in that fragment. Moreover, each time a new collection of fragment, i.e. work, begins, it is preceded by the comment '# newdoc id = [name]'. For instance:

- '# newdoc id = bluethenstaub'
- '# newpar id = bluethenstaub-f1'
- '# author = Novalis'
- '# work = Blüthenstaub'
- '# sent_id = bluethenstaub-f1-s1'

In this case, the sentence following the set of comments would be the first sentence of the first fragment of the collection "Blüthenstaub" written by Novalis.
We made this choice about such a use of comments because we want to preserve the parallelism between the treebanked data and the source texts as much as possible. In this perpsetive, this treebank aims to be the linguistically annotated counterpart of the orgiginal texts, thus preserving those categories that we are traditionally acquainted to adopt in order to work on literary texts.

# Acknowledgments

Many thanks to Daniel Zeman, who has promptly solved some fundamental problems concerning the data format, and showed great interest for this project right from the beginning.
...

# Changelog

* 2023-05-15 v2.12
  * Fixed: nominals cannot have obj and iobj children.
  * Dative arguments are oblique, hence they are obl:arg and not iobj.
  * PRON vs. DET annotation made consistent across German UD treebanks.
* 2019-10-30
  * Fixed all those errors reported by the validation script in the version 2.4.

## References

* (citation)

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.4
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: nonfiction
Lemmas: automatic with corrections
UPOS: converted with corrections
XPOS: automatic with corrections
Features: not available
Relations: manual native
Contributors: Salomoni, Alessio
Contributing: elsewhere
Contact: alessio.salomoni@unibg.it
===============================================================================
</pre>

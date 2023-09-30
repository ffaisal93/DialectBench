# Summary

The NYUAD Arabic UD treebank is based on the Penn Arabic Treebank (PATB), parts 1, 2, and 3, through conversion to CATiB dependency trees.


# Introduction

The treebank consists of 19,738 sentences (738889 tokens), and its domain is mainly newswire. The annotation is licensed under the terms of CC BY-SA 4.0, and the original PATB can be obtained from the LDC’s official website.

The morphological and syntactic annotation of the NYUAD Arabic UD treebank is created through automatic conversion of the PATB data.


# Acknowledgments

We would like to thank the Linguistic Data Consortium's Arabic language group, and particularly Dr. Mohamed Maamouri and Drs Ann Bies and Seth Kulick, as well as the rest of the annotation team who participated in creating the Penn Arabic Treebank. We also would like to thank Reem Faraj, Ryan Roth and the annotators of the Columbia Arabic Treebank. The development of the the NYUAD Arabic UD treebank relied heavily on these two efforts.


# Data Splits

The data was split into Train, Dev, and Test according to the LDC Arabic treebanks and associated corpora: Data divisions manual (Diab, Mona, Nizar Habash, Owen Rambow, and Ryan Roth. arXiv preprint arXiv:1309.5652 (2013))

# Data

Due to LDC licensing restrictions, the annotations are released without the data. To merge the annotation with the corresponding PATB data, please follow the following steps:
1) obtain a copy of the PATB data from the LDC website:
PATB Part 1, v4.1: https://catalog.ldc.upenn.edu/LDC2010T13
PATB Part 2, v3.1: https://catalog.ldc.upenn.edu/LDC2011T09
PATB Part 3, v3.2: https://catalog.ldc.upenn.edu/LDC2010T08
2) combine all the integrated files from all three treebanks in one directory.
Note: if you don’t have all three treebank, the trees coming from them will be left as is.
3) Run the following command:
java -jar merge.jar <conllu file> <integrated files directory>


# Statistics

Train
Tree count:  15,789
Word count:  590,819
Token count: 502,991
Dep. relations: 28 of which 3 language specific
POS tags: 16
Category=value feature pairs: 28

Dev
Tree count:  1,986
Word count:  73,945
Token count: 63,136
Dep. relations: 28 of which 3 language specific
POS tags: 16
Category=value feature pairs: 27

Test
Tree count:  1,963
Word count:  74,125
Token count: 63,168
Dep. relations: 28 of which 3 language specific
POS tags: 16
Category=value feature pairs: 27


# Changelog

* 2017-11-15 v2.1
  * No change.
* 2017-03-01 v2.0
  * Initial UD release.


=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.0
License: CC BY-SA 4.0
Includes text: no
Genre: news
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Habash, Nizar; Taji, Dima
Contributing: elsewhere
Contact: taji@ufal.mff.cuni.cz
===============================================================================

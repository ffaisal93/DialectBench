# Summary

TWITTIRÒ-UD is a collection of ironic Italian tweets annotated in Universal Dependencies.
The treebank can be exploited for the training of NLP systems to enhance their performance on social media texts, and in particular, for irony detection purposes.


# Introduction

TWITTIRÒ-UD has been created by enriching a resource originally developed for training and testing irony detection systems, also exploited as a benchmark for the Italian irony detection task held in EVALITA 2018
(Cignarella et al., 2018c). The treebank comprises both the fine-grained annotation for irony applied in Karoui et al. (2017), and the morphological and syntactic information encoded by the UD format.

The original corpus consists of 1,424 tweets (28,387 tokens). The syntactic annotation process was carried out through alternating steps of automatic scripting and manual revision, and finally with some out-of-domain parsing experiments. Parsing results also underwent a manual revision by two independent annotators.

In order to meet the requirements of the EU General Data Protection Regulation (GDPR), entered into force on May 2018, the resource content has been pseudonymized, by substituting original tweet IDs and user names.

:warning: An overall amount of 527 tweets overlaps with [PoSTWITA-UD](https://github.com/UniversalDependencies/UD_Italian-PoSTWITA).
The overlapping content however has been distributed such that it ends up in the same partition in both treebanks.


# Corpus splitting

The treebank has been randomly split as follows:
* it_twittiro-ud-train.conllu: 1,138 tweets
* it_twittiro-ud-dev.conllu: 144 tweets
* it_twittiro-ud-test.conllu: 142 tweets


# Basic statistics
Tree count:  1,424
Word count:  29,605
Token count: 28,387
Dep. relations: 54 of which 19 language specific
POS tags: 16
Category=value feature pairs: 42


# References
* Cignarella, A. T., Bosco, C., Patti, V., & Lai, M. (2018). Application and analysis of a multi-layered scheme for irony on the Italian Twitter Corpus TWITTIRO. In LREC 2018, Eleventh International Conference on Language Resources and Evaluation (pp. 4204-4211). European Language Resources Association (ELRA).

* Cignarella, A. T., Bosco, C., & Rosso, P. (2019). Presenting TWITTIRÒ-UD: An Italian Twitter Treebank in Universal Dependencies. In Proceedings of the Fifth International Conference on Dependency Linguistics (Depling, SyntaxFest 2019) (pp. 190-197).

* Cignarella, A. T., Frenda, S., Basile, V., Bosco, C., Patti, V., & Rosso, P. (2018). Overview of the EVALITA 2018 task on Irony Detection in Italian Tweets (IronITA). In Sixth Evaluation Campaign of Natural Language Processing and Speech Tools for Italian (EVALITA 2018) (Vol. 2263, pp. 1-6). CEUR-WS.

* Karoui, J., Benamara, F., Moriceau, V., Patti, V., Bosco, C., and Aussenac-Gilles, N. (2017). Exploring the impact of pragmatic phenomena on irony detection in tweets: A multilingual corpus study. In Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics (pp. 262–272)


# Changelog

* 2019-11-15 v2.5
  * Initial release in Universal Dependencies.


# Metadata

=== Machine-readable metadata (DO NOT REMOVE!) ================================
```
Data available since: UD v2.5
License: CC BY-SA 4.0
Includes text: yes
Genre: social
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Cignarella, Alessandra T.; Bosco, Cristina; Sanguinetti, Manuela
Contributing: elsewhere
Contact: cigna@di.unito.it
```
===============================================================================

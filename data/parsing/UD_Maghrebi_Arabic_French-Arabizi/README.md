# Summary

A Universal Dependencies corpus for a romanized user-generated content variety of Algerian, a North-African Arabic dialect known for its frequent usage of code-switching. We added to the UD annotations NER annotations extending the French Treebank NER scheme (Sagot et al, 2012) and Offensive language classification and corrected many of the translations (still ongoing).

# Introduction

The first version of the NArabizi Corpus was presented in [(Seddah & al., 2020)](https://aclanthology.org/2020.acl-main.107.pdf), with extensive parsing results presented in [(Riabi et al, 2021)](https://aclanthology.org/2021.wnut-1.47/).
More details about this release will be available in an upcoming publication.

# Splitting
The now deduplicated corpus contains 18561 tokens in 1287 sentences.

In **UD_Magherebi_Arabic_French-Arabizi**, data were randomly split into:

 * `fr_Magherebi_Arabic_French-Arabizi-ud-test.conllu`: 14444 tokens in 1003 sentences
 * `fr_Magherebi_Arabic_French-Arabizi-ud-dev.conllu`: 2064 tokens in 139 sentences
 * `fr_Magherebi_Arabic_French-Arabizi-ud-train.conllu`: 2053 tokens in 145 sentences

# Genres
The original sentences of the corpus are taken from:
 * Algerian newspaper’s web forums collected by [(Cotterell et al., 2014)](http://www.lrec-conf.org/proceedings/lrec2014/workshops/LREC2014Workshop-OSACT%20Proceedings.pdf#page=39).
 * Lyrics from a few dozen popular songs of various genres (Raï, hip-hop, etc.)


# Acknowledgments
* contributors: Arij Riabi, Farah Essaidi, Amal Fethi, Menel Mahamdi, Djamé Seddah
* contact: Arij Riabi: arij.riabi@inria.fr, Djamé Seddah: djame.seddah@gmail.com
* UD maintainer: Arij Riabi: arij.riabi@inria.fr, Djamé Seddah: djame.seddah@gmail.com

# References
* Djamé Seddah, Farah Essaidi, Amal Fethi, Matthieu Futeral, Benjamin Muller, Pedro Javier Ortiz Suárez, Benoît Sagot, and Abhishek Srivastava. 2020. [Building a user-generated content North-African Arabizi treebank: Tackling hell](https://aclanthology.org/2020.acl-main.107.pdf). In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 1139–1150, Online Association for Computational Linguistics.
* Benoît Sagot, Marion Richard, Rosa Stern. 2012. [Annotation référentielle du Corpus Arboré de Paris 7 en entités nommées}(https://aclanthology.org/F12-2050.pdf). In Proceedings of the Joint Conference JEP-TALN-RECITAL 2012, volume 2, TALN.

* New publication coming soon.

# Changelog
* 2023-05-15 v2.12
  * Initial release in Universal Dependencies.
* 2023-03-8
  * Manual corrections in the original Treebank
  * Deduplication of threebank
  * Improve NOUN/PROPN distinction
  * Several changes for harmonisation
  * Harmonisation of tokenisation
  * Correction of the cycles
  * Fixing encoding error for Arabic script
  * Verify and fix origin text
  * Add NER annotations in MISC field
  * Add offensive annotations in the Meta data.
  * Fix some translations by Native speakers


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.12
License: CC BY-SA 4.0
Includes text: yes
Genre: nonfiction news
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Riabi, Arij; Essaidi, Farah; Fethi, Amal; Mahamdi, Menel; Seddah, Djamé
Contributing: elsewhere
Contact: djame.seddah@gmail.com
===============================================================================
</pre>

# Summary

The South_Levantine_Arabic-MADAR treebank consists of 100 manually-annotated sentences taken from the [MADAR](https://camel.abudhabi.nyu.edu/madar/) (Multi-Arabic Dialect Applications and Resources) project.

TO-DO: Add 20 annotated sentences from CCC as a train set.

# Introduction

The treebank contains 100 manually annotated sentences in the South Levantine dialect primarily spoken in Amman. The sentences were taken from the "MADAR Parallel Corpus Dataset" (Bouamor et al., 2018) which consists of parallel texts translated into 25 dialects spoken in 25 diferent cities in the Arab World. The original texts were taken from the Basic Traveling Expression Corpus (BTEC) (described in Takezawa et al., 2007).

Sentences in the treebank can best be described as short conversational tourism-related texts.

The treebank was created as part of the "Language Technology: Research and Development" course at Uppsala University. You can view the report here: ["Parsing Low-Resource Levantine Arabic: Annotation Projection versus Small-Sized Annotated Data"](https://drive.google.com/file/d/1LJF00GqSiMF6lZ_vtJflh22-V7e065xp/view?usp=sharing). The report describes two methods for parsing low-resource Levantine Arabic using the treebank provided in this repo (but split instead into three sets: train, dev, and test).

# Acknowledgments

Big thanks to Houda Bouamor, Nizar Habash, and the MADAR project team for creating the [multi-dialect parallel corpus](https://camel.abudhabi.nyu.edu/madar-parallel-corpus/) and allowing me to use the Amman portion of it prior to official release.

## References

* Bouamor, Houda, Nizar Habash, Mohammad Salameh, Wajdi Zaghouani, Owen Rambow, Dana Abdulrahim, Ossama Obeid, Salam Khalifa, Fadhl Eryani, Alexander Erdmann and Kemal Oflazer. The MADAR Arabic Dialect Corpus and Lexicon. In Proceedings of the International Conference on Language Resources and Evaluation (LREC 2018), Miyazaki, Japan, 2018.

* Takezawa, Toshiyuki, et al. "Multilingual spoken language corpus development for communication research." International Journal of Computational Linguistics & Chinese Language Processing, Volume 12, Number 3, September 2007: Special Issue on Invited Papers from ISCSLP 2006. 2007.


# Changelog

* 2022-11-15 v2.11
  * Fixed double subject in a sentence.
* 2020-11-15 v2.7
  * Initial release in Universal Dependencies.

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.7
License: CC BY-SA 4.0
Includes text: yes
Genre: spoken social
Lemmas: manual native
UPOS: manual native
XPOS: not available
Features: not available
Relations: manual native
Contributors: Zahra, Shorouq
Contributing: here
Contact: shorouqjzahra@gmail.com
===============================================================================
</pre>

# Summary

UD Turkish-German SAGT is a Turkish-German code-switching treebank that is developed as part of the [SAGT](https://www.ims.uni-stuttgart.de/en/research/projects/sagt/) project. 

# Introduction

The treebank consists of bilingual conversation transcriptions annotated with several
layers: language IDs, lemmas, POS tags, morphological features, and dependency
relations. Language IDs are described below.
The rest of the annotations follow the Universal Dependencies annotation scheme, and
the conventions used in monolingual Turkish and German treebanks. 

There are 48 distinct conversations from 17 participants.
The majority of the speakers are university students, hence the most
frequent age range is 18–25. Common conversation themes include studies, work,
travel, free time activities such as sports, books, TV, and future plans.

The accompanying audio recordings of transcriptions are also available as a speech corpus, with
a separate licence. Please contact ozlem@ims.uni-stuttgart.de for further information.

# Data Split

In total, there are 2184 sentences in the treebank. All sentences contain at least one intrasentential switch.
The data is split into train, development, and test sets, paying attention to conversation boundaries as well as a balanced theme and participant distribution.

<table>
<tr style="background-color: #eee"><th>Split</th><th># Conversations</th><th># Sentences</th><th># Tokens</th>
</tr>
<tr><td>train      </td><td>15</td><td>578</td><td>10084</td></tr>
<tr><td>development</td><td>17</td><td>801</td><td>13057</td></tr>
<tr><td>test       </td><td>16</td><td>805</td><td>14092</td></tr>
</table>

# Language IDs

The treebank annotates two types of language IDs. The first one is stored as the `CSID` feature in the MISC column and follows the tag set of Çetinoğlu (2016). Each token has one of the following tags:

- TR: Turkish
- DE: German
- LANG3: Third language
- MIXED: Intra-word code-switching
- OTHER: Punctuation, numbers, emoticons, symbols etc.

The second type of language ID is stored as the `Lang` feature in the MISC column. With this feature, it is possible to use the UD validator to check language-specific constraints. The value of the feature is the ISO 639 code of the token's language in UD. It corresponds to

- 'tr' for TR tokens
- 'de' for DE tokens
- corresponding ISO codes for LANG3 tokens (e.g., 'en' for English)
- qtd, the language code of the SAGT treebank, for MIXED tokens
- no `Lang` feature for OTHER tokens



# Contributors

* Özlem Çetinoğlu -- IMS, University of Stuttgart
* Çağrı Çöltekin -- Department of Linguistics, University of Tübingen

# Acknowledgments

The treebank development is funded by DFG via project CE 326/1-1 “Computational Structural Analysis of German-Turkish  Code-Switching”. We thank Cansu Turgut, Reha Sakızlı, Semanur Ceylan, and Sevde Ceylan for data collection and annotation.

## References

For the treebank and speech collection:

Çetinoğlu, Özlem and Çağrı Çöltekin (2022). “Two languages, one treebank: building a Turkish–German code-switching treebank and its challenges”. In: _Language Resources
and Evaluation_, pp. 1–35. issn: 1574-020X.

https://link.springer.com/content/pdf/10.1007/s10579-021-09573-1.pdf

```
@article{cetinoglu2022,
year = {2022},
title = {{Two languages, one treebank: building a Turkish–German code-switching treebank and its challenges}},
author = {Çetinoğlu, Özlem and Çöltekin, Çağrı},
journal = {Language Resources and Evaluation},
issn = {1574-020X},
doi = {10.1007/s10579-021-09573-1},
pages = {1--35}
}
```

For the treebank:
* Özlem Çetinoğlu and Çağrı Çöltekin (2019). "Challenges of Annotating a Code-Switching Treebank". In _Proceedings of the 18th International Workshop on Treebanks and Linguistic Theories (TLT, SyntaxFest 2019)_.

<https://www.aclweb.org/anthology/W19-7809.pdf>

```
@inproceedings{cetinoglu2019,
    title = "Challenges of Annotating a Code-Switching Treebank",
    author = {{\c{C}}etino{\u{g}}lu, {\"O}zlem  and
      {\c{C}}{\"o}ltekin, {\c{C}}a{\u{g}}r{\i}},
    booktitle = "Proceedings of the 18th International Workshop on Treebanks and Linguistic Theories (TLT, SyntaxFest 2019)",
    OPTmonth = aug,
    year = "2019",
    address = "Paris, France",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-7809",
    doi = "10.18653/v1/W19-7809",
    pages = "82--90",
}
```


For language IDs:
* Özlem Çetinoğlu (2016). "A Turkish-German Code-Switching Corpus". In _Proceedings of the 10th edition of the Language Resources and Evaluation Conference_.

<http://www.lrec-conf.org/proceedings/lrec2016/pdf/1151_Paper.pdf>

```
@InProceedings{cetinoglu2016,
  author = {Özlem Çetinoğlu},
  title = {A {Turkish}-German Code-Switching Corpus},
  booktitle = {Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016)},
  year = {2016},
  location = {Portorož, Slovenia},
  pages = {23--28},
  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Sara Goggi and Marko Grobelnik and Bente Maegaard and Joseph Mariani and Helene
           Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {978-2-9517408-9-1},
} 
```

# Changelog

* 2023-05-15 v2.12
  * The `Polarity=Neg` feature is not used together with `PronType=Neg` (German _kein_).

* 2021-11-15 v2.9
  * The `LangID` feature is renamed as `CSID`, and the `Lang` feature is introduced.
  
* 2020-05-15 v2.8
  * The full set of training data is released.
  
* 2020-11-15 v2.7
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.7
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: spoken
Lemmas: manual native
UPOS: manual native
XPOS: not available
Features: manual native
Relations: manual native
Contributors: Çetinoğlu, Özlem; Çöltekin, Çağrı
Contributing: elsewhere
Contact: ozlem@ims.uni-stuttgart.de
===============================================================================
</pre>

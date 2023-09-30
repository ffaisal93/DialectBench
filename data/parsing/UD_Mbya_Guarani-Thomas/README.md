# Summary

UD Mbya_Guarani-Thomas is a corpus of Mbyá Guaraní (Tupian) texts collected by Guillaume Thomas. The current version of the corpus consists of three speeches by Paulina Kerechu Núñez Romero, a Mbyá Guaraní speaker from Ytu, Caazapá Department, Paraguay.

# Introduction

UD Mbya_Guarani-Thomas is a corpus of Mbyá Guaraní (Tupian) texts collected by Guillaume Thomas. The current version of the corpus consists of three speeches by Paulina Kerechu Núñez Romero, a Mbyá Guaraní speaker from Paraguay. These speeches were recorded in August 2017 in the Mbyá Guaraní community Ytu, Caazapá Department, Paraguay. They were transcribed by Ronaldi Recalde Centurion (Ytu community) and translated into Brazilian Portuguese by Alberto Álvares. The texts were interlinearized in SIL FieldWorks Language Explorer (Black and Simons 2006) and manually annotated in UD in Arborator (Gerdes 2013) by Guillaume Thomas. Features were converted automatically from the morphological glosses added in SIL FieldWorks Language Explorer.

Consider using the development version of the corpus, which contains the latest improvements, while the official release is updated every 6 months:

* https://github.com/UniversalDependencies/UD_Mbya_Guarani-Thomas/tree/dev

# Acknowledgments

The development of the corpus was supported by a Connaught New Researcher Award to Guillaume Thomas at the University of Toronto.

Special thanks are due to Paulina Kerechu Núñez Romero for allowing us to use these recordings, and to Ronaldi Recalde Centurion and Alberto Álvares for their essential role in transcribing and translating these recordings.

## References

* Andrew Black and Gary Simons. 2006. The SIL FieldWorks Language Explorer Approach to Morphological Parsing. Computational Linguistics for Less studied Languages: Texas Linguistics Society, 10. SIL.

* Kim Gerdes, 2013. Collaborative dependency annotation. In Journal Proceedings of the second international conference on dependency linguistics (DepLing 2013), 88-97.


# Changelog

* 2021-05-15 v2.8
  * Subcat=Int,Ditran,IntInd changed to Subcat=Intr,Ditr,Indir following the global UD documentation.

* 2019-06-07 v2.4
  * Corrected dependencies in GUN001R030I001 (sent 988-1006)
  * Updated annotation guidelines on [gpythomas.com/Mbya_Treebank_Guidelines.pdf](https://www.gpythomas.com/Mbya_Treebank_Guidelines.pdf)
  * Revised xpos annotation of adjectives and adverbs (see revised annotation guidelines)
  * Fixed feature annotation of pronouns
  * Corrected bugs identified in udapi tools

* 2019-05-15 v2.4
  * Initial release in Universal Dependencies.

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.4
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: nonfiction
Lemmas: automatic
UPOS: automatic with corrections
XPOS: manual native
Features: converted with corrections
Relations: automatic with corrections
Contributors: Thomas, Guillaume
Contributing: elsewhere
Contact: guillaume.thomas@utoronto.ca
===============================================================================
</pre>

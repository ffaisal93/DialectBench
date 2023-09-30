# Summary

UD Mbya_Guarani-Dooley is a corpus of narratives written in Mbyá Guaraní (Tupian) in Brazil, and collected by Robert Dooley. Due to copyright restrictions, the corpus that is distributed as part of UD only contains the annotation (tags, features, relations) while the FORM and LEMMA columns are empty.

# Introduction

UD Mbya_Guarani-Dooley is the UD annotation of a corpus of narratives written by two Mbyá Guaraní speakers, Nelson Florentino and Darci Pires de Lima, between 1976 and 1990 in Brazil. The corpus was compiled by Robert A. Dooley (SIL), and is archived at the Archive of the Indigenous Languages of Latin America:

* Dooley, Robert A. "Mbyá Guaraní Collection of Robert Dooley" The Archive of the Indigenous Languages of Latin America: www.ailla.utexas.org. Media: text. Access: 100% restricted. PID ailla:119734

The narratives in Dooley's collection were interlinearized in SIL FieldWorks Language Explorer (Black and Simons 2006), and manually annotated in UD in Arborator (Gerdes 2013). Features were converted automatically from the morphological glosses added in SIL FieldWorks Language Explorer.

Due to copyright restrictions, the corpus that is distributed as part of UD only contains the annotation (tags, features, relations), while the FORM and LEMMA columns are empty. A password protected version of UD Mbya_Guarani-Dooley with FORM and LEMMA fields is archived on the Archive of the Indigenous Languages of Latin America, in the following collection:

* Guillaume, Thomas and Dooley, Robert A. Dependency Treebank derived from the Mbyá Guaraní collection of Robert Dooley. Access: 100% restricted. PID ailla:119734

Consider using the development version of the corpus, which contains the latest improvements, while the official release is updated every 6 months:

* https://github.com/UniversalDependencies/UD_Mbya_Guarani-Dooley/tree/dev

# Acknowledgments

The development of the corpus was supported by a Connaught New Researcher Award to Guillaume Thomas at the University of Toronto. Several research assistants participated in the dependency annotation of the corpus:

* Gregory Antono, Laurestine Bradford, Vidhya Elango, Jean-François Juneau, Angelika Kiss, Barbara Peixoto, Darragh Winkelman.

## References

* Andrew Black and Gary Simons. 2006. The SIL FieldWorks Language Explorer Approach to Morphological Parsing. Computational Linguistics for Less studied Languages: Texas Linguistics Society, 10. SIL.

* Kim Gerdes, 2013. Collaborative dependency annotation. In Journal Proceedings of the second international conference on dependency linguistics (DepLing 2013), 88-97.


# Changelog

* 2021-05-15 v2.8
  * Subcat=Int,Ditran,IntInd changed to Subcat=Intr,Ditr,Indir following the global UD documentation.

* 2019-10-12 v2.4 (dev branch)
  * Major modifications in preparation for v2.5 release. See updated annotation guidelines.

* 2019-06-07 v2.4 (dev branch)
  * Corrected many typos. Checked for bug with udapi.

* 2019-06-07 v2.4 (dev branch)
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
Includes text: no
Genre: fiction
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

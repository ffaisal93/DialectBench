# Summary

This treebank consists of dialectal transcriptions of spoken Komi-Zyrian. The current texts are short recorded segments from different areas where the Iźva dialect of Komi language is spoken.

# Introduction

The materials have been collected within the Iźva Komi Documentation Project, funded by Kone Foundation in 2014-2016, and archived in [The Language Archive](https://archive.mpi.nl/islandora/object/lat%253A1839_00_0000_0000_0021_64F1_D). The transcriptions have been done by native speakers, and the orthographic transcription system, although matching the Komi orthography where applicable, is primarily phonemic. The data in this treebank represents only the northern Iźva dialect of Komi, but materials from other dialects will also be included in the future. The `sent_id` values match those in archived the IKDP corpus, and the `+` character is used to mark sentence IDs that span across multiple annotations.

The corpus contains portions of recordings made between 1959 and 2016. The parts that have been published earlier by Erik Vászolyi in the Specimina Sibirica series are reproduced here with written permission. One portion of the corpus comes from Syrjänische Texte Bd. III published by Finno-Ugrian Society, and originally translated and edited by Paula Kokkonen. 

The IKDP corpus uses the treebank as one of its annotation schemes. The entire audio-visual language documentation corpus will be archived in 2021 both to [The Language Archive in Nijmegen](https://archive.mpi.nl/tla/islandora/object/tla%3A1839_00_0000_0000_0021_64F1_D) and the [Language Bank of Finland](https://www.kielipankki.fi/language-bank/). In this process, the actual linking of the treebank to the multimedia files will be revisited and clear conventions for doing this will be developed and documented. 

# Acknowledgments

The work was done as collaboration within the [Kone Foundation](https://koneensaatio.fi/)-funded research project [Language Documentation meets Language Technology: The Next Step in the Description of Komi](langdoc.github.io/IKDP-2) and the LAKME project funded by a grant from Paris Sciences et Lettres (IDEX PSL reference ANR-10-IDEX-0001-02).

If you use this treebank in your work, please cite:

- Partanen, Niko; Blokland, Rogier; Lim, KyungTae; Poibeau, Thierry and Rießler, Michael 2018: [First Komi-Zyrian Universal Dependencies Treebanks](http://universaldependencies.org/udw18/PDFs/28_Paper.pdf). Proceedings of the Second Workshop on Universal Dependencies (UDW 2018) (pp. 126-132).

## Sources used

- Blokland, Rogier; Chuprov, Vassily; Fedina, Maria; Fedina, Marina; Levchenko, Dmitriy; Partanen, Niko and Rießler, Michael. 2016: Iźva Komi Documentation Project corpus. Funded by Kone Foundation. URL: https://hdl.handle.net/1839/00-0000-0000-001B-99BC-F@view

- Vászolyi, Erik 1999: *Syrjaenica: narratives, folklore and folk poetry from eight dialects of the Komi language. Vol. 1, Upper Izhma, Lower Ob, Kanin Peninsula, Upper Jusva, Middle Inva, Udora*. Savariae.

- Uotila, T.E., Kokkonen, Paula (Ed.) 1989: *Syrjänische Texte. Bd III. Komi-Syrjänisch: Luza-Letka-, Ober-Sysola-, Mittel-Sysola-, Prisyktyvkar-, Unter-Vychegda- und Udora-Dialekte.* Suomalais-Ugrilaisen Seuran Toimituksia — Mémoires de la Société Finno-Ougrienne 202. [Download PDF.](https://www.sgr.fi/sust/st/st3.pdf)

Recording of Eric Vászolyi that has been used in this treebank has been described in article:

- Blokland, Rogier; Partanen, Niko; Rießler, Michael 2021: This is thy brother’s voice – Documentary and metadocumentary linguistic work with a folklore recording from the Nenets-Komi contact area. In: Hämäläinen, Mika; Partanen, Niko & Alnajjar, Khalid (Eds.): Multilingual Facilitation. RootRoo Ltd. [Download PDF.](https://helda.helsinki.fi/bitstream/handle/10138/327798/20_Blokland_Multilingual_Facilitation.pdf?sequence=2&isAllowed=y)

The transcription is also published in Zenodo:

- Rogier Blokland, Niko Partanen, & Michael Rießler. (2021, March 10). langdoc/spoken-komi-corpus-vaszolyi: Spoken Komi Corpus: Erik Vászolyi (Version v0.2). Zenodo. http://doi.org/10.5281/zenodo.4593789

# Changelog

* 2023-04-29
  * Work with Valency
- 2022-04-29
  - Feature development
  - Deprel correction and documentation
  - Trouble shooting in dependencies
- 2021-04-29
  - New sentences added from Erik Vászolyi's recordings
  - New sentences included from IKDP corpus.
  - Language tags systematized.
- 2020-11-06
  - Annotations of the auxiliaries were improved
- 2020-05-15
  - New sentences included from IKDP corpus.
  - Expanding advmod:mmod, :lmod and :tmod.
  - Punctuation was harmonized
  - Various consistency improvements were made, especially in converbs and connegatives
- 2019-10-11
    - Improvements in annotation consistency: Unmarked accusatives analysed as nominatives, aux:neg and acl:relcl added new relations. Individual lemmas corrected. Few missing tags added and POS classes reconsidered Gerunds classified as converbs. Features for PronTypes and Degree improved. 
- 2019-04-30
    - New sentences added and annotations harmonized
- 2018-11-01
    - README file updated and various improvements done

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.2
License: CC BY-SA 4.0
Includes text: yes
Genre: spoken
Lemmas: automatic with corrections
UPOS: converted with corrections
XPOS: automatic with corrections
Features: automatic with corrections
Relations: manual native
Contributors: Partanen, Niko; Blokland, Rogier; Rießler, Michael; Rueter, Jack
Contributing: here
Contact: nikotapiopartanen@gmail.com
===============================================================================
</pre>

# Summary

UD Komi-Zyrian Lattice is a treebank of written standard Komi-Zyrian. 

# Introduction

The treebank contains continuous texts in the written Komi-Zyrian language. All of the data comes from openly available sources, or are individual sentences used here with exact references to the original works. The largest segments are from Lev Uspenskiy's book *Нёль боевӧй случай* (URN http://urn.fi/URN:NBN:fi-fe2014102045428), which was digitalized in the National Library of Finland's [Fenno-Ugrica](https://fennougrica.kansalliskirjasto.fi/) project, and Ivan Belyx's short story which was added to [Komi Nebögain online library](http://komikyv.org) by the author himself in 2013. Some articles from the newspaper [Выль туйӧд's 1939 number 67](http://urn.fi/URN:NBN:fi-fe201802013020) have also been included as complete texts. Several texts are used for individual examples, and these are marked with the tag `-ind`, to distinguish them from the running text. The complete list of sources with additional information and further links is available in this README file below.

# Acknowledgments

This work has been developed within the framework of the LAKME project funded by a grant from Paris Sciences et Lettres (IDEX PSL reference ANR-10-IDEX-0001-02). Thierry Poibeau is also partially supported by a RGNF-CNRS (grant between the LATTICE-CNRS Laboratory and the Russian State University for the Humanities in Moscow). In the UD releases 2.7 and 2.8. [Kone Foundation](https://koneensaatio.fi/en/)-funded research project [Language Documentation meets Language Technology: The Next Step in the Description of Komi](langdoc.github.io/IKDP-2), led by [Rogier Blokland](https://katalog.uu.se/profile/?id=N14-1060) and [Michael Rießler](https://uefconnect.uef.fi/en/person/michael.riesler/), expanded the treebank. In this phase the annotation work was done by Niko Partanen and Jack Rueter. [GiellaLT](https://giellalt.uit.no/lang-kpv) infrastucture was used in morphological analysis.

If you use this treebank in your work, please cite:

- Partanen, Niko; Blokland, Rogier; Lim, KyungTae; Poibeau, Thierry and Rießler, Michael 2018: [First Komi-Zyrian Universal Dependencies Treebanks](http://universaldependencies.org/udw18/PDFs/28_Paper.pdf). Proceedings of the Second Workshop on Universal Dependencies (UDW 2018) (pp. 126-132).

## Sources used

| Sentence id start | Publication name | Publishing year | Link to Fenno-Ugrica | Link to Komi Nebögain | 
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| 
| belykh1997a | Иван Белых 1997: Шера зэр | 1997 | | http://komikyv.org/kpv/content/шера-зэр | 
| belykh2005a | Иван Белых 2005: Таысь унаыс оз и ков | 2005 | | http://komikyv.org/kpv/node/26865 | 
| falkner1927a | Фалькнер В.Н. 1927: Лоам ми ёнӧсь, дзоньвидзаӧсь да!: мӧд нига" | 1927 | http://urn.fi/URN:NBN:fi-fe2014102045431 | http://komikyv.org/kpv/contents/loam-mi-yonos-dzonvidzaos-da | |
| goffensefer1927a | Гоффеншефер С. 1927: Чакотка | 1927 | http://urn.fi/URN:NBN:fi-fe201604159701 | http://komikyv.org/kpv/contents/chahotka |  
| koskabyr1925a | Кос Кабыр 1925: Мувыв тӧдмалӧм. Медводдза нига = Ывлавыв тӧдмалӧм. Арся уджъяс. | 1925 | http://urn.fi/URN:NBN:fi-fe2014070132058 | http://komikyv.org/kpv/contents/yvlavyv-todmalom-1 | 
| kpv_1-7_Vyl_tujod_1939_09_10_0001 | Выль туйӧд 9.10.1939, page 1 | 1939 | http://urn.fi/URN:NBN:fi-fe201802013020 | | | 
| kpv_1-7_Vyl_tujod_1939_09_10_0002 | Выль туйӧд 9.10.1939, page 2 | 1939 | http://urn.fi/URN:NBN:fi-fe201802013020 | | | 
| rossinskiy1925a | Российскӧй Д. 1925: Гут разӧдӧ висьӧмъяс | 1925 | http://urn.fi/URN:NBN:fi-fe2014070332096 | http://komikyv.org/kpv/content/гут-разӧдӧ-висьӧмъяс | 
| uspensky1940a | Успенский, Лев 1940: Нёль боевӧй случай | 1940 | http://urn.fi/URN:NBN:fi-fe2014102045428 | | | 
| Minin:OjsjaCvettez | Minjin I. A. (Минин И. А.) 1962. Vojsya dzoridzjas (Войся дзоридзьяс) (висьт) // Войвыв кодзув (1962. №1) | 1962 | | http://komikyv.org/kpv/node/31062 |

In release 2.7 various sentences used in the Komi-language grammar *Ӧнія коми кыв* (2000) were included. These sentences are marked with sent_id's that contain components `OKK:2000:page:n-th sentence:original author`. These sentences were included to cover different grammatical phenomena in Komi more thoroughly. When refering to these sentences, we advise you also cite the original source:

- Федюнёва, Г. (Ed.); Некрасова, Г.; Лудыкова, В.; Цыпанов, Е.; Попова, Э. 2000: *Ӧнія коми кыв: Морфология.* [Modern Komi Language: Morphology] Сыктывкар: Коми небӧг лэдзанін. 
- Fedûnëva, G. (Ed.); Nekrasova, G.; Ludykova, V.; Cypanov, E.; Popova, È. 2000: *Ӧnìâ komi kyv: Morfologiâ.* [Modern Komi Language: Morphology] Syktyvkar: Komi nebӧg lèdzanіn. 


# Changelog

* 2023-04-29
  * Work with Valency, Diminutive
* 2022-10-31
  * Grammar research input
  * Migrating :lmp, :lto, :lfrom into :lmod, and :comp to :cmp
- 2022-04-30
  - Feature development
  - Deprel correction and documentation
  - Trouble shooting in dependencies
- 2021-10-31
  - Auxiliary, feature and deprel documentation
  - New sentences added from grammar Ӧнія коми кыв: морфология
- 2021-04-30
  - Auxiliary, feature and deprel documentation
  - New sentences added from grammar Ӧнія коми кыв: морфология
- 2020-10-31
  - 193 new sentences added from grammar Ӧнія коми кыв: морфология
  - 10 new parallel sentences added that are shared with [Komi Permyak](https://github.com/UniversalDependencies/UD_Komi_Permyak-UH) treebank
- 2020-05-15
  - Parallel sentences from Minjin shared with Komi_Permyak-UH.
  - Expanding advmod:mmod, :lmod and :tmod.
  - Punctuation was harmonized
  - Various consistency improvements were made, especially in converbs
- 2019-10-11
  - Improvements in annotation consistency: Unmarked accusatives analysed as nominatives, aux:neg and acl:relcl new added relations. Individual lemmas corrected. Few missing tags added and POS classes reconsidered Gerunds classified as converbs. Features for PronTypes and Degree improved. New sentences added. Few typos corrected.
- 2019-04-30
    - Annotations harmonized
- 2018-11-01
  - README file updated and various corrections done
- 2018-10-18
  - New sentences from various sources added

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.2
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction
Lemmas:	automatic with corrections
UPOS: converted with corrections
XPOS: automatic with corrections
Features: automatic with corrections
Relations: manual native
Contributors: Partanen, Niko; Lim, KyungTae; Poibeau, Thierry; Rueter, Jack
Contributing: here
Contact: nikotapiopartanen@gmail.com
===============================================================================
</pre>

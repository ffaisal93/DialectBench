# Summary

This is a Komi-Permyak literary language treebank consisting of original and translated texts.


# Introduction

Initial Komi-Permyak Universal Dependency type annotation.

This includes 30 sentences originally presented as 20 at
http://ilazki.thinkgeek.co.uk/brat/#/uralic/fin with UD v1 dependencies.
The additional sentences stem from variation in expression within the
Komi-Permyak language, and the text_id with additional letters indicates
this variation. Additionally other sentences have been added in the later releases. 

The translation were made by Larisa Ponomareva based on the Finnish, Russian and Komi-Zyrian texts:

* http://ilazki.thinkgeek.co.uk/brat/#/uralic/fin
* http://ilazki.thinkgeek.co.uk/brat/#/uralic/rus
* http://ilazki.thinkgeek.co.uk/brat/#/uralic/kpv


# Acknowledgments

UH = University of Helsinki
Development repository:
[https://github.com/rueter/erme-ud-komi-permyak](https://github.com/rueter/erme-ud-komi-permyak)
Annotation work is simultaneous to finite-state transducer development by Larisa Ponomareva, Niko Partanen and Jack Rueter in the [GiellaLT](https://giellalt.uit.no/lang-koi) infrastucture, which also works with Constraint Grammar disambiguation of the morphological analysis.

Work connected to this treebank is described in following publication. If you use this treebank in your work, please cite:

* Rueter, Jack; Partanen, Niko and Ponomareva, Larisa 2020: [On the questions in developing computational infrastructure for Komi-Permyak](https://www.aclweb.org/anthology/2020.iwclul-1.3.pdf). Proceedings of the Sixth International Workshop on Computational Linguistics of Uralic Languages (pp. 15-25).

## References

* Batalova, P.M. (Баталова. Р. М.) Коми-пермяцкая диалектология. М., Изд-во "Наука", 1975. 252 с. 
* Fadejev T. Sjemjalӧn sudjba. 1965 (Фадеев Т. П.) Семьялӧн судьба (висьт) // Иньва. Литературно-художественный сборник. Кудымкар, 1965.
* Fadejev T. Pochkaez osjsjӧny, 1970 (Фадеев Т. П.) Почкаэз оссьӧны (висьт) // Почкаэз оссьӧны: рассказзэз. Кудымкар: Пермское кн. изд-во, Коми-Перм. отделение, 1970
* Fadejev T. Ybshar, 1989 (Фадеев Т. П.) Ыбшар (Роман куим частьын). Кудымкар: Пермское кн. изд-во, Коми-Перм. отделение, 1989.
* Fadejev T. Miritchӧm, 1990 (‒ Фадеев Т. П.) Миритчӧм. Ӧтік акта трагедия // Коми-пермяцкӧӥ национальнӧй драматургия. Ӧтік акта пьесаэз. Кудымкар, 1990
* Fadejev T. Goradzulj, 1993 (Фадеев Т. П.) Горадзуль. Сизим картинаа драма // Коми-пермяцкӧй национальнӧӥ драматургия. Уна акта пьесаэз. Кудымкар, 1993
* Fedosejev S. Vilj gortyn, 1985 (Федосеев С. А.) Виль гортын (повесть) // Пармаын югыт: бӧрйӧм коми-пермяцкӧй проза. Кудымкар: Пермскӧӥ книжнӧй изд-во, Коми-Пермяцкӧй отделеннё, 1985.
* Kanjukov V. Larec, 1994 (‒ Канюков В. И.) Ларец (висьт) // Чарӧтӧм пу. Кудымкар, 1994.
* Lytkin V. I. (chief ed.) 1961 Коми-пермяцкий язык, введение, фонетика, лексика и морфология.  
* Minjin I. A. (Минин И. А.) 1968. Panyt yjis tӧlisj(Паныт уйис тӧлісь) (повесть). Кудымкар, 1968.
* Minjin I. A. (Минин И. А.) 1988. Kydz shynjnjalӧ apostol (Кыдз шыннялӧ апостол) (повесть) // Оча морос: повесттез, рассказзэз, пьеса. Кудымкар: Пермское кн. изд-во, Коми-Перм. отделение, 1988.
* Minjin I. A. (Минин И. А.) 1964. Ojsja cvettez (Ойся цветтэз) (висьт) // Оча морос: повесттез, рассказзэз, пьеса. Кудымкар: Пермское кн. изд-во, Коми-Перм. отделение, 1964. (http://komikyv.org/koi/node/31063)
* Ponomareva, L.G. (Пономарева. Л. Г.) Речь северных коми-пермяков. М.: Языки Народов Мира, 2016. 514 с.
* Shadrin I. A. (Шадрин И. А.) 1959. Djoma (Дёма) (висьт) // Тулысся ваэз. Литературно-художественный сборник. Кудымкар, 1959.
* Nekrasova G. A. (Г. А. Некрасова), Sergeeva E. N. (Е. Н. Сергеева) 2018. МАРКИРОВАНИЕ АКТАНТОВ ДВУХМЕСТНЫХ ПРЕДИКАТОВ В КУДЫМКАРСКО-ИНЬВЕНСКОМ ДИАЛЕКТЕ КОМИ-ПЕРМЯЦКОГО ЯЗЫКА. Валентностные классы двухместных предикатов в разноструктурных языках [Valency classes of two-place predicates].  Отв. ред. С. С. Сай: Сборник статей. с. 354–375. СПб.: ИЛИ РАН, 2018. 624 с. ИЯЛИ КНЦ УрО РАН, Сыктывкар, Колледж метрополитена, Санкт-Петербург.



# Changelog

* 2023-04-29
  * Work with Valency, Diminutive
* 2022-10-31
  * Grammar research and dictionary input
* 2022-04-29
  * Feature development
  * Deprel correction and documentation
  * Trouble shooting in dependencies
* 2021-10-31
  * Auxiliary, feature and deprel documentation
  * Language tag systematization.
  * Example sentences from Nekrasova, G. A.; Sergeeva, E. N. 2018.
* 2021-04-29
  * Auxiliary, feature and deprel documentation
  * Language tag systematization.
* 2020-11-15 v2.7
  * Additional parallel sentences from Minjin shared with [Komi-Zyrian](https://github.com/UniversalDependencies/UD_Komi_Zyrian-Lattice) treebank.
  * Expanding compound:prt, xcomp:ds and adding VerbForm.
* 2020-05-15 v2.6
  * Parallel sentences from Minjin shared with Komi_Zyrian-Lattice.
  * Expanding advmod:mmod, :lmod, :tmod and adding NameType.
* 2019-11-15 v2.5
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.5
License: CC BY-SA 4.0
Includes text: yes
Genre: fiction
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Ponomareva, Larisa; Partanen, Niko; Rueter, Jack; Tyers, Francis
Contributing: elsewhere
Contact: rueter.jack@gmail.com
===============================================================================
</pre>

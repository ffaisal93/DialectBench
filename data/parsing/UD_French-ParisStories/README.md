# Summary

Paris Stories is a corpus of oral French collected and transcribed by Linguistics students from Sorbonne Nouvelle and corrected by students from the Plurital Master's Degree of Computational Linguistics ( Inalco, Paris Nanterre, Sorbonne Nouvelle) between 2017 and 2021.
It contains monologues and dialogues from speakers living in the Parisian region.


# Introduction

For an assignment, students had to record a friend or a relative sharing an anecdote about a given theme (meaningful encounters, vacations, interesting stories..).
The corpus was created for the study of contemporary spoken French and to train a syntactic parser for spoken French.
All data has been morpho-syntactically annotated following the SUD (Surface Syntactic Universal Dependencies) guidelines.

See SUD Guidelines : https://surfacesyntacticud.github.io/guidelines/u/

The Treebank can be found here : http://match.grew.fr/?corpus=SUD_French-ParisStories@latest

The recordings can be downloaded via the url given in the '# sound_url' metadata.

## Description

-- Paris Stories 2019 --

Creation Year : 2017

Annotation Year : 2019

Size :
- 19 samples
- 13951 tokens
- 709 sentences
- app. 1 hour of recordings


Topics : travels, funny/unusual stories

-- Paris Stories 2020 --

Creation Year : 2018

Annotation Year : 2020

Size :
- 16 samples
- 9064 tokens
- 553 sentences
- app. 30 min of recordings


Topics : vacation stories, funny/unusual stories


-- Paris Stories 2021 --

Creation Year : 2020

Annotation Year : 2021

Size :
- 14 samples
- 7825 tokens
- 499 sentences
- app. 45 minutes of recordings


Topics : first encounters, funny/unusual stories

## Development

The corpus is maintained [here](https://github.com/surfacesyntacticud/SUD_French-ParisStories) in the [SUD](https://surfacesyntacticud.github.io/) framework and automatically converter into UD using the [Grew](https://grew.fr) software with the conversions rules described [here](https://github.com/surfacesyntacticud/tools/tree/master/converter).

## Data Split

The file `fr_parisstories-ud-test.conllu` contains the following data:

  * `ParisStories_2019_cuisineApproximative.conllu`
  * `ParisStories_2019_devoirPhilosophie.conllu`
  * `ParisStories_2019_peripitiesVoiture.conllu`
  * `ParisStories_2019_prepaScientifique.conllu`
  * `ParisStories_2019_vacancesEte.conllu`
  * `ParisStories_2019_voyageItalie.conllu`
  * `ParisStories_2020_blessureRecreation.conllu`
  * `ParisStories_2020_campBedouin.conllu`
  * `ParisStories_2020_concoursInstagram.conllu`
  * `ParisStories_2020_histoireHorreur.conllu`
  * `ParisStories_2020_poissonsNoel.conllu`
  * `ParisStories_2020_sortiesAdolescence.conllu`
  * `ParisStories_2021_adoptionMouts.conllu`
  * `ParisStories_2021_couruLaVoir.conllu`
  * `ParisStories_2021_loulouLeChat.conllu`
  * `ParisStories_2021_soireeHalloweenGrange.conllu`

The file `fr_parisstories-ud-train.conllu` contains the following data:

  * `ParisStories_2019_concoursEquitation.conllu`
  * `ParisStories_2019_experienceFac.conllu`
  * `ParisStories_2019_histoireDeBanlieue.conllu`
  * `ParisStories_2019_journeeTournage.conllu`
  * `ParisStories_2019_mauriceAventure.conllu`
  * `ParisStories_2019_mercrediSoir.conllu`
  * `ParisStories_2019_patisserieFine.conllu`
  * `ParisStories_2019_peripleCrous.conllu`
  * `ParisStories_2019_stagePrimaire.conllu`
  * `ParisStories_2019_voyageEcosse.conllu`
  * `ParisStories_2020_aideAuxEnfants.conllu`
  * `ParisStories_2020_alarmeTrain.conllu`
  * `ParisStories_2020_anecdoteMetro.conllu`
  * `ParisStories_2020_descenteCanoe.conllu`
  * `ParisStories_2020_dragQueen.conllu`
  * `ParisStories_2020_galereNice.conllu`
  * `ParisStories_2020_histoireOurs.conllu`
  * `ParisStories_2020_maisonAbondonnee.conllu`
  * `ParisStories_2020_requinReunion.conllu`
  * `ParisStories_2020_sangDEncre.conllu`
  * `ParisStories_2021_discussionSansAbris.conllu`
  * `ParisStories_2021_maintenantJeSais.conllu`
  * `ParisStories_2021_neesLeMemeMois.conllu`
  * `ParisStories_2021_nouveauxEleves.conllu`
  * `ParisStories_2021_nouvelleCollegue.conllu`
  * `ParisStories_2021_pireSoireeHorrible.conllu`
  * `ParisStories_2021_pluieEtMamie.conllu`
  * `ParisStories_2021_prenomDeVieille.conllu`
  * `ParisStories_2021_rencontreAngelaMerkel.conllu`
  * `ParisStories_2021_rencontreMourinho.conllu`



# Acknowledgments

Annotation : Sylvain Kahane, Bruno Guillaume, Mariam Nakhlé, Vanessa Gaudray-Bouju, Menel Mahamdi

Annotation tools development : Kim Gerdes, Marine Courtin, Gaël Guibon

Conversion and handling of data validation : Bruno Guillaume

Direction of data collection : Cédric Gendrot, Kim Gerdes, Marine Courtin

We would like to thank all the students who participated in this project.


## References

An article about the annotation of spoken French will soon be released (Kahane et al. 2021)


# Changelog

* 2021-11-15 v2.9
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.9
License: CC BY-SA 4.0
Includes text: yes
Genre: spoken
Lemmas: converted from manual
UPOS: converted from manual
XPOS: not available
Features: converted from manual
Relations: converted from manual
Contributors: Gerdes, Kim; Kahane, Sylvain; Mahamdi, Menel
Contributing: elsewhere
Contact: gerdes@lisn.fr
===============================================================================
</pre>

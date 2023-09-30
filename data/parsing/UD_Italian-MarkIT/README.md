# MarkIT: Italian Treebank of Marked Structures

This page refers to the dataset presented in the paper:

It is MarkIT That is New: An Italian Treebank of Marked Constructions. Teresa Paccosi, Alessio Palmero Aprosio and Sara Tonelli, To appear in Proceedings of the Eighth Italian Conference on Computational Linguistics 2022 (CLIC-it 2021)

# Summary

The MarkIT resource contains around 800 sentences extracted from students' essays manually annotated with syntactic depencendies. The treebank covers seven types of marked constructions, plus some ambiguous sentences whose syntax can be wrongly classified as marked.

# Introduction

MarkIT is a treebank of marked constructions in Italian, containing around 1,300 sentences with dependency annotation.
First we automatically annotate the sentences using Tint, then a manual fix of the errors is performed on the whole dataset.
The resource covers seven types of marked constructions plus some ambiguous sentences, whose syntax can be wrongly classified as marked.

# Acknowledgments

The selection, extraction, and annotation of the dataset have been performed by Teresa Paccosi, Alessio Palmero Aprosio, and Sara Tonelli.

# Changelog

* 2022-11-15 v2.11
  * Removed duplicated sentences
  * Fixed `nsubj:outer` relation
  * Fixed genre and sentences amount in README
  * Minor fixes
* 2022-05-15 v2.10
  * Initial release in Universal Dependencies.

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.10
License: CC BY 4.0
Includes text: yes
Genre: grammar-examples
Lemmas: automatic with corrections
UPOS: automatic with corrections
XPOS: automatic with corrections
Features: automatic with corrections
Relations: manual native
Contributors: Paccosi, Teresa; Palmero Aprosio, Alessio; Tonelli, Sara
Contributing: elsewhere
Contact: aprosio@fbk.eu
===============================================================================
</pre>

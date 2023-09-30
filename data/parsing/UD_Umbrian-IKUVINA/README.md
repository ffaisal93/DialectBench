# Summary

UD_Umbrian-IKUVINA is a dependency treebank rendering of the Iguvine tablets ([Wikipedia](https://en.wikipedia.org/wiki/Iguvine_Tablets)).
The seven bronze tablets describe religious ceremonies performed by the Umbrian people in Italy before the rise of the Roman empire.

The corpus will eventually contain all the tablets.
But as of May 2022, only tablet I is release with partial morphological analysis and partial lemmatisation. (POS tagging and Dependency trees are complete)


# Introduction

As the corpus is still under construction, so we have not decided on a standard split yet.

Specific information about the analysis can be found on the language doc page.


## Status

|Tablet | Lemma | POS  | Features | Head | Relations |
|-------|-------|------|----------|------|-----------|
|I      | Part  | Done | Part     | Done | Done      |
|II     |       |      |          |      |           |
|III    |       |      |          |      |           |
|IV     |       |      |          |      |           |
|V um   | Part  | Done | Done     | Done | Done      |
|V la   |       |      |          |      |           |
|VI     |       |      |          |      |           |
|VII    |       |      |          |      |           |



# Acknowledgments

This treebank is maintained by Mathieu Dehouck.


<!--
## References

* (citation) -->

# Changelog

* 2022-10-31 v2.11
  * added Umbrian section of Tablet V,
  * changed the relation of "anzeriates" in tablet I sentence 1 from [dep] to [acl].

* 2022-05-15 v2.10
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.10
License: CC BY-SA 4.0
Includes text: yes
Genre: nonfiction
Lemmas: manual native
UPOS: manual native
XPOS: not available
Features: manual native
Relations: manual native
Contributors: Dehouck, Mathieu
Contributing: here
Contact: mathieudehouck-ud@mailo.com
===============================================================================
</pre>

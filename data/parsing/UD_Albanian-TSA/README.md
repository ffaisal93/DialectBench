# Summary
The UD Albanian Treebank is a small treebank for Standard Albanian, developed within a project framework at Uppsala University. The data was extracted from Wikipedia.

# Introduction
The UD Treebank for Standard Albanian (TSA) is a small treebank that consists of 60 sentences corresponding to 922 tokens. The data was collected from different Wikipedia entries. This treebank was created mainly manually following the Universal Dependencies guidelines. The lemmatization was performed using the lemmatizer https://bitbucket.org/timarkh/uniparser-albanian-grammar/src/master/ developed by the Albanian National Corpus team (Maria Morozova, Alexander Rusakov, Timofey Arkhangelskiy). Tagging and Morphological Analysis were semi-automated through python scripts and corrected manually, whereas Dependency relations were assigned fully manually. We encourage any initiatives to increase the size and/or improve the overall quality of the Treebank.

# Acknowledgments
This treebank was created by Marsida Toska at Uppsala University under the supervision of Joakim Nivre.

# Changelog
* 2020-08-03 v2.8
  * Adding "case" in the morphological features of pronouns and fixing the erronous NOUN-tag of a verb ("ekziston")

* 2020-07-08 v2.7
  * Changing POS from SCONJ to PRON for "që", when introducing relative clauses
  * Fixing a minor error in the morphological analysis of "lajmet"

* 2020-05-15 v2.6
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.6
License: CC BY-SA 4.0
Includes text: yes
Genre: wiki
Lemmas: manual native
UPOS: manual native
XPOS: not available
Features: manual native
Relations: manual native
Contributors: Toska, Marsida
Contributing: here
Contact: m_a_r_c_y_94@hotmail.com
===============================================================================
</pre>

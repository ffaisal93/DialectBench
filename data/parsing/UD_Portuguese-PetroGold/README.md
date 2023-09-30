# Summary

UD_Portuguese-PetroGold is a fully revised treebank which consists of academic texts from the oil & gas domain in Brazilian Portuguese.

# Introduction

UD_Portuguese-PetroGold is a fully revised treebank which consists of academic texts from the oil & gas domain in Brazilian Portuguese processed in full: only elements such as summary, abstract, appendices and bibliographic references were excluded, as well as figures, graphs, formulas and tables. The annotation was manually revised from automatic annotation by a team of linguists from PUC-Rio (Brazil).

The corpus was created as part of the Petrolês Project (http://petroles.puc-rio.ai), a partnership between Petrobras Research and Development Center (CENPES) and Applied Computational Intelligence Lab (PUC-Rio/ICA). Petrolês aims to promote research initiatives related to Natural Language Processing and Computational Linguistics for the Portuguese Language.

# Acknowledgments

We want to thank everyone from ICA/PUC-Rio who assisted in the process of gathering the text from originally PDF files. We also want to thank Petrobras researchers and geoscientists for making the Petrolês corpus publicly available, for their technical assistance and funding.

## How to contribute

Changes should be made via pull request directly to `not-to-release/petrogold.conllu` in the `dev` branch.

## How to cite

```
@inproceedings{souza2022polishing,
  title={Polishing the gold--how much revision do we need in treebanks?},
  author={De Souza, Elvis and Freitas, Cl{\'a}udia},
  booktitle={Procedings of the Universal Dependencies Brazilian Festival},
  pages={1--11},
  year={2022}
}
```

## References

* de Souza, E., & Freitas, C. (2022, March). Polishing the gold–how much revision do we need in treebanks?. In Procedings of the Universal Dependencies Brazilian Festival (pp. 1-11). [Link](https://aclanthology.org/2022.udfestbr-1.2.pdf)

* de Souza, E., & Freitas, C. (2022, March). Still on arguments and adjuncts: the status of the indirect object and the adverbial adjunct relations in Universal Dependencies for Portuguese. In Procedings of the Universal Dependencies Brazilian Festival (pp. 1-10). [Link](https://aclanthology.org/2022.udfestbr-1.5.pdf)

* de Souza, E., Silveira, A., Cavalcanti, T., Castro, M. C., & Freitas, C. (2021, November). PetroGold–Corpus padrão ouro para o domínio do petróleo. In Anais do XIII Simpósio Brasileiro de Tecnologia da Informação e da Linguagem Humana (pp. 29-38). SBC. [Link](https://sol.sbc.org.br/index.php/stil/article/view/17781)

# Changelog

* 2023-05-15 v2.12
  * Now each file has entire documents (https://github.com/UniversalDependencies/UD_Portuguese-PetroGold/issues/3#issuecomment-1335172579)
    * `train`: 15 documents -- sentences: 8054 --> 7170 (90% --> 80%)
    * `test`: 2 documents -- sentences: 445 --> 1039 (5% --> 12%)
    * `dev`: 2 documents -- sentences: 447 --> 737 (5% --> 8%)
* 2022-11-15 v2.11
  * Initial release in Universal Dependencies.


<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.11
License: CC BY-SA 4.0
Includes text: yes
Genre: academic
Lemmas: manual native
UPOS: manual native
XPOS: not available
Features: manual native
Relations: manual native
Contributors: de Souza, Elvis; Freitas, Cláudia; Silveira, Aline; Cavalcanti, Tatiana; Castro, Maria Clara; Evelyn, Wograine
Contributing: here source
Contact: elvis.desouza99@gmail.com
===============================================================================
</pre>

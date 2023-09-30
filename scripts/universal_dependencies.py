import conllu

import datasets


_CITATION = """\
@misc{11234/1-3424,
title = {Universal Dependencies 2.7},
author = {Zeman, Daniel and Nivre, Joakim and Abrams, Mitchell and Ackermann, Elia and Aepli, No{\"e}mi and Aghaei, Hamid and Agi{\'c}, {\v Z}eljko and Ahmadi, Amir and Ahrenberg, Lars and Ajede, Chika Kennedy and Aleksandravi{\v c}i{\=u}t{\.e}, Gabriel{\.e} and Alfina, Ika and Antonsen, Lene and Aplonova, Katya and Aquino, Angelina and Aragon, Carolina and Aranzabe, Maria Jesus and Arnard{\'o}ttir, {\t H}{\'o}runn and Arutie, Gashaw and Arwidarasti, Jessica Naraiswari and Asahara, Masayuki and Ateyah, Luma and Atmaca, Furkan and Attia, Mohammed and Atutxa, Aitziber and Augustinus, Liesbeth and Badmaeva, Elena and Balasubramani, Keerthana and Ballesteros, Miguel and Banerjee, Esha and Bank, Sebastian and Barbu Mititelu, Verginica and Basmov, Victoria and Batchelor, Colin and Bauer, John and Bedir, Seyyit Talha and Bengoetxea, Kepa and Berk, G{\"o}zde and Berzak, Yevgeni and Bhat, Irshad Ahmad and Bhat, Riyaz Ahmad and Biagetti, Erica and Bick, Eckhard and Bielinskien{\.e}, Agn{\.e} and Bjarnad{\'o}ttir, Krist{\'{\i}}n and Blokland, Rogier and Bobicev, Victoria and Boizou, Lo{\"{\i}}c and Borges V{\"o}lker, Emanuel and B{\"o}rstell, Carl and Bosco, Cristina and Bouma, Gosse and Bowman, Sam and Boyd, Adriane and Brokait{\.e}, Kristina and Burchardt, Aljoscha and Candito, Marie and Caron, Bernard and Caron, Gauthier and Cavalcanti, Tatiana and Cebiroglu Eryigit, Gulsen and Cecchini, Flavio Massimiliano and Celano, Giuseppe G. A. and Ceplo, Slavomir and Cetin, Savas and Cetinoglu, Ozlem and Chalub, Fabricio and Chi, Ethan and Cho, Yongseok and Choi, Jinho and Chun, Jayeol and Cignarella, Alessandra T. and Cinkova, Silvie and Collomb, Aurelie and Coltekin, Cagr{\i} and Connor, Miriam and Courtin, Marine and Davidson, Elizabeth and de Marneffe, Marie-Catherine and de Paiva, Valeria and Derin, Mehmet Oguz and de Souza, Elvis and Diaz de Ilarraza, Arantza and Dickerson, Carly and Dinakaramani, Arawinda and Dione, Bamba and Dirix, Peter and Dobrovoljc, Kaja and Dozat, Timothy and Droganova, Kira and Dwivedi, Puneet and Eckhoff, Hanne and Eli, Marhaba and Elkahky, Ali and Ephrem, Binyam and Erina, Olga and Erjavec, Tomaz and Etienne, Aline and Evelyn, Wograine and Facundes, Sidney and Farkas, Rich{\'a}rd and Fernanda, Mar{\'{\i}}lia and Fernandez Alcalde, Hector and Foster, Jennifer and Freitas, Cl{\'a}udia and Fujita, Kazunori and Gajdosov{\'a}, Katar{\'{\i}}na and Galbraith, Daniel and Garcia, Marcos and G{\"a}rdenfors, Moa and Garza, Sebastian and Gerardi, Fabr{\'{\i}}cio Ferraz and Gerdes, Kim and Ginter, Filip and Goenaga, Iakes and Gojenola, Koldo and G{\"o}k{\i}rmak, Memduh and Goldberg, Yoav and G{\'o}mez Guinovart, Xavier and Gonz{\'a}lez Saavedra,
Berta and Grici{\=u}t{\.e}, Bernadeta and Grioni, Matias and Grobol, Lo{\"{\i}}c and Gr{\=u}z{\={\i}}tis, Normunds and Guillaume, Bruno and Guillot-Barbance, C{\'e}line and G{\"u}ng{\"o}r, Tunga and Habash, Nizar and Hafsteinsson, Hinrik and Haji{\v c}, Jan and Haji{\v c} jr., Jan and H{\"a}m{\"a}l{\"a}inen, Mika and H{\`a} M{\~y}, Linh and Han, Na-Rae and Hanifmuti, Muhammad Yudistira and Hardwick, Sam and Harris, Kim and Haug, Dag and Heinecke, Johannes and Hellwig, Oliver and Hennig, Felix and Hladk{\'a}, Barbora and Hlav{\'a}{\v c}ov{\'a}, Jaroslava and Hociung, Florinel and Hohle, Petter and Huber, Eva and Hwang, Jena and Ikeda, Takumi and Ingason, Anton Karl and Ion, Radu and Irimia, Elena and Ishola, {\d O}l{\'a}j{\'{\i}}d{\'e} and Jel{\'{\i}}nek, Tom{\'a}{\v s} and Johannsen, Anders and J{\'o}nsd{\'o}ttir, Hildur and J{\o}rgensen, Fredrik and Juutinen, Markus and K, Sarveswaran and Ka{\c s}{\i}kara, H{\"u}ner and Kaasen, Andre and Kabaeva, Nadezhda and Kahane, Sylvain and Kanayama, Hiroshi and Kanerva, Jenna and Katz, Boris and Kayadelen, Tolga and Kenney, Jessica and Kettnerov{\'a}, V{\'a}clava and Kirchner, Jesse and Klementieva, Elena and K{\"o}hn, Arne and K{\"o}ksal, Abdullatif and Kopacewicz, Kamil and Korkiakangas, Timo and Kotsyba, Natalia and Kovalevskait{\.e}, Jolanta and Krek, Simon and Krishnamurthy, Parameswari and Kwak, Sookyoung and Laippala, Veronika and Lam, Lucia and Lambertino, Lorenzo and Lando, Tatiana and Larasati, Septina Dian and Lavrentiev, Alexei and Lee, John and L{\^e} H{\`{\^o}}ng, Phương and Lenci, Alessandro and Lertpradit, Saran and Leung, Herman and Levina, Maria and Li, Cheuk Ying and Li, Josie and Li, Keying and Li, Yuan and Lim, {KyungTae} and Linden, Krister and Ljubesic, Nikola and Loginova, Olga and Luthfi, Andry and Luukko, Mikko and Lyashevskaya, Olga and Lynn, Teresa and Macketanz, Vivien and Makazhanov, Aibek and Mandl, Michael and Manning, Christopher and Manurung, Ruli and Maranduc, Catalina and Marcek, David and Marheinecke, Katrin and Mart{\'{\i}}nez Alonso, H{\'e}ctor and Martins, Andr{\'e} and Masek, Jan and Matsuda, Hiroshi and Matsumoto, Yuji and {McDonald}, Ryan and {McGuinness}, Sarah and Mendonca, Gustavo and Miekka, Niko and Mischenkova, Karina and Misirpashayeva, Margarita and Missil{\"a}, Anna and Mititelu, Catalin and Mitrofan, Maria and Miyao, Yusuke and Mojiri Foroushani, {AmirHossein} and Moloodi, Amirsaeid and Montemagni, Simonetta and More, Amir and Moreno Romero, Laura and Mori, Keiko Sophie and Mori, Shinsuke and Morioka, Tomohiko and Moro, Shigeki and Mortensen, Bjartur and Moskalevskyi, Bohdan and Muischnek, Kadri and Munro, Robert and Murawaki, Yugo and M{\"u}{\"u}risep, Kaili and Nainwani, Pinkey and Nakhl{\'e}, Mariam and Navarro Hor{\~n}iacek, Juan Ignacio and Nedoluzhko,
Anna and Ne{\v s}pore-B{\=e}rzkalne, Gunta and Nguy{\~{\^e}}n Th{\d i}, Lương and Nguy{\~{\^e}}n Th{\d i} Minh, Huy{\`{\^e}}n and Nikaido, Yoshihiro and Nikolaev, Vitaly and Nitisaroj, Rattima and Nourian, Alireza and Nurmi, Hanna and Ojala, Stina and Ojha, Atul Kr. and Ol{\'u}{\`o}kun, Ad{\'e}day{\d o}̀ and Omura, Mai and Onwuegbuzia, Emeka and Osenova, Petya and {\"O}stling, Robert and {\O}vrelid, Lilja and {\"O}zate{\c s}, {\c S}aziye Bet{\"u}l and {\"O}zg{\"u}r, Arzucan and {\"O}zt{\"u}rk Ba{\c s}aran, Balk{\i}z and Partanen, Niko and Pascual, Elena and Passarotti, Marco and Patejuk, Agnieszka and Paulino-Passos, Guilherme and Peljak-{\L}api{\'n}ska, Angelika and Peng, Siyao and Perez, Cenel-Augusto and Perkova, Natalia and Perrier, Guy and Petrov, Slav and Petrova, Daria and Phelan, Jason and Piitulainen, Jussi and Pirinen, Tommi A and Pitler, Emily and Plank, Barbara and Poibeau, Thierry and Ponomareva, Larisa and Popel, Martin and Pretkalnina, Lauma and Pr{\'e}vost, Sophie and Prokopidis, Prokopis and Przepi{\'o}rkowski, Adam and Puolakainen, Tiina and Pyysalo, Sampo and Qi, Peng and R{\"a}{\"a}bis, Andriela and Rademaker, Alexandre and Rama, Taraka and Ramasamy, Loganathan and Ramisch, Carlos and Rashel, Fam and Rasooli, Mohammad Sadegh and Ravishankar, Vinit and Real, Livy and Rebeja, Petru and Reddy, Siva and Rehm, Georg and Riabov, Ivan and Rie{\ss}ler, Michael and Rimkut{\.e}, Erika and Rinaldi, Larissa and Rituma, Laura and Rocha, Luisa and R{\"o}gnvaldsson, Eir{\'{\i}}kur and Romanenko, Mykhailo and Rosa, Rudolf and Roșca, Valentin and Rovati, Davide and Rudina, Olga and Rueter, Jack and R{\'u}narsson, Kristjan and Sadde, Shoval and Safari, Pegah and Sagot, Benoit and Sahala, Aleksi and Saleh, Shadi and Salomoni, Alessio and Samardzi{\'c}, Tanja and Samson, Stephanie and Sanguinetti, Manuela and S{\"a}rg,
Dage and Saul{\={\i}}te, Baiba and Sawanakunanon, Yanin and Scannell, Kevin and Scarlata, Salvatore and Schneider, Nathan and Schuster, Sebastian and Seddah, Djam{\'e} and Seeker, Wolfgang and Seraji, Mojgan and Shen, Mo and Shimada, Atsuko and Shirasu, Hiroyuki and Shohibussirri, Muh and Sichinava, Dmitry and Sigurðsson, Einar Freyr and Silveira, Aline and Silveira, Natalia and Simi, Maria and Simionescu, Radu and Simk{\'o}, Katalin and {\v S}imkov{\'a}, M{\'a}ria and Simov, Kiril and Skachedubova, Maria and Smith, Aaron and Soares-Bastos, Isabela and Spadine, Carolyn and Steingr{\'{\i}}msson, Stein{\t h}{\'o}r and Stella, Antonio and Straka, Milan and Strickland, Emmett and Strnadov{\'a}, Jana and Suhr, Alane and Sulestio, Yogi Lesmana and Sulubacak, Umut and Suzuki, Shingo and Sz{\'a}nt{\'o}, Zsolt and Taji, Dima and Takahashi, Yuta and Tamburini, Fabio and Tan, Mary Ann C. and Tanaka, Takaaki and Tella, Samson and Tellier, Isabelle and Thomas, Guillaume and Torga, Liisi and Toska, Marsida and Trosterud, Trond and Trukhina, Anna and Tsarfaty, Reut and T{\"u}rk, Utku and Tyers, Francis and Uematsu, Sumire and Untilov, Roman and Uresov{\'a}, Zdenka and Uria, Larraitz and Uszkoreit, Hans and Utka, Andrius and Vajjala, Sowmya and van Niekerk, Daniel and van Noord, Gertjan and Varga, Viktor and Villemonte de la Clergerie, Eric and Vincze, Veronika and Wakasa, Aya and Wallenberg, Joel C. and Wallin, Lars and Walsh, Abigail and Wang, Jing Xian and Washington, Jonathan North and Wendt, Maximilan and Widmer, Paul and Williams, Seyi and Wir{\'e}n, Mats and Wittern, Christian and Woldemariam, Tsegay and Wong, Tak-sum and Wr{\'o}blewska, Alina and Yako, Mary and Yamashita, Kayo and Yamazaki, Naoki and Yan, Chunxiao and Yasuoka, Koichi and Yavrumyan, Marat M. and Yu, Zhuoran and Zabokrtsk{\'y}, Zdenek and Zahra, Shorouq and Zeldes, Amir and Zhu, Hanzhi and Zhuravleva, Anna},
url = {http://hdl.handle.net/11234/1-3424},
note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
copyright = {Licence Universal Dependencies v2.7},
year = {2020} }
"""  # noqa: W605

_DESCRIPTION = """\
Universal Dependencies is a project that seeks to develop cross-linguistically consistent treebank annotation for many languages, with the goal of facilitating multilingual parser development, cross-lingual learning, and parsing research from a language typology perspective. The annotation scheme is based on (universal) Stanford dependencies (de Marneffe et al., 2006, 2008, 2014), Google universal part-of-speech tags (Petrov et al., 2012), and the Interset interlingua for morphosyntactic tagsets (Zeman, 2008).
"""

_NAMES = ["UD_Armenian-ArmTDP",
         "UD_Gheg-GPS",
         "UD_Norwegian-Nynorsk",
         "UD_Albanian-TSA",
         "UD_Italian-PUD",
         "UD_Portuguese-Bosque",
         "UD_Italian-PoSTWITA",
         "UD_Old_French-SRCMF",
         "UD_Swiss_German-UZH",
         "UD_North_Sami-Giella",
         "UD_Norwegian-Bokmaal",
         "UD_French-ParisStories",
         "UD_German-LIT",
         "UD_Italian-MarkIT",
         "UD_Chinese-GSDSimp",
         "UD_Chinese-HK",
         "UD_Umbrian-IKUVINA",
         "UD_Guarani-OldTuDeT",
         "UD_Low_Saxon-LSDC",
         "UD_French-Rhapsodie",
         "UD_Mbya_Guarani-Thomas",
         "UD_French-ParTUT",
         "UD_Classical_Chinese-Kyoto",
         "UD_Norwegian-NynorskLIA",
         "UD_Komi_Permyak-UH",
         "UD_Chinese-CFL",
         "UD_Arabic-NYUAD",
         "UD_Portuguese-PUD",
         "UD_Portuguese-PetroGold",
         "UD_Italian-TWITTIRO",
         "UD_Neapolitan-RB",
         "UD_Turkish_German-SAGT",
         "UD_Chinese-PUD",
         "UD_Maghrebi_Arabic_French-Arabizi",
         "UD_Portuguese-CINTIL",
         "UD_French-PUD",
         "UD_South_Levantine_Arabic-MADAR",
         "UD_Komi_Zyrian-Lattice",
         "UD_Frisian_Dutch-Fame",
         "UD_Skolt_Sami-Giellagas",
         "UD_Mbya_Guarani-Dooley",
         "UD_Ligurian-GLT",
         "UD_Dutch-Alpino",
         "UD_Arabic-PUD",
         "UD_Komi_Zyrian-IKDP",
         "UD_Western_Armenian-ArmTDP",
         "UD_Portuguese-GSD",
         "singlish",
         "UD_Arabic-PADT",
         "TwitterAAE",
         "UD_English-EWT"]

_DESCRIPTIONS = {"UD_Armenian-ArmTDP": "xx",
                 "UD_Gheg-GPS": "xx",
                 "UD_Norwegian-Nynorsk": "xx",
                 "UD_Albanian-TSA": "xx",
                 "UD_Italian-PUD": "xx",
                 "UD_Portuguese-Bosque": "xx",
                 "UD_Italian-PoSTWITA": "xx",
                 "UD_Old_French-SRCMF": "xx",
                 "UD_Swiss_German-UZH": "xx",
                 "UD_North_Sami-Giella": "xx",
                 "UD_Norwegian-Bokmaal": "xx",
                 "UD_French-ParisStories": "xx",
                 "UD_German-LIT": "xx",
                 "UD_Italian-MarkIT": "xx",
                 "UD_Chinese-GSDSimp": "xx",
                 "UD_Chinese-HK": "xx",
                 "UD_Umbrian-IKUVINA": "xx",
                 "UD_Guarani-OldTuDeT": "xx",
                 "UD_Low_Saxon-LSDC": "xx",
                 "UD_French-Rhapsodie": "xx",
                 "UD_Mbya_Guarani-Thomas": "xx",
                 "UD_French-ParTUT": "xx",
                 "UD_Classical_Chinese-Kyoto": "xx",
                 "UD_Norwegian-NynorskLIA": "xx",
                 "UD_Komi_Permyak-UH": "xx",
                 "UD_Chinese-CFL": "xx",
                 "UD_Arabic-NYUAD": "xx",
                 "UD_Portuguese-PUD": "xx",
                 "UD_Portuguese-PetroGold": "xx",
                 "UD_Italian-TWITTIRO": "xx",
                 "UD_Neapolitan-RB": "xx",
                 "UD_Turkish_German-SAGT": "xx",
                 "UD_Chinese-PUD": "xx",
                 "UD_Maghrebi_Arabic_French-Arabizi": "xx",
                 "UD_Portuguese-CINTIL": "xx",
                 "UD_French-PUD": "xx",
                 "UD_South_Levantine_Arabic-MADAR": "xx",
                 "UD_Komi_Zyrian-Lattice": "xx",
                 "UD_Frisian_Dutch-Fame": "xx",
                 "UD_Skolt_Sami-Giellagas": "xx",
                 "UD_Mbya_Guarani-Dooley": "xx",
                 "UD_Ligurian-GLT": "xx",
                 "UD_Dutch-Alpino": "xx",
                 "UD_Arabic-PUD": "xx",
                 "UD_Komi_Zyrian-IKDP": "xx",
                 "UD_Western_Armenian-ArmTDP": "xx",
                 "UD_Portuguese-GSD": "xx",
                 "singlish": "xx",
                 "UD_Arabic-PADT": "xx",
                 "TwitterAAE": "xx",
                 "UD_English-EWT": "xx"}

_PREFIX = "../data/parsing/"
_UD_DATASETS = {"UD_Armenian-ArmTDP": {
                "train": "UD_Armenian-ArmTDP/hy_armtdp-ud-train.conllu",
                "test": "UD_Armenian-ArmTDP/hy_armtdp-ud-test.conllu",
                "dev": "UD_Armenian-ArmTDP/hy_armtdp-ud-dev.conllu"
                },
             "UD_Gheg-GPS": {
                "test": "UD_Gheg-GPS/aln_gps-ud-test.conllu"},
             "UD_Norwegian-Nynorsk": {
                "test": "UD_Norwegian-Nynorsk/no_nynorsk-ud-test.conllu",
                "dev": "UD_Norwegian-Nynorsk/no_nynorsk-ud-dev.conllu",
                "train": "UD_Norwegian-Nynorsk/no_nynorsk-ud-train.conllu"},
             "UD_Albanian-TSA": {
                "test": "UD_Albanian-TSA/sq_tsa-ud-test.conllu"},
             "UD_Italian-PUD": {
                "test": "UD_Italian-PUD/it_pud-ud-test.conllu"},
             "UD_Portuguese-Bosque": {
                "test": "UD_Portuguese-Bosque/pt_bosque-ud-test.conllu",
                "dev": "UD_Portuguese-Bosque/pt_bosque-ud-dev.conllu",
                "train": "UD_Portuguese-Bosque/pt_bosque-ud-train.conllu"},
             "UD_Italian-PoSTWITA": {
                "dev": "UD_Italian-PoSTWITA/it_postwita-ud-dev.conllu",
                "train": "UD_Italian-PoSTWITA/it_postwita-ud-train.conllu",
                "test": "UD_Italian-PoSTWITA/it_postwita-ud-test.conllu"},
             "UD_Old_French-SRCMF": {
                "train": "UD_Old_French-SRCMF/fro_srcmf-ud-train.conllu",
                "test": "UD_Old_French-SRCMF/fro_srcmf-ud-test.conllu",
                "dev": "UD_Old_French-SRCMF/fro_srcmf-ud-dev.conllu"},
             "UD_Swiss_German-UZH": {
                "test": "UD_Swiss_German-UZH/gsw_uzh-ud-test.conllu"},
             "UD_North_Sami-Giella": {
                "train": "UD_North_Sami-Giella/sme_giella-ud-train.conllu",
                "test": "UD_North_Sami-Giella/sme_giella-ud-test.conllu"},
             "UD_Norwegian-Bokmaal": {
                "dev": "UD_Norwegian-Bokmaal/no_bokmaal-ud-dev.conllu",
                "test": "UD_Norwegian-Bokmaal/no_bokmaal-ud-test.conllu",
                "train": "UD_Norwegian-Bokmaal/no_bokmaal-ud-train.conllu"},
             "UD_French-ParisStories": {
                "train": "UD_French-ParisStories/fr_parisstories-ud-train.conllu",
                "test": "UD_French-ParisStories/fr_parisstories-ud-test.conllu",
                "dev": "UD_French-ParisStories/fr_parisstories-ud-dev.conllu"},
             "UD_German-LIT": {
                "test": "UD_German-LIT/de_lit-ud-test.conllu"},
             "UD_Italian-MarkIT": {
                "train": "UD_Italian-MarkIT/it_markit-ud-train.conllu",
                "dev": "UD_Italian-MarkIT/it_markit-ud-dev.conllu",
                "test": "UD_Italian-MarkIT/it_markit-ud-test.conllu"},
             "UD_Chinese-GSDSimp": {
                "train": "UD_Chinese-GSDSimp/zh_gsdsimp-ud-train.conllu",
                "test": "UD_Chinese-GSDSimp/zh_gsdsimp-ud-test.conllu",
                "dev": "UD_Chinese-GSDSimp/zh_gsdsimp-ud-dev.conllu"},
             "UD_Chinese-HK": {
                "test": "UD_Chinese-HK/zh_hk-ud-test.conllu"},
             "UD_Umbrian-IKUVINA": {
                "test": "UD_Umbrian-IKUVINA/xum_ikuvina-ud-test.conllu"},
             "UD_Guarani-OldTuDeT": {
                "test": "UD_Guarani-OldTuDeT/gn_oldtudet-ud-test.conllu"},
             "UD_Low_Saxon-LSDC": {
                "test": "UD_Low_Saxon-LSDC/nds_lsdc-ud-test.conllu"},
             "UD_French-Rhapsodie": {
                "dev": "UD_French-Rhapsodie/fr_rhapsodie-ud-dev.conllu",
                "train": "UD_French-Rhapsodie/fr_rhapsodie-ud-train.conllu",
                "test": "UD_French-Rhapsodie/fr_rhapsodie-ud-test.conllu"},
             "UD_Mbya_Guarani-Thomas": {
                "test": "UD_Mbya_Guarani-Thomas/gun_thomas-ud-test.conllu"},
             "UD_French-ParTUT": {
                "train": "UD_French-ParTUT/fr_partut-ud-train.conllu",
                "dev": "UD_French-ParTUT/fr_partut-ud-dev.conllu",
                "test": "UD_French-ParTUT/fr_partut-ud-test.conllu"},
             "UD_Classical_Chinese-Kyoto": {
                "dev": "UD_Classical_Chinese-Kyoto/lzh_kyoto-ud-dev.conllu",
                "train": "UD_Classical_Chinese-Kyoto/lzh_kyoto-ud-train.conllu",
                "test": "UD_Classical_Chinese-Kyoto/lzh_kyoto-ud-test.conllu"},
             "UD_Norwegian-NynorskLIA": {
                "train": "UD_Norwegian-NynorskLIA/no_nynorsklia-ud-train.conllu",
                "dev": "UD_Norwegian-NynorskLIA/no_nynorsklia-ud-dev.conllu",
                "test": "UD_Norwegian-NynorskLIA/no_nynorsklia-ud-test.conllu"},
             "UD_Komi_Permyak-UH": {
                "test": "UD_Komi_Permyak-UH/koi_uh-ud-test.conllu"},
             "UD_Chinese-CFL": {
                "test": "UD_Chinese-CFL/zh_cfl-ud-test.conllu"},
             "UD_Arabic-NYUAD": {
                "train": "UD_Arabic-NYUAD/ar_nyuad-ud-train.conllu",
                "dev": "UD_Arabic-NYUAD/ar_nyuad-ud-dev.conllu",
                "test": "UD_Arabic-NYUAD/ar_nyuad-ud-test.conllu"},
             "UD_Portuguese-PUD": {
                "test": "UD_Portuguese-PUD/pt_pud-ud-test.conllu"},
             "UD_Portuguese-PetroGold": {
                "train": "UD_Portuguese-PetroGold/pt_petrogold-ud-train.conllu",
                "test": "UD_Portuguese-PetroGold/pt_petrogold-ud-test.conllu",
                "dev": "UD_Portuguese-PetroGold/pt_petrogold-ud-dev.conllu"},
             "UD_Italian-TWITTIRO": {
                "test": "UD_Italian-TWITTIRO/it_twittiro-ud-test.conllu",
                "train": "UD_Italian-TWITTIRO/it_twittiro-ud-train.conllu",
                "dev": "UD_Italian-TWITTIRO/it_twittiro-ud-dev.conllu"},
             "UD_Neapolitan-RB": {
                "test": "UD_Neapolitan-RB/nap_rb-ud-test.conllu"},
             "UD_Turkish_German-SAGT": {
                "test": "UD_Turkish_German-SAGT/qtd_sagt-ud-test.conllu",
                "dev": "UD_Turkish_German-SAGT/qtd_sagt-ud-dev.conllu",
                "train": "UD_Turkish_German-SAGT/qtd_sagt-ud-train.conllu"},
             "UD_Chinese-PUD": {
                "test": "UD_Chinese-PUD/zh_pud-ud-test.conllu"},
             "UD_Maghrebi_Arabic_French-Arabizi": {
                "dev": "UD_Maghrebi_Arabic_French-Arabizi/qaf_arabizi-ud-dev.conllu",
                "train": "UD_Maghrebi_Arabic_French-Arabizi/qaf_arabizi-ud-train.conllu",
                "test": "UD_Maghrebi_Arabic_French-Arabizi/qaf_arabizi-ud-test.conllu"},
             "UD_Portuguese-CINTIL": {
                "test": "UD_Portuguese-CINTIL/pt_cintil-ud-test.conllu",
                "train": "UD_Portuguese-CINTIL/pt_cintil-ud-train.conllu",
                "dev": "UD_Portuguese-CINTIL/pt_cintil-ud-dev.conllu"},
             "UD_French-PUD": {
                "test": "UD_French-PUD/fr_pud-ud-test.conllu"},
             "UD_South_Levantine_Arabic-MADAR": {
                "test": "UD_South_Levantine_Arabic-MADAR/ajp_madar-ud-test.conllu"},
             "UD_Komi_Zyrian-Lattice": {
                "test": "UD_Komi_Zyrian-Lattice/kpv_lattice-ud-test.conllu"},
             "UD_Frisian_Dutch-Fame": {
                "test": "UD_Frisian_Dutch-Fame/qfn_fame-ud-test.conllu"},
             "UD_Skolt_Sami-Giellagas": {
                "test": "UD_Skolt_Sami-Giellagas/sms_giellagas-ud-test.conllu"},
             "UD_Mbya_Guarani-Dooley": {
                "test": "UD_Mbya_Guarani-Dooley/gun_dooley-ud-test.conllu"},
             "UD_Ligurian-GLT": {
                "train": "UD_Ligurian-GLT/lij_glt-ud-train.conllu",
                "test": "UD_Ligurian-GLT/lij_glt-ud-test.conllu"},
             "UD_Dutch-Alpino": {
                "train": "UD_Dutch-Alpino/nl_alpino-ud-train.conllu",
                "test": "UD_Dutch-Alpino/nl_alpino-ud-test.conllu",
                "dev": "UD_Dutch-Alpino/nl_alpino-ud-dev.conllu"},
             "UD_Arabic-PUD": {
                "test": "UD_Arabic-PUD/ar_pud-ud-test.conllu"},
             "UD_Komi_Zyrian-IKDP": {
                "test": "UD_Komi_Zyrian-IKDP/kpv_ikdp-ud-test.conllu"},
             "UD_Western_Armenian-ArmTDP": {
                "test": "UD_Western_Armenian-ArmTDP/hyw_armtdp-ud-test.conllu",
                "dev": "UD_Western_Armenian-ArmTDP/hyw_armtdp-ud-dev.conllu",
                "train": "UD_Western_Armenian-ArmTDP/hyw_armtdp-ud-train.conllu"},
             "UD_Portuguese-GSD": {
                "dev": "UD_Portuguese-GSD/pt_gsd-ud-dev.conllu",
                "train": "UD_Portuguese-GSD/pt_gsd-ud-train.conllu",
                "test": "UD_Portuguese-GSD/pt_gsd-ud-test.conllu"},
             "singlish": {
                "dev": "singlish/dev.conllu",
                "test": "singlish/test.conllu",
                "train": "singlish/train.conllu"
             },
             "UD_Arabic-PADT": {
                "dev": "UD_Arabic-PADT/ar_padt-ud-dev.conllu",
                "train": "UD_Arabic-PADT/ar_padt-ud-train.conllu",
                "test": "UD_Arabic-PADT/ar_padt-ud-test.conllu"},
             "TwitterAAE": {
                "test": "TwitterAAE/all500_gold.conllu"
             },
            "UD_English-EWT": {
                "dev": "UD_English-EWT/en_ewt-ud-dev.conllu",
                "test": "UD_English-EWT/en_ewt-ud-test.conllu",
                "train": "UD_English-EWT/en_ewt-ud-train.conllu"
            }
             }


class UniversaldependenciesConfig(datasets.BuilderConfig):
    """BuilderConfig for Universal dependencies"""

    def __init__(self, data_url, **kwargs):
        super(UniversaldependenciesConfig, self).__init__(version=datasets.Version("2.7.0", ""), **kwargs)

        self.data_url = data_url


class UniversalDependencies(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("2.7.0")
    BUILDER_CONFIGS = [
        UniversaldependenciesConfig(
            name=name,
            description=_DESCRIPTIONS[name],
            data_url="../data/parsing/" + _UD_DATASETS[name]["test"].split("/")[0],
        )
        for name in _NAMES
    ]
    BUILDER_CONFIG_CLASS = UniversaldependenciesConfig

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "idx": datasets.Value("string"),
                    "text": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "lemmas": datasets.Sequence(datasets.Value("string")),
                    "upos": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "NOUN",
                                "PUNCT",
                                "ADP",
                                "NUM",
                                "SYM",
                                "SCONJ",
                                "ADJ",
                                "PART",
                                "DET",
                                "CCONJ",
                                "PROPN",
                                "PRON",
                                "X",
                                "_",
                                "ADV",
                                "INTJ",
                                "VERB",
                                "AUX",
                                "CONJ",
                                "root"
                            ]
                        )
                    ),
                    "xpos": datasets.Sequence(datasets.Value("string")),
                    "feats": datasets.Sequence(datasets.Value("string")),
                    "head": datasets.Sequence(datasets.Value("string")),
                    "deprel": datasets.Sequence(datasets.Value("string")),
                    "deps": datasets.Sequence(datasets.Value("string")),
                    "misc": datasets.Sequence(datasets.Value("string")),
                }
            ),
            supervised_keys=None,
            homepage="https://universaldependencies.org/",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls_to_download = {}
        for split, address in _UD_DATASETS[self.config.name].items():
            urls_to_download[split] = []
            if isinstance(address, list):
                for add in address:
                    urls_to_download[split].append(_PREFIX + add)
            else:
                urls_to_download[split].append(_PREFIX + address)

        downloaded_files = dl_manager.download_and_extract(urls_to_download)
        splits = []

        if "train" in downloaded_files:
            splits.append(
                datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]})
            )

        if "dev" in downloaded_files:
            splits.append(
                datasets.SplitGenerator(
                    name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}
                )
            )

        if "test" in downloaded_files:
            splits.append(
                datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]})
            )

        return splits

    def _generate_examples(self, filepath):
        id = 0
        for path in filepath:
            with open(path, "r", encoding="utf-8") as data_file:
                tokenlist = list(conllu.parse_incr(data_file))
                for sent in tokenlist:
                    if "sent_id" in sent.metadata:
                        idx = sent.metadata["sent_id"]
                    else:
                        idx = id

                    tokens = [token["form"] for token in sent]

                    if "text" in sent.metadata:
                        txt = sent.metadata["text"]
                    else:
                        txt = " ".join(tokens)

                    yield id, {
                        "idx": str(idx),
                        "text": txt,
                        "tokens": [token["form"] for token in sent],
                        "lemmas": [token["lemma"] for token in sent],
                        "upos": [token["upos"] for token in sent],
                        "xpos": [token["xpos"] for token in sent],
                        "feats": [str(token["feats"]) for token in sent],
                        "head": [str(token["head"]) for token in sent],
                        "deprel": [str(token["deprel"]) for token in sent],
                        "deps": [str(token["deps"]) for token in sent],
                        "misc": [str(token["misc"]) for token in sent],
                    }
                    id += 1
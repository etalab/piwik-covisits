# Recommendations data.gouv.fr à partir des visites Matomo

Ce dépôt permet de générer des recommendations sur data.gouv.fr à l'aide du plugin [udata-recommendations](https://github.com/opendatateam/udata-recommendations). Les recommendations sont tirées des visites de data.gouv.fr [enregistrées par Matomo](https://stats.data.gouv.fr/index.php?module=CoreHome&action=index&idSite=109).

🤖 Les recommendations sont calculées automatiquement tous les jours, par rapport au visite des 30 derniers jours.

## URL

Les recommendations de ce dépôt sont disponibles en JSON à l'adresse https://etalab.github.io/piwik-covisits/recommendations.json

## Usage

```
$ python fetch.py
$ python aggregate.py
$ python compute.py
$ python top50.py
$ python generate.py
```

```
$ python fetch.py
2018-03-12 : done
2018-03-13 : done
2018-03-14 : done
2018-03-15 : done
2018-03-16 : done
2018-03-17 : done
2018-03-18 : done
2018-03-19 : done
2018-03-20 : done
2018-03-21 : done
2018-03-22 : done
2018-03-23 : done
2018-03-24 : done
2018-03-25 : done
2018-03-26 : done
2018-03-27 : done
2018-03-28 : done
2018-03-29 : done
2018-03-30 : done
2018-03-31 : done
2018-04-01 : done
2018-04-02 : done
2018-04-03 : done
2018-04-04 : done
2018-04-05 : done
2018-04-06 : done
2018-04-07 : done
2018-04-08 : done
2018-04-09 : done
2018-04-10 : done
2018-04-11 : done
2018-04-12 : done

$ python aggregate.py
13190
10833
5803
12688
11799
6278
12759
12820
12046
12352
4722
12880
10158
5611
12272
16253
4655
9849
12319
10647
5351
12931
12443
1587
5360
13467
4436
11732
12060
5825
13277
12055

$ python compute.py
visits/2018-03-20.json
visits/2018-03-23.json
visits/2018-03-25.json
visits/2018-04-03.json
visits/2018-03-14.json
visits/2018-03-18.json
visits/2018-03-21.json
visits/2018-03-13.json
visits/2018-03-15.json
visits/2018-03-28.json
visits/2018-04-07.json
visits/2018-03-27.json
visits/2018-03-30.json
visits/2018-03-17.json
visits/2018-04-04.json
visits/2018-04-12.json
visits/2018-03-31.json
visits/2018-04-06.json
visits/2018-03-22.json
visits/2018-03-16.json
visits/2018-04-08.json
visits/2018-04-10.json
visits/2018-04-09.json
visits/2018-03-12.json
visits/2018-03-24.json
visits/2018-03-26.json
visits/2018-04-01.json
visits/2018-04-11.json
visits/2018-03-29.json
visits/2018-04-02.json
visits/2018-03-19.json
visits/2018-04-05.json
14321
168042

$ python generate.py

```

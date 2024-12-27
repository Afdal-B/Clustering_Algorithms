# K-means and Bisective K-Means for clustering

Ce projet implémente deux algorithmes de clustering : K-Means et Bisective K-Means.

## K-Means

L'algorithme K-Means partitionne un ensemble de données en `k` clusters. Il fonctionne en répétant les étapes suivantes jusqu'à convergence :

1. Initialisation des centres de clusters.
2. Attribution de chaque point de données au centre de cluster le plus proche.
3. Mise à jour des centres de clusters en calculant la moyenne des points de données attribués à chaque cluster.

## Bisective K-Means

L'algorithme Bisective K-Means est une variante de K-Means qui fonctionne de manière hiérarchique. Il commence avec un seul cluster contenant toutes les données, puis il divise récursivement les clusters jusqu'à obtenir `k` clusters. À chaque étape, le cluster avec la plus grande distance paire maximale est sélectionné pour être divisé en deux sous-clusters en utilisant l'algorithme K-Means.

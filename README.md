# K-means and Bisective K-Means for clustering

This project implements two clustering algorithms: K-Means and Bisective K-Means.

## K-Means

The K-Means algorithm partitions a dataset into `k` clusters. It operates by repeating the following steps until convergence:

1. Initialize cluster centers.
2. Assign each data point to the nearest cluster center.
3. Update cluster centers by calculating the mean of the data points assigned to each cluster.

## Bisective K-Means

The Bisective K-Means algorithm is a hierarchical variant of K-Means. It starts with a single cluster containing all data, then recursively divides clusters until `k` clusters are obtained. At each step, the cluster with the largest maximum pairwise distance is selected to be split into two sub-clusters using the K-Means algorithm.

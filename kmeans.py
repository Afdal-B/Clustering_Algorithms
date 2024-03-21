import numpy as np

import numpy
import pandas

from clustering_resources import *

RandomNumGen.set_seed(2304491)


def kmeans(Dn, k, num_iter=100, num_restart=100, centers=None, random=True):
    clabelArray = []
    restart_count = 0
    restart = False
    while (restart_count < num_restart):
        # initialize representatives
        if random:
            centers = sample_domain(k, Dn)
        for _ in range(num_iter):
            # We compute the distances between datapoints and centers
            distances = L2_distance(Dn, centers)
            # for each row in distance, we get the index of the minimum distance
            clabelArray = numpy.argmin(distances, axis=1)
            # We save a copy of our current centers
            previous_centers = numpy.copy(centers)
            for i in range(0, k):
                # We get the cluster i
                cluster = [Dn[id, :] for id in numpy.where(numpy.array(clabelArray) == i)[0]]
                if (len(cluster) <= 0):
                    restart_count += 1
                    restart = True
                    break
                else:
                    # if the cluster is not empty, we compute the mean
                    restart=False
                    mean = numpy.mean(cluster, axis=0)
                    centers[i] = mean

            if restart:
                break
            elif numpy.allclose(numpy.array(previous_centers), numpy.array(centers)):
                return clabelArray



    return None

if __name__ == "__main__":
    dataset=[[0.282,0.562],
            [0.295,0.593],
            [0.323,0.467],
            [0.377,0.655],
            [0.418,0.626],
            [0.106,0.539],
            [0.119,0.426],
            [0.198,0.301],
            [0.196,0.503],
            [0.331,0.586],
            [0.053,0.820],
            [0.099,0.874],
            [0.119,0.884],
            [0.113,0.793],
            [0.137,0.866],
            [0.165,0.850]]
    dataset=numpy.array(dataset)
    centers = numpy.array([[0.230, 0.560], [0.150, 0.740], [0.120, 0.860]], dtype=np.float32)
    # We try kmeans with centers we choose
    # labels=kmeans(dtf,k=3,random=False,centers=centers)
    # print(labels)
    # print(numpy.bincount(labels))
    labels = kmeans(dataset, k=3, random=True)
    print(labels)
    print(numpy.bincount(labels+1))

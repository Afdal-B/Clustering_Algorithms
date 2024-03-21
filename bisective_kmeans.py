from kmeans import *
#Task 2
# A function du compute the maximum pairwise distance in a cluster
def max_pairwise_distance(cluster):
    pair_dist=L2_distance(cluster,cluster)
    return numpy.max(pair_dist)

#A function to put label on datapoint
def to_label(clusters,k,Dn):
    list=[-1]*Dn.shape[0]
    for i in range(k):
        for datapoint in clusters[i].tolist():
            indexlist=(Dn.tolist()).index(datapoint)
            list[indexlist]=i
    return list



def bisec_kmeans(Dn,k):
    #We initialize our clusters list with the dataset
    clusters=[Dn]
    #We repeat the process untill we have k clusters
    while len(clusters) < k:
        # we get the id of the cluster with the maximum maximum pairwise distance
        maxid=0
        for i in range(1,len(clusters)):
            if(max_pairwise_distance(clusters[i]) > max_pairwise_distance(clusters[maxid])):
                maxid=i
        #We apply kmeans on this cluster and we delete it from clusters
        clabel = kmeans(clusters.pop(maxid), k=2)
        cluster1= numpy.array([Dn[id, :] for id in numpy.where(numpy.array(clabel) == 0 )[0]])
        cluster2= numpy.array([Dn[id, :] for id in numpy.where(numpy.array(clabel) == 1 )[0]])
        #We add the two new clusters to our list of clusters
        clusters.extend([cluster1,cluster2])
    return numpy.array(to_label(clusters,k,Dn))

if __name__=="__main__":
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
    #test
    dataset=numpy.array(dataset)
    m=max_pairwise_distance(dataset)
    x=bisec_kmeans(dataset,3)
    print(x)
    print(numpy.bincount(x+1))
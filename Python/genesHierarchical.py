import numpy as np
from sklearn.cluster import AgglomerativeClustering
import collections
import sys
from sklearn import metrics
from sklearn.externals import joblib
from sklearn.metrics import davies_bouldin_score

def main():
    if(len(sys.argv) != 2):
        print("Usage: python genesHierarchical.py in")
        exit(1)
    columns = [i for i in range(1,6483)]
    data = np.loadtxt(sys.argv[1],delimiter=",",skiprows=1,usecols=columns)
    cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage="average")
    cluster.fit_predict(data)
    clusters = cluster.labels_
    with open("clustersHierarchical.txt","w") as f:
        for i in clusters:
            f.write(str(int(i))+"\n")
    clustersNum = collections.Counter(clusters)
    for x in clustersNum:
        print("Cid: {:>5}".format(x)," Size: {:>5}".format(clustersNum[x]))
    joblib.dump(cluster, "genesHierarchical.sav")

    quality = davies_bouldin_score(data, clusters)
    print(quality)
    
if __name__ == '__main__':
    main()





from sklearn.cluster import KMeans
import collections
import numpy as np
import sys
from sklearn.externals import joblib
from sklearn import metrics
from sklearn.metrics import davies_bouldin_score

def main():
    if(len(sys.argv) != 2):
        print("Usage: python cellsKmeans.py in")
        exit(1)
    data = np.loadtxt(sys.argv[1])
    kmeans_model = KMeans(n_clusters=15, random_state=1).fit(data)
    clusters = kmeans_model.labels_
    clustersNum = collections.Counter(clusters)
    for x in clustersNum:
        print("Cid: {:>5}".format(x)," Size: {:>5}".format(clustersNum[x]))
    joblib.dump(kmeans_model, 'celssKmeansModel.sav')

    quality = davies_bouldin_score(data, clusters)
    print(quality)



if __name__ == '__main__':
    main()



import numpy as np
from sklearn.cluster import AgglomerativeClustering
import collections
import sys
from sklearn.externals import joblib
from sklearn import metrics
from sklearn.metrics import davies_bouldin_score

def main():
    if(len(sys.argv) != 2):
        print("Usage: python hierarchicalCells.py in")
        exit(1)
    data = np.loadtxt(sys.argv[1])
    cluster = AgglomerativeClustering(n_clusters=8, affinity='euclidean', linkage='average')
    cluster.fit_predict(data)
    clustersNum = collections.Counter(cluster.labels_)
    for x in clustersNum:
        print("Cid: {:>5}".format(x)," Size: {:>5}".format(clustersNum[x]))
    joblib.dump(cluster, 'hierarchicalCellsModel.sav')



if __name__ == '__main__':
    main()





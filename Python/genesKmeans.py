import sys
import numpy as np 
import collections
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.metrics import davies_bouldin_score


def main():
	if len(sys.argv) != 2:
		print("Usage: python genesKmeans.py inputFile")
		exit(1)

	col = [x for x in range(1, 6483)]
	data = np.loadtxt(sys.argv[1], delimiter = ",", usecols = col, skiprows = 1)
	kmeans_clustering = KMeans(n_clusters = 15, random_state = 1).fit(data)

	clusters = kmeans_clustering.labels_
	with open("clustersKmeans.txt", "w") as file:
		for i in clusters:
			file.write(str(int(i)) + "\n")

	numberOfClusters = collections.Counter(clusters)
	for x in numberOfClusters:
		print("C", x, "  size: ", numberOfClusters[x])

	joblib.dump(kmeans_clustering, "genesKmeans.sav")

	quality = davies_bouldin_score(data, clusters)
	print(quality)


if __name__ == "__main__":
	main()



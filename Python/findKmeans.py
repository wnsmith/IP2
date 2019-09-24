import sys
import numpy as np 
import pandas as pd 
from sklearn.cluster import KMeans

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 findKmeans.py inputFile")
		exit(1)

	col = [x for x in range(1, 6483)]
	data = np.loadtxt(sys.argv[1], delimiter = ",", usecols = col, skiprows = 1)

	for k in range (1, 21):
		kmeans_clustering = KMeans(n_clusters = k, random_state = 1).fit(data)
		iterate = kmeans_clustering.inertia_

		print("k: ", k, " ------ ", iterate)


if __name__ == "__main__":
	main()



	
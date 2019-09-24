import numpy as np 
import sys
import collections
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn import metrics
from sklearn.metrics import davies_bouldin_score

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 genesDbscan inputFile")
		exit(1)

	col = [x for x in range(1, 6484)]

	data = np.loadtxt(sys.argv[1], delimiter = ",", usecols = col, skiprows = 1)
	scaler = StandardScaler()
	scaler.fit(data)

	data = scaler.transform(data)
	
	z = DBSCAN(eps = 0.02, min_samples = 2)
	z.fit(data)

	clusters = z.labels_

	with open("dbscanCl.txt", "w") as file:
		for i in clusters:
			file.write(str(int(i)) + "\n")
	numberOfClusters = collections.Counter(clusters)
	for x in numberOfClusters:
		if x == -1:
			print("Outliers: ", numberOfClusters[x])
		else:
			print("CLUSTER", x, " -- SIZE: ", numberOfClusters[x])	
	joblib.dump(z, "genesDbscanModel.sav")


 

if __name__ == "__main__":
	main()




 
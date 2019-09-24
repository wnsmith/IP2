from minisom import MiniSom
import matplotlib.pyplot as plt
import numpy as np
import sys
from sklearn.externals import joblib

def main():
    if(len(sys.argv) != 2):
        print("Usage: python genesSom.py input")
        exit(1)
    columns = [i for i in range(1,6483)]
    X = np.loadtxt(sys.argv[1],delimiter=",",skiprows=1,usecols=columns)
    mdl = MiniSom(26, 26, 6482)
    #mdl.random_weights_init(X)
    mdl.pca_weights_init(X)
    mdl.train_batch(X, 100)
    joblib.dump(mdl, '"genesSomModel.sav')

    plt.pcolor(mdl.distance_map().T)
    plt.show()

if __name__ == '__main__':
	main()






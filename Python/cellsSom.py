from minisom import MiniSom
import matplotlib.pyplot as plt
import numpy as np
import sys
from sklearn.externals import joblib

def main():
    if(len(sys.argv) != 2):
        print("Usage: python cellsSom.py inputFile")
        exit(1)
    X = np.loadtxt(sys.argv[1])
    mdl = MiniSom(20, 20, 10561)
    mdl.random_weights_init(X)
    mdl.train_batch(X, 100)
    joblib.dump(mdl, 'cellsSomModel.sav')
    
    plt.pcolor(mdl.distance_map().T)
    plt.show()

if __name__ == '__main__':
	main()
 





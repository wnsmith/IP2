import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

def main():
    datafile = 'dend.txt'
    df = pd.read_csv(datafile,sep=',')
    df = df.set_index('gene')
    cells = list(df.columns.values)
    dendrogrammer(df, cells)

def dendrogrammer(df, leaf_labels):
    D = df.values
    if len(leaf_labels) != len(D):
        D = np.transpose(D)
    Z = linkage(D, method='ward', metric='euclidean')
    plt.figure(figsize=(10, 6))
    ax = plt.subplot()
    plt.subplots_adjust(left=0.07, bottom=0.3, right=0.98, top=0.95,
    wspace=0, hspace=0)
    plt.xlabel('Cell Line')
    plt.ylabel('Distance')
    dendrogram(Z, leaf_rotation=90., leaf_font_size=10.,
    labels=leaf_labels)
    plt.savefig('dendrogram.png')

if __name__ == '__main__':
    main()



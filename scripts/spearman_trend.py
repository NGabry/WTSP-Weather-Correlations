import sys
import scipy.stats as scipy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':


    years = range(2000,2020,1)

    df = pd.read_csv('1900_2019_clean.csv')
    #df = pd.read_csv('2000_2019_clean.csv')

    if len(sys.argv) == 2:

        df = df.drop(df[df[sys.argv[1]] == 'FALSE'].index)
        df = df[df[sys.argv[1]].notna()]
        x = df['YEAR'].astype(float)
        y = df[sys.argv[1]].astype(float)
        xy = scipy.spearmanr(x,y)
        print(sys.argv[1], 'r=', xy.correlation, 'p=',xy.pvalue)

        plt.style.use('ggplot')
        plt.plot(x, y, 'o', color='navy')
        #plt.plot(x, xy.intercept + xy.slope*x, 'r')
        plt.ylabel(sys.argv[1], fontsize = 16, color='navy')
        plt.xticks(fontsize = 14, rotation=45, horizontalalignment='right')
        plt.xlabel('Year', fontsize = 16,  color='navy')
        plt.tight_layout()
        plt.show()

    if len(sys.argv) == 3:
        arg2 = int(sys.argv[2])

        df = df.drop(df[df['MONTH'] != arg2].index)
        df = df.drop(df[df[sys.argv[1]] == 'FALSE'].index)
        df = df[df[sys.argv[1]].notna()]
        x = df['YEAR'].astype(float)
        y = df[sys.argv[1]].astype(float)
        xy = scipy.linregress(x,y)
        print(sys.argv[1],'/',sys.argv[2], 'r=', xy.rvalue, 'p=',xy.pvalue)

        plt.style.use('ggplot')
        plt.plot(x, y, '-', color='navy')
        #plt.plot(x, xy.intercept + xy.slope*x, 'r')
        plt.ylabel(sys.argv[1], fontsize = 16, color='navy')
        plt.xticks(fontsize = 14, rotation=45, horizontalalignment='right')
        plt.xlabel('Year', fontsize = 16,  color='navy')
        plt.tight_layout()
        plt.show()


import sys
import scipy.stats as scipy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':

    years = range(2000,2020,1)

    weather = pd.read_csv('1999_2018_clean.csv')
    julian = pd.read_csv('Julian_means.csv')

    arg1 = int(sys.argv[1])

    month = weather.drop(weather[weather['MONTH'] != arg1].index)
    month = month.drop(month[month[sys.argv[3]] == 'FALSE'].index)
    month = month[month[sys.argv[3]].notna()]
    y = month[sys.argv[3]].astype(float)
    x = julian[sys.argv[2]].astype(float)
    xy = scipy.linregress(x,y)
    print(sys.argv[2],'/',sys.argv[3], ':', sys.argv[1], 'r=', xy.rvalue, 'p=',xy.pvalue)

    plt.style.use('ggplot')
    plt.plot(x, y, 'o', color='navy')
    plt.plot(x, xy.intercept + xy.slope*x, 'r')
    plt.ylabel(sys.argv[3], fontsize = 16, color='navy')
    plt.xticks(fontsize = 14, rotation=45, horizontalalignment='right')
    plt.xlabel('Julian Date', fontsize = 16,  color='navy')
    plt.tight_layout()
    plt.show()

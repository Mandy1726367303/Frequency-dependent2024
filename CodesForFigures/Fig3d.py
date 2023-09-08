import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import seaborn as sns

A = pd.read_csv(r'cor_NFDS(treat).csv')
x = A.CCF
y = A.NB
sns.jointplot(x, y, data = A, kind = 'reg',xlim=(0.075,0.15),ylim=(0,30),color="indianred")
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':15
         }
plt.tick_params(labelsize=15)
plt.tick_params(pad = 0.03)
plt.ylim(8,30)
plt.yticks([10,15,20,25])
plt.xticks([0.08,0.1,0.12,0.14])
plt.xlabel('Average CCF',font=font,fontsize=22)
plt.ylabel('Antigenic mutation load',font=font,fontsize=22)
plt.title("NFDS (post-therapy)",font=font,fontsize=22)
rho, pval = spearmanr(x, y)
plt.text(0.1,18, r"Spearmans's $\rho$={:.2g}".format(rho), font=font,fontsize=15)
plt.text(0.1,16, r'$p={}\times 10^{}$'.format(*r'{:.2e}'.format(pval).split('e')).replace('^', '^{').replace('$', '}$')[1:], font=font,fontsize=15)
plt.show()

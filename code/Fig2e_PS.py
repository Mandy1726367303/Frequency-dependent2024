import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr

A = pd.read_csv(r'coru1.2.csv')
x = A.CCF
y = A.NB
fig, ax = plt.subplots()
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2))
ax.plot(x, y_est, linewidth=2, color="black",alpha=0.8)
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2,color = "red")
ax.plot(x, y,'o', color='steelblue',alpha=1)
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':20
         }
plt.tick_params(labelsize=15)
plt.tick_params(pad = 0.03)
plt.ylim(-3,22)
plt.yticks([5,15])
plt.xlabel('Average CCF',font=font,fontsize=22)
plt.ylabel('Antigenic mutation load',font=font,fontsize=22)
plt.title("PS",font=font,fontsize=22)
rho, pval = spearmanr(x, y)
ax.text(0.2,19, r"Pearson's $\rho$={:.2g}".format(rho), font=font,fontsize=15)
ax.text(0.2,17, r'$p={}\times 10^{}$'.format(*r'{:.2e}'.format(pval).split('e')).replace('^', '^{').replace('$', '}$')[1:], font=font,fontsize=15)
ax.text(0.07,-2,"Simulated tumors:\n $n=100$",font=font,fontsize=11)
plt.show()
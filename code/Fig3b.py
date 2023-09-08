import matplotlib.pyplot as plt
from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter
from lifelines.utils import median_survival_times
from lifelines.statistics import logrank_test
import pandas as pd

df = pd.read_csv('Virtual_Patients(treat).csv')
kmf = KaplanMeierFitter()
groups = df['s']
ix = (groups == 'PE')

kmf.fit(df['OS'][ix], df['D'][ix], label='PS')
ax = kmf.plot(color='steelblue',linewidth=2.5)
treatment_median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
kmf.fit(df['OS'][~ix], df['D'][~ix], label='NFDS')
ax = kmf.plot(ax=ax,color='indianred',linewidth=2.5)

control_median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':15
         }
plt.ylim(-0.1,1.7)
plt.yticks([0,0.5,1])
plt.xlim(23,63)
plt.tick_params(labelsize=14)
plt.xlabel('Time',font=font,fontsize=18)
plt.ylabel('Fraction of surviving patients',font=font,fontsize=20)
#plt.text(62, 1.13, r'Log-Rank $p<0.005$',font=font, fontsize=14)
plt.text(45, 1.2, r'Log-Rank $p<0.005$',font=font, fontsize=15)
plt.legend(prop = font)
plt.show()
results = logrank_test(df['OS'][ix], df['OS'][~ix], df['D'][ix], df['D'][~ix], alpha=.99)
results.print_summary()
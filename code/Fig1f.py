import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
muload = pd.read_csv('meload.csv')
mhload = pd.read_csv('mehload.csv')

muload = muload.to_numpy().T
mhload = mhload.to_numpy().T
fig, axes = plt.subplots(1,2, figsize=(12,5))

v1 = axes[0].violinplot(dataset=muload.T, widths=0.5,showextrema=False)
v2 = axes[1].violinplot(dataset=mhload.T, widths=0.5,showextrema=False)
#colors1 = ['darkseagreen','mediumaquamarine','lightseagreen','#1c9099']
colors1 = ['#b3cde3','#67a9cf','#43a2ca','#1c9099']
colors2 = ['palegoldenrod','darkkhaki','goldenrod','darkgoldenrod']
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':17
         }

for patch, color in zip(v1['bodies'], colors1):
    #patch.set_edgecolor('black')
    patch.set_alpha(0.7)
    patch.set_facecolor(color)
for patch, color in zip(v2['bodies'], colors2):
    #patch.set_edgecolor('black')
    patch.set_alpha(0.6)
    patch.set_facecolor(color)

for i, d in enumerate(muload):
    min_value, quantile1, median, quantile3, max_value = np.percentile(d, [0, 25, 50, 75, 100])
    axes[0].vlines(i + 1, quantile1, quantile3, color="#1c9099",lw=4, zorder=2,alpha=0.8)
    axes[0].vlines(i + 1, min_value, max_value,color="#1c9099", zorder=2,alpha=0.8)
    axes[0].scatter(i + 1, median, color='#edf8e9', zorder=3, s=7)
for i, d in enumerate(mhload):
    min_value, quantile1, median, quantile3, max_value = np.percentile(d, [0, 25, 50, 75, 100])
    axes[1].vlines(i + 1, quantile1, quantile3,color="#3d4331", lw=4, zorder=2,alpha=0.5)
    axes[1].vlines(i + 1, min_value, max_value, color="#3d4331",zorder=2,alpha=0.5)
    axes[1].scatter(i + 1, median, color='#edf8e9', zorder=3, s=7)

#axes[0].plot([1, 1, 4, 4], [132, 132+2, 132+2, 132], lw=1, c="k")
#axes[1].plot([1, 1, 4, 4], [103, 103+2, 103+2, 103], lw=1, c="k")
my_label = ['s=-0.1','s=-0.4','s=-0.8','s=-1.2']      # 自定义坐标轴值
axes[0].set_ylim(42,150)
y = np.linspace(60,120,3)
axes[0].set_yticks(y)
#axes[0].text(1,134,r'Kruskal-Wallis $p=8.35 \times 10^{-11}$',font=font,fontsize=17)
axes[0].tick_params(labelsize=15)
axes[0].tick_params(pad = 0.03)  #通过pad参数调整距离
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,10000,3))]
axes[0].set_xlabel('Selection intensity',font=font,fontsize=20)
axes[0].set_ylabel('Antigenic mutation load',font=font,fontsize=20)
axes[1].set_ylim(30,120)
y = np.linspace(50,100,3)
axes[1].set_yticks(y)
axes[1].text(1, 107,r'Kruskal-Wallis $p=3.24 \times 10^{-14}$', font=font,fontsize=17)
axes[1].tick_params(labelsize=15)
axes[1].tick_params(labelsize=15)
axes[1].tick_params(pad = 0.03)
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,10000,3))]
axes[1].set_xlabel('Selection intensity',font=font,fontsize=20)
axes[0].set_title("PS (IE)",font=font,fontsize=22)
axes[1].set_title("NFDS (IE)",font=font,fontsize=22)
axes[0].set_xticks(ticks=[1,2,3,4])
axes[1].set_xticks(ticks=[1,2,3,4])
axes[0].set_xticklabels(my_label,font=font)
axes[1].set_xticklabels(my_label,font=font)
#    ,rotation=60, ha='right')
plt.show()

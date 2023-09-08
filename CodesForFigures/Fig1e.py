import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
muload = pd.read_csv('muload1.csv')
mhload = pd.read_csv('mhload1.csv')

muload = muload.to_numpy().T
mhload = mhload.to_numpy().T
fig, axes = plt.subplots(1,2, figsize=(12,5))

v1 = axes[0].violinplot(dataset=muload.T, widths=0.55,showextrema=False)
v2 = axes[1].violinplot(dataset=mhload.T, widths=[0.48,0.45,0.55,0.55],showextrema=False)

#fcae91
#fb6a4a
#de2d26
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':17
         }

colors1 = ['#bdc9e1','#74a9cf','#2b8cbe','#045a8d']
colors2 = ['#fee5d9','#fcae91', '#fb6a4a', '#de2d26']
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
    axes[0].vlines(i + 1, quantile1, quantile3, color="#045a8d",lw=4, zorder=2,alpha=0.7)
    axes[0].vlines(i + 1, min_value, max_value,color="#045a8d", zorder=2,alpha=0.7)
    axes[0].scatter(i + 1, median, color='#eff3ff', zorder=3, s=7)
for i, d in enumerate(mhload):
    min_value, quantile1, median, quantile3, max_value = np.percentile(d, [0, 25, 50, 75, 100])
    axes[1].vlines(i + 1, quantile1, quantile3,color="#a50f15", lw=4, zorder=2,alpha=0.8)
    axes[1].vlines(i + 1, min_value, max_value, color="#a50f15",zorder=2,alpha=0.8)
    axes[1].scatter(i + 1, median, color='#fee5d9', zorder=3, s=7)

#axes[0].plot([1, 1, 4, 4], [115, 115+2, 115+2, 115], lw=1, c="k")
#axes[1].plot([1, 1, 4, 4], [100, 100+2, 100+2, 100], lw=1, c="k")
axes[1].plot([3, 3, 4, 4], [84, 84+2, 84+2, 84], lw=1, c="k")
my_label = ['s=-0.1','s=-0.4','s=-0.8','s=-1.2']      # 自定义坐标轴值
axes[0].set_ylim(25,129)
y = np.linspace(30,100,3)
axes[0].set_yticks(y)
axes[0].text(0.9, 115,r'Kruskal-Wallis $p=8.18 \times 10^{-31}$',font=font,fontsize=17)
#"kruskal-Wallis p=8.1760e-31"
axes[0].tick_params(labelsize=15)
axes[0].tick_params(labelsize=15)
axes[0].tick_params(pad = 0.03)  #通过pad参数调整距离
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,10000,3))]
axes[0].set_xlabel('Selection intensity',font=font,fontsize=20)
axes[0].set_ylabel('Antigenic mutation load',font=font,fontsize=20)
axes[1].set_ylim(40,110)
y = np.linspace(50,100,3)
axes[1].set_yticks(y)
#axes[1].text(1.8, 87, "p=0.76196", fontsize=12)
axes[1].text(2.6, 87, r'Wilcoxon $p=0.048$',font=font, fontsize=14)
axes[1].text(1, 100,r'Kruskal-Wallis $p=9.88 \times 10^{-16}$',font=font, fontsize=17)
axes[1].tick_params(labelsize=15)
axes[1].tick_params(labelsize=15)
axes[1].tick_params(pad = 0.03)  #通过pad参数调整距离
#plt.yticks(y,[format(i,',.2f') for i in y])
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,10000,3))]
axes[1].set_xlabel('Selection intensity',font=font,fontsize=20)
axes[0].set_title("PS",font=font,fontsize=22)
axes[1].set_title("NFDS",font=font,fontsize=22)
axes[0].set_xticks(ticks=[1,2,3,4])
axes[1].set_xticks(ticks=[1,2,3,4])
axes[0].set_xticklabels(my_label,font=font)
axes[1].set_xticklabels(my_label,font=font)
plt.show()

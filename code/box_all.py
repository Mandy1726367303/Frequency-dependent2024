
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

aCCF = pd.read_csv(r'aCCF_All004.csv')
NB = pd.read_csv(r'NB_All004.csv')
SD = pd.read_csv(r'SD_All004.csv')
# 首先有图（fig），然后有轴（ax）
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 5))
bplot1 = axes[0].boxplot(aCCF,
                         vert=True,widths=0.4,#labels=['PS','F-dS'],
                         #positions=[0.05,0.8],
                         patch_artist=True)

bplot2 = axes[1].boxplot(NB,widths=0.4,#labels=['PS','F-dS','PS,E'],
                         #positions=[0.05,0.8],
                         vert=True,
                         patch_artist=True)
bplot3 = axes[2].boxplot(SD,widths=0.4,#labels=['PS','F-dS'],
                         #positions=[0.05,0.8],
                         vert=True,
                         patch_artist=True)
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':10
         }
# 颜色填充
my_label = ['Pervasive','frequency-\ndependent','Pervasive(IE)','Frequency-\ndependent(IE)']
colors = ['steelblue', 'indianred','teal','palevioletred']#,'lightcoral']
for bplot in (bplot1, bplot2, bplot3):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
axes[0].plot([1, 1, 2, 2], [0.3, 0.3+0.02, 0.3+0.02, 0.3], lw=1, c="k")
axes[0].plot([1, 1, 3, 3], [0.42, 0.42+0.02, 0.42+0.02, 0.42], lw=1, c="k")
axes[0].plot([2, 2, 4, 4], [0.47, 0.47+0.02, 0.47+0.02, 0.47], lw=1, c="k")
axes[0].plot([3, 3, 4, 4], [0.53, 0.53+0.02, 0.53+0.02, 0.53], lw=1, c="k")
axes[0].set_ylim(0,0.67)
axes[0].set_yticks([0.1,0.2,0.3])
axes[0].text(1.1, 0.33, r'$7.33 \times 10^{-6}$',font=font, fontsize=12)
axes[0].text(1.5, 0.45, r'$5.58 \times 10^{-7}$',font=font, fontsize=12)
axes[0].text(2.9, 0.5, r'$NS$',font=font, fontsize=12)
axes[0].text(3, 0.56, r'$9.53 \times{-10}$',font=font, fontsize=12)
axes[0].text(0.6, 0.62, r'Kruskal-Wallis $p=6.83 \times 10^{-22}$',font=font, fontsize=14)
axes[0].tick_params(labelsize=14)
axes[0].tick_params(labelsize=14)
axes[0].tick_params(pad = 0.03)  #通过pad参数调整距离
axes[1].plot([1, 1, 2, 2], [23.2, 23.2+3, 23.2+3, 23.2], lw=1, c="k")
axes[1].plot([1, 1, 3, 3], [40, 40+3, 40+3, 40], lw=1, c="k")
axes[1].plot([2, 2, 4, 4], [49, 49+3, 49+3, 49], lw=1, c="k")
axes[1].plot([3, 3, 4, 4], [57, 57+3, 57+3, 57], lw=1, c="k")
axes[1].set_ylim(-5,72)
axes[1].set_yticks([10,20,40])
axes[1].text(1.1, 27, r'$0.017$',font=font, fontsize=12)
axes[1].text(1.5, 44, r'$1.84 \times 10^{-9}$',font=font, fontsize=12)
axes[1].text(2.9, 53, r'$NS$',font=font, fontsize=12)
axes[1].text(3, 61, r'$1.5 \times10^{-9}$',font=font, fontsize=12)
axes[1].text(0.6, 67, r'Kruskal-Wallis $p=1.61 \times 10^{-21}$',font=font, fontsize=14)
axes[1].tick_params(labelsize=12)
axes[1].tick_params(labelsize=12)
axes[1].tick_params(pad = 0.03)  #通过pad参数调整距离
#plt.yticks(y,[format(i,',.2f') for i in y])
#y_tick = ['{:,}'.format(x) for x in (np.linspace(0,10000,3))]
axes[2].plot([1, 1, 2, 2], [4.8, 4.8+0.5, 4.8+0.5, 4.8], lw=1, c="k")
axes[2].plot([1, 1, 3, 3], [12, 12+0.5, 12+0.5, 12], lw=1, c="k")
axes[2].plot([2, 2, 4, 4], [14, 14+0.5, 14+0.5, 14], lw=1, c="k")
axes[2].plot([3, 3, 4, 4], [16, 16+0.5, 16+0.5, 16], lw=1, c="k")
axes[2].set_ylim(-2,21)
axes[2].set_yticks([0,5,10])
axes[2].text(1.1, 5.5, r'$NS$',font=font, fontsize=12)
axes[2].text(1.5, 12.8, r'$1.66 \times 10^{-9}$',font=font, fontsize=12)
axes[2].text(2.9, 15, r'$NS$',font=font, fontsize=12)
axes[2].text(3, 16.7, r'$1.56 \times 10^{-9}$',font=font, fontsize=12)
axes[2].text(0.6, 19, r'Kruskal-Wallis $p=2.55 \times 10^{-21}$',font=font, fontsize=14)
axes[2].tick_params(labelsize=12)
axes[2].tick_params(labelsize=12)
axes[2].tick_params(pad = 0.03)
axes[0].set_title("Average cancer cell fraction\n(CCF>0.4,s=-0.8)",font=font,fontsize=17)
axes[1].set_title("Antigenic mutation load\n(CCF>0.04,s=-0.8)",font=font,fontsize=17)
axes[2].set_title("Shannon diversity\n(CCF>0.04,s=-0.8)",font=font,fontsize=17)
axes[0].set_xticks(ticks=[1,2,3,4])
axes[1].set_xticks(ticks=[1,2,3,4])
axes[2].set_xticks(ticks=[1,2,3,4])
axes[0].set_xticklabels(my_label,font=font,rotation=12)
axes[1].set_xticklabels(my_label,font=font,rotation=12)
axes[2].set_xticklabels(my_label,font=font,rotation=12)
plt.show()
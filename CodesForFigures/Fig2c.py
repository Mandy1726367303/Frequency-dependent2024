import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

aCCF = pd.read_csv(r'aCCF_All001.csv')
NB = pd.read_csv(r'NB_All001.csv')
SD = pd.read_csv(r'SD_All001.csv')
#fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 5))
plt.figure(figsize=(6,5))
#bplot1 = plt.boxplot(aCCF,
                         #vert=True,
                         #patch_artist=True)

bplot2 = plt.boxplot(NB,widths=0.4,
                         vert=True,
                         patch_artist=True)
#bplot3 = plt.boxplot(SD,widths=0.4,
                         #vert=True,
                         #patch_artist=True)
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':14
         }

my_label = ['PS','NFDS','PS (IE)','NFDS (IE)']
colors = ['steelblue', 'indianred','teal','darkgoldenrod']#,'lightcoral']
for patch, color in zip(bplot2['boxes'], colors):
    patch.set_facecolor(color)
#plt.plot([1, 1, 2, 2], [0.09, 0.09+0.008, 0.09+0.008, 0.09], lw=1, c="k")
#plt.plot([1, 1, 3, 3], [0.184, 0.185+0.008, 0.184+0.008, 0.184], lw=1, c="k")
#axes[0].plot([3, 3, 4, 4], [0.212, 0.212+0.008, 0.212+0.008, 0.212], lw=1, c="k")
#plt.plot([2, 2, 4, 4], [0.22, 0.22+0.008, 0.22+0.008, 0.22], lw=1, c="k")
#plt.ylim(0,0.27)
#plt.yticks([0.1,0.2])
#plt.text(1.1, 0.1, r'$0.0018$',font=font, fontsize=15)
#plt.text(1.5, 0.194, r'$3.091 \times 10^{-8}$',font=font, fontsize=15)
#plt.text(2.8, 0.224, r'$9.07 \times 10^{-10}$',font=font, fontsize=12)
#plt.text(1.4, 0.24, r'Kruskal-Wallis $p=7.57 \times 10^{-22}$',font=font, fontsize=15)
#plt.text(2.8, 0.23, r'$NS$',font=font, fontsize=15)
plt.tick_params(labelsize=15)
plt.tick_params(labelsize=15)
plt.tick_params(pad = 0.03)  #通过pad参数调整距离
plt.plot([1, 1, 2, 2], [83, 83+5, 83+5, 83], lw=1, c="k")
plt.plot([1, 1, 3, 3], [124, 124+5, 124+5, 124], lw=1, c="k")
#plt.plot([3, 3, 4, 4], [137, 137+5, 137+5, 137], lw=1, c="k")
plt.plot([2, 2, 4, 4], [141, 141+5, 141+5, 141], lw=1, c="k")
plt.ylim(20,168)
plt.yticks([60,90,120])
plt.text(1, 89, r'$6.26 \times 10^{-6}$',font=font, fontsize=15)
plt.text(1.35, 130, r'$1.97 \times 10^{-9}$',font=font, fontsize=15)
#plt.text(2.9, 144, r'$3.07 \times 10^{-9}$',font=font, fontsize=12)
plt.text(2.8, 147, r'$NS$',font=font, fontsize=15)
#plt.text(0.8, 155, r'Kruskal-Wallis $p=1.59 \times 10^{-24}$',font=font, fontsize=15)
#plt.yticks(y,[format(i,',.2f') for i in y])
#y_tick = ['{:,}'.format(x) for x in (np.linspace(0,10000,3))]
#plt.plot([1, 1, 2, 2], [9, 9+0.6, 9+0.6, 9], lw=1, c="k")
#plt.plot([1, 1, 3, 3], [18.5, 18.5+0.6, 18.5+0.6, 18.5], lw=1, c="k")
#axes[2].plot([3, 3, 4, 4], [21, 21+0.6, 21+0.6, 21], lw=1, c="k")
#plt.plot([2, 2, 4, 4], [21, 21+0.6, 21+0.6, 21], lw=1, c="k")
#plt.ylim(1,24)
#plt.yticks([5,10])
#plt.text(1.2, 9.8, r'$0.0003$',font=font, fontsize=15)
#plt.text(1.5, 19.3, r'$1.47 \times 10^{-9}$',font=font, fontsize=15)
#plt.text(2.9, 21.8, r'$1.47 \times 10^{-9}$',font=font, fontsize=12)
#plt.text(2.8, 21.8, r'$NS$',font=font, fontsize=15)
#plt.text(0.8, 24, r'Kruskal-Wallis $p=1.53 \times 10^{-23}$',font=font, fontsize=14)
#plt.title("Average cancer cell fraction",font=font,fontsize=22)
plt.title("Antigenic mutation load",font=font,fontsize=22)
#plt.title("Shannon diversity",font=font,fontsize=22)
plt.xticks(ticks=[1,2,3,4],labels=my_label,rotation=0,font=font)
#axes[2].set_xticks(ticks=[1,2,3,4])
#axes[2].set_xticklabels(my_label,font=font,rotation=12)
plt.show()
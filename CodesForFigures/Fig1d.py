import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

T1 = pd.read_csv(r'rate_0.1.csv')
T2 = pd.read_csv(r'rate_0.4.csv')
T3 = pd.read_csv(r'rate_0.8.csv')
bplot1 = plt.boxplot(T1,
                         vert=True,widths=0.5,
                         patch_artist=True)


font = {'family':'Arial' ,
        #'weight':'bold',
        'size':17
         }
# 颜色填充
my_label = ['PS','NFDS']
color1 = ['steelblue','indianred']
for patch, color in zip(bplot1['boxes'], color1):
    patch.set_facecolor(color)

plt.tick_params(labelsize=15)
plt.tick_params(labelsize=15)
plt.tick_params(pad = 0.03)
plt.ylim(0.05,0.5)
plt.yticks([0.1,0.4])
plt.ylabel('Tumor growth rate',font=font,fontsize=22)
plt.plot([1, 1, 2, 2], [0.43, 0.43+0.01, 0.43+0.01, 0.43], lw=1, c="k")
#plt.plot([1, 1, 2, 2], [0.33, 0.33+0.01, 0.33+0.01, 0.33], lw=1, c="k")
#plt.text(0.95,0.348,r'Wilcoxon $p=2.19 \times 10^{-6}$',font=font)
#plt.text(1,0.34,r'Wilcoxon $p=2.19 \times 10^{-6}$',font=font)
plt.text(1.4,0.45,r'NS',font=font)
plt.xticks(ticks=[1,2],labels=my_label,font=font)
plt.title("$s=-0.1$",font=font,fontsize=22)
plt.show()

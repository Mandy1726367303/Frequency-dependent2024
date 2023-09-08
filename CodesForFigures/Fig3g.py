import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

aCCF = pd.read_csv(r'Pre_PostCCF(PS).csv')
plt.figure(figsize=(6,6))
bplot1 = plt.boxplot(aCCF,
                         vert=True,widths=0.3,
                         labels=['Pre-therapy','Post-therapy'],
                         patch_artist=True)
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':17
         }
color1 = ['teal','steelblue']
for patch, color in zip(bplot1['boxes'], color1):
    patch.set_facecolor(color)
x = aCCF.Pre
y = aCCF.Post
plt.plot([1, 1, 2, 2], [0.045,0.045+0.001, 0.045+0.001, 0.045], lw=1, c="k")
plt.text(1,0.147, r'Wilcoxon $p=1.63 \times 10^{-9}$',font=font, fontsize=16)
#plt.text(1.4,0.0463, r'NS',font=font, fontsize=16)
plt.ylim(0.022,0.05)
plt.yticks([0.03,0.04])
plt.ylabel('Average CCF',font=font,fontsize=22)
plt.title("PS",font=font,fontsize=22)
plt.tick_params(labelsize=17)
plt.show()
print(stats.wilcoxon(x, y))
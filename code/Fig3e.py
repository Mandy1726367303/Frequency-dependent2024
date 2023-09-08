import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
mh = np.loadtxt('m_NFDS_IE_1.txt')
mh1 = np.loadtxt('m_NFDS_IE_2.txt')
mh2 = np.loadtxt('m_NFDS_IE_3.txt')
mh3 = np.loadtxt('m_NFDS_IE_4.txt')
mh4 = np.loadtxt('m_NFDS_IE_5.txt')
mh = mh[:,1]/10000
mh = mh[mh>0.04]
mh1 = mh1[:,1]/10000
mh1 = mh1[mh1>0.04]
mh2 = mh2[:,1]/10000
mh2 = mh2[mh2>0.04]
mh3 = mh3[:,1]/10000
mh3 = mh3[mh3>0.04]
mh4 = mh4[:,1]/10000
mh4 = mh4[mh4>0.04]
mu = np.loadtxt('m_PS_IE_1.txt')
mu1 = np.loadtxt('m_PS_IE_2.txt')
mu2 = np.loadtxt('m_PS_IE_3.txt')
mu3 = np.loadtxt('m_PS_IE_4.txt')
mu4 = np.loadtxt('m_PS_IE_5.txt')
mu = mu[:,1]/10000
mu = mu[mu>0.04]
mu1 = mu1[:,1]/10000
mu1 = mu1[mu1>0.04]
mu2 = mu2[:,1]/10000
mu2 = mu2[mu2>0.04]
mu3 = mu3[:,1]/10000
mu3 = mu3[mu3>0.04]
mu4 = mu4[:,1]/10000
mu4 = mu4[mu4>0.04]
font = {'family':'Arial' ,
        #'weight':'bold',
        'size':13
         }
axes[1].hist(mh, bins = 25, range=(0.04,0.65),alpha=0.8, color='darkgoldenrod')
axes[1].hist(mh1, bins = 25, range=(0.04,0.65),alpha=1, color='darkgoldenrod')
axes[1].hist(mh2, bins = 25, range=(0.04,0.65),alpha=0.4, color='darkgoldenrod')
axes[1].hist(mh3, bins = 25 ,range=(0.04,0.65),alpha=0.6, color='darkgoldenrod')
axes[1].hist(mh4, bins = 25, range=(0.04,0.65),alpha=0.5, color='darkgoldenrod')
axes[1].set_xlabel('Cancer cell fraction',font=font, fontsize=20)
axes[0].set_ylabel('Number of subclonal mutations',font=font, fontsize=20)
axes[1].set_title("NFDS (IE)",font=font, fontsize=20)
axes[0].tick_params(labelsize=14)
axes[1].tick_params(labelsize=14)
axes[0].hist(mu, bins = 25, range=(0.04,0.65),alpha=1, color='teal')
axes[0].hist(mu1, bins = 25, range=(0.04,0.65),alpha=0.8, color='teal')
axes[0].hist(mu2, bins = 25, range=(0.04,0.65),alpha=0.6, color='teal')
axes[0].hist(mu3, bins = 25, range=(0.04,0.65),alpha=0.4, color='teal')
axes[0].hist(mu4, bins = 25, range=(0.04,0.65),alpha=0.5, color='teal')
axes[0].set_xlim(0.006,1.01)
axes[0].set_yticks([40,80])
axes[1].set_yticks([60,120])
axes[1].set_xlim(0.006,1.01)
axes[0].text(0.35, 76,"Distinct subclones", font=font,fontsize=17)
axes[1].text(0.3, 40,"No distinct subclone", font=font,fontsize=17)
#axes[0].set_ylim(-5,130)
axes[0].set_xlabel('Cancer cell fraction',font=font, fontsize=20)
axes[0].set_title("PS (IE)",font=font, fontsize=20)
plt.show()

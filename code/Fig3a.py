import numpy as np
import matplotlib.pyplot as plt
ph1 = np.loadtxt('p_NFDS_treat1.txt')
ph2 = np.loadtxt('p_NFDS_treat2.txt')
ph3 = np.loadtxt('p_NFDS_treat3.txt')
th1 = np.loadtxt('t_NFDS_treat1.txt')
th2 = np.loadtxt('t_NFDS_treat2.txt')
th3 = np.loadtxt('t_NFDS_treat3.txt')

pu1 = np.loadtxt('p_PS_treat1.txt')
pu2 = np.loadtxt('p_PS_treat2.txt')
pu3 = np.loadtxt('p_PS_treat3.txt')
tu1 = np.loadtxt('t_PS_treat1.txt')
tu2 = np.loadtxt('t_PS_treat2.txt')
tu3 = np.loadtxt('t_PS_treat3.txt')


ah1 = round(len(th1)/10)
th1_1 = th1[:ah1]
th1_2 = th1[ah1:]
ph1_1 = ph1[:ah1]
ph1_2 = ph1[ah1:]
ah2 = round(len(th2)/14)
th2_1 = th2[:ah2]
th2_2 = th2[ah2:]
ph2_1 = ph2[:ah2]
ph2_2 = ph2[ah2:]
ah3 = round(len(th3)/13)
th3_1 = th3[:ah3]
th3_2 = th3[ah3:]
ph3_1 = ph3[:ah3]
ph3_2 = ph3[ah3:]

au1 = round(len(tu1)/3)
tu1_1 = tu1[:au1]
tu1_2 = tu1[au1:]
pu1_1 = pu1[:au1]
pu1_2 = pu1[au1:]
au2 = round(len(tu2)/3)
tu2_1 = tu2[:au2]
tu2_2 = tu2[au2:]
pu2_1 = pu2[:au2]
pu2_2 = pu2[au2:]
au3 = round(len(tu3)/3)
tu3_1 = tu3[:au3]
tu3_2 = tu3[au3:]
pu3_1 = pu3[:au3]
pu3_2 = pu3[au3:]
plt.plot(tu1_1,pu1_1,linewidth=3,color='teal',alpha=1,label="PS (IE)")
plt.plot(tu1_2,pu1_2,linewidth=3,color='steelblue',alpha=1,label="PS")
plt.plot(tu2_1,pu2_1,linewidth=3,color='teal',alpha=1)
plt.plot(tu2_2,pu2_2,linewidth=3,color='steelblue',alpha=1)
plt.plot(tu3_1,pu3_1,linewidth=3,color='teal',alpha=1)
plt.plot(tu3_2,pu3_2,linewidth=3,color='steelblue',alpha=1)
plt.plot(th1_1,ph1_1,linewidth=3,color='darkgoldenrod',alpha=1,label="NFDS (IE)")
plt.plot(th1_2,ph1_2,linewidth=3,color='indianred',alpha=1,label="NFDS")
plt.plot(th2_1,ph2_1,linewidth=3,color='darkgoldenrod',alpha=1)
plt.plot(th2_2,ph2_2,linewidth=3,color='indianred',alpha=1)
plt.plot(th3_1,ph3_1,linewidth=3,color='darkgoldenrod',alpha=1)
plt.plot(th3_2,ph3_2,linewidth=3,color='indianred',alpha=1)

font = {'family':'Arial' ,
        'size':15
         }
plt.xlim(-5,55)
x=np.linspace(0,50,3)
plt.xticks(x)
plt.ylim(-2000,40000)
y = np.linspace(0,38000,3)
plt.yticks(y)
plt.yticks(y,[format(i,',.0f') for i in y])
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,35000,3))]
plt.tick_params(labelsize=15)
plt.tick_params(pad = 0.03)
plt.xlabel('Time',font=font,fontsize=22)
plt.ylabel('Number of cells',font=font,fontsize=22)
plt.title("Simulations of immunotherapy",fontsize=22)
#plt.text(16, 27000, "Checkpoint blockade",font=font, fontsize=15)
plt.legend(loc="upper left",prop=font)
plt.show()
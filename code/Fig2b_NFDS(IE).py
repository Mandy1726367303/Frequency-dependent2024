import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p1 = np.loadtxt('p_NFDS_IE_0.txt')
p2 = np.loadtxt('p_NFDS_IE_1.txt')
p3 = np.loadtxt('p_NFDS_IE_2.txt')
p4 = np.loadtxt('p_NFDS_IE_3.txt')
p5 = np.loadtxt('p_NFDS_IE_4.txt')
p6 = np.loadtxt('p_NFDS_IE_5.txt')
p7 = np.loadtxt('p_NFDS_IE_6.txt')
p8 = np.loadtxt('p_NFDS_IE_7.txt')
p9 = np.loadtxt('p_NFDS_IE_8.txt')
p10 = np.loadtxt('p_NFDS_IE_9.txt')
p11 = np.loadtxt('p_NFDS_IE_10.txt')
p12 = np.loadtxt('p_NFDS_IE_11.txt')
p13 = np.loadtxt('p_NFDS_IE_12.txt')
p14 = np.loadtxt('p_NFDS_IE_13.txt')
p15 = np.loadtxt('p_NFDS_IE_14.txt')
p16 = np.loadtxt('p_NFDS_IE_15.txt')
p17 = np.loadtxt('p_NFDS_IE_16.txt')
p18 = np.loadtxt('p_NFDS_IE_17.txt')
p19 = np.loadtxt('p_NFDS_IE_18.txt')
p20 = np.loadtxt('p_NFDS_IE_19.txt')
t1 = np.loadtxt('t_NFDS_IE_0.txt')
t2 = np.loadtxt('t_NFDS_IE_1.txt')
t3 = np.loadtxt('t_NFDS_IE_2.txt')
t4 = np.loadtxt('t_NFDS_IE_3.txt')
t5 = np.loadtxt('t_NFDS_IE_4.txt')
t6 = np.loadtxt('t_NFDS_IE_5.txt')
t7 = np.loadtxt('t_NFDS_IE_6.txt')
t8 = np.loadtxt('t_NFDS_IE_7.txt')
t9 = np.loadtxt('t_NFDS_IE_8.txt')
t10 = np.loadtxt('t_NFDS_IE_9.txt')
t11 = np.loadtxt('t_NFDS_IE_10.txt')
t12 = np.loadtxt('t_NFDS_IE_11.txt')
t13 = np.loadtxt('t_NFDS_IE_12.txt')
t14 = np.loadtxt('t_NFDS_IE_13.txt')
t15 = np.loadtxt('t_NFDS_IE_14.txt')
t16 = np.loadtxt('t_NFDS_IE_15.txt')
t17 = np.loadtxt('t_NFDS_IE_16.txt')
t18 = np.loadtxt('t_NFDS_IE_17.txt')
t19 = np.loadtxt('t_NFDS_IE_18.txt')
t20 = np.loadtxt('t_NFDS_IE_19.txt')

font = {'family':'Arial' ,
        #'weight':'bold',
        'size':11
         }
plt.figure(figsize=(4,6))
plt.plot(t1,p1,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t2,p2,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t4,p4,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t5,p5,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t6,p6,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t7,p7,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t8,p8,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t9,p9,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t10,p10,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t11,p11,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t12,p12,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t13,p13,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t14,p14,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t15,p15,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t16,p16,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t17,p17,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t18,p18,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t19,p19,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t20,p20,linewidth=6,color="darkgoldenrod",alpha=0.2)
plt.plot(t3,p3,linewidth=3,color="darkgoldenrod",alpha=1)

plt.xlim(-5,39)
x = np.linspace(0,30,3)
plt.xticks(x,font=font,fontsize=17)
plt.ylim(-7000,110000)
y = np.linspace(0,100000,3)
plt.yticks(y,font=font,fontsize=17)
plt.tick_params(labelsize=15)
plt.yticks(y,[format(i,',.0f') for i in y])
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,100000,3))]
plt.xlabel('Time',font=font, fontsize=22)
plt.title("NFDS (IE)",font=font,fontsize=21)
#plt.ylabel('Number of tumor cells',font=font,fontsize=22)
plt.show()








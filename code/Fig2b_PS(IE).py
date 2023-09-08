import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

p2 = np.loadtxt('p_PS_1.txt')
p3 = np.loadtxt('p_PS_2.txt')
p4 = np.loadtxt('p_PS_3.txt')
p5 = np.loadtxt('p_PS_4.txt')
p6 = np.loadtxt('p_PS_5.txt')
p7 = np.loadtxt('p_PS_6.txt')
p8 = np.loadtxt('p_PS_48.txt')
p9 = np.loadtxt('p_PS_49.txt')
p10 = np.loadtxt('p_PS_9.txt')
p11 = np.loadtxt('p_PS_10.txt')
p12 = np.loadtxt('p_PS_40.txt')
p18 = np.loadtxt('p_PS_41.txt')
p19 = np.loadtxt('p_PS_42.txt')
p20 = np.loadtxt('p_PS_44.txt')
p21 = np.loadtxt('p_PS_20.txt')
p22 = np.loadtxt('p_PS_21.txt')
p23 = np.loadtxt('p_PS_22.txt')
p24 = np.loadtxt('p_PS_45.txt')
p25 = np.loadtxt('p_PS_46.txt')
p26 = np.loadtxt('p_PS_25.txt')
p27 = np.loadtxt('p_PS_26.txt')
p30 = np.loadtxt('p_PS_29.txt')
t2 = np.loadtxt('t_PS_1.txt')
t3 = np.loadtxt('t_PS_2.txt')
t4 = np.loadtxt('t_PS_3.txt')
t5 = np.loadtxt('t_PS_4.txt')
t6 = np.loadtxt('t_PS_5.txt')
t7 = np.loadtxt('t_PS_6.txt')
t8 = np.loadtxt('t_PS_48.txt')
t9 = np.loadtxt('t_PS_49.txt')
t10 = np.loadtxt('t_PS_9.txt')
t11 = np.loadtxt('t_PS_10.txt')
t12 = np.loadtxt('t_PS_40.txt')
t18 = np.loadtxt('t_PS_41.txt')
t19 = np.loadtxt('t_PS_42.txt')
t20 = np.loadtxt('t_PS_44.txt')
t21 = np.loadtxt('t_PS_20.txt')
t22 = np.loadtxt('t_PS_21.txt')
t23 = np.loadtxt('t_PS_22.txt')
t24 = np.loadtxt('t_PS_45.txt')
t25 = np.loadtxt('t_PS_46.txt')
t26 = np.loadtxt('t_PS_25.txt')
t27 = np.loadtxt('t_PS_26.txt')
t30 = np.loadtxt('t_PS_29.txt')


font = {'family':'Arial' ,
        #'weight':'bold',
        'size':11
         }
plt.figure(figsize=(4,6))
plt.plot(t2,p2,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t3,p3,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t4,p4,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t5,p5,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t6,p6,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t7,p7,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t8,p8,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t9,p9,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t10,p10,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t11,p11,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t12,p12,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t18,p18,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t19,p19,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t20,p20,linewidth=8,color="cadetblue",alpha=0.3)
plt.plot(t21,p21,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t22,p22,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t23,p23,linewidth=7,color="cadetblue",alpha=0.3)
#plt.plot(t24,p24,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t25,p25,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t26,p26,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t27,p27,linewidth=7,color="cadetblue",alpha=0.3)
plt.plot(t30,p30,linewidth=3,color="teal",alpha=1)


plt.xlim(-5,50)
x = [0,20,40]
plt.xticks(x,font=font,fontsize=17)
plt.ylim(-16000,110000)
y = np.linspace(0,100000,3)
plt.yticks(y,font=font,fontsize=17)
plt.tick_params(labelsize=15)
plt.yticks(y,[format(i,',.0f') for i in y])
y_tick = ['{:,}'.format(x) for x in (np.linspace(0,100000,3))]
plt.xlabel('Time',font=font, fontsize=22)
#axes[1].set_ylabel('Number of tumor cells',fontsize=15)
plt.title("PS (IE)",font=font,fontsize=22)
#plt.ylabel('Number of tumor cells',font=font,fontsize=22)
plt.show()








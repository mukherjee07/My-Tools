# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend import Legend
#import matplotlib
df=pd.read_csv('Axial.csv')
df2=pd.read_csv('energy2I5.csv')
df3=pd.read_csv('energy2A5.csv')
Li = df.iloc[:,0].values
BEI = df.iloc[:,7].values
#BEI = 27.14*BEI
BEI2 = df.iloc[:,5].values
BEI3 = df.iloc[:,4].values
Li2=df2.iloc[:,0].values
#BEI2=df2.iloc[:,1].values
#BEI2 = 27.14*BEI2
Li3=df3.iloc[:,0].values
#BEI3=df3.iloc[:,2].values
#BEI = 27.14*BEI
#BEI3 = 27.14*BEI3
#Li2=df.iloc[:,9].values
fig=plt.figure()
#plt.subplot(111)
#ax1= fig.add_subplot(111)
##ax1.set_legend("Fukui Indices")
#ax1.set_xlabel("Position index",fontsize="12")
#ax1.set_ylabel("minimum energy (eV)",fontsize="12")
##ax1.set_ylim([-0.4,6])
#ax1.plot(Li,BEI,'olive',marker="H")
#ax1.legend(["energy B3LYP/TZVP "],loc="best",bbox_to_anchor=(0.47, 0.7),fontsize="12")
#ax2 = ax1.twinx()
##ax2.set_legend("Fukui Indices")
#ax2.set_xlabel("Position index",fontsize="12")
#ax2.set_ylabel("optimum z-axis distance Å",fontsize="12")
##ax2.ylim([-0.4,6])
#ax2.plot(Li,BEI2,'c',marker="8")
###Legend(ax2, lines[1:], ['line C', 'line D'],
## #            loc='lower right', frameon=False)
#ax2.legend(["z-axis B3LYP/TZVP"],loc="center right",fontsize="12")
#ax1.add_artist(l2)
#plt.grid('True')
#plt.legend(["PBE0 with SVP basis set"],loc="center right")
#plt.subplot(212)
#plt.legend("Z-axis distance (in Angstorm)")
#plt.xlabel("conformer index",fontsize="12")
#plt.ylabel("energy NTCDA+10Li (eV)",fontsize="12")
#plt.ylim([-0.4,6])
#plt.plot(Li2,BEI2,'green',marker="8")
#plt.legend(["PBE0 with SVP basis set"],loc="upper right",fontsize="12")
##plt.grid('True')
##
#plt.subplot(311)
plt.legend("energy NTCDA+5$Li^+$")
plt.xlabel("conformer index",fontsize="12")
plt.ylabel("energy NTCDA+5$Li^+$ (in eV)",fontsize="12")
#plt.lim([0,5])
plt.plot(Li,BEI,'teal',marker="8")
plt.legend(["PBE0 with TZVP basis set"],fontsize="12",loc="upper center")
#plt.subplots_adjust(top=1.00, bottom=0.0, left=0.00, right=1.0, hspace=2.00,
#               wspace=2.0)
#fig.savefig("19.jpg", dpi=200, bbox_inches='tight')
plt.show()



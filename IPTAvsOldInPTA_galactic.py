from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import numpy as np

dat = []

ggl=[]

ggb=[]

f1 = open('IPTA_LB.txt','r')  #complete list of IPTA pulsars with 64 objects
n1 = 0
for line in f1:
 s = line.split()
 dat.append(s)
 n1 = n1 +1  

for i in range(0,n1):
     
     ggl.append(float(dat[i][0]))  # galactic coordinates input
     ggb.append(float(dat[i][1]))

f1.close()

N=i

gl = ggl * u.degree
gb = ggb * u.degree


c = SkyCoord(l=gl, b=gb, frame='galactic')


l_rad = c.l.wrap_at(180 * u.deg).radian
b_rad = c.b.radian

data = []

ggl2=[]
ggb2=[]

#

f3 = open('InPTAOld_LB.txt','r') # complete list of OLD InPTA pulsars with 19 objects
n3 = 0
for line in f3:
    s3 = line.split()
    data.append(s3)
    n3 = n3 +1

for j in range(0,n3):
    
    ggl2.append(float(data[j][0]))   
    ggb2.append(float(data[j][1]))

f3.close()

#
M=j

gl2 = ggl2 * u.degree
gb2 = ggb2 * u.degree

c2 = SkyCoord(l=gl2, b=gb2, frame='galactic')
l2_rad = c2.l.wrap_at(180 * u.deg).radian
b2_rad = c2.b.radian

plt.figure(figsize=(8,4.2))
plt.subplot(111, projection="aitoff")
plt.title("Location of InPTA and IPTA pulsars", y=1.08, fontsize=20)
plt.grid(True)

plt.scatter(l_rad, b_rad, c="grey", s=220, marker="h", alpha=0.7) # IPTA pulsars plotted as gray diamonds
plt.scatter(l3_rad, b3_rad, c="red",s=20,alpha=0.9)  # InPTA old pulsars plotted as red circles


plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('l (deg)', fontsize=20)
plt.ylabel('b (deg)', fontsize=20)

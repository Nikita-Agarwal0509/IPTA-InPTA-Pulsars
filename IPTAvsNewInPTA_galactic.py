from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import numpy as np

dat = []

ggl=[]

ggb=[]

f1 = open('/home/nikita/Documents/IPTA_LB.txt','r')  #complete list of IPTA pulsars with 64 objects
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

ggl1=[]
ggb1=[]

f2 = open('/home/nikita/Documents/InPTANew_LB.txt','r') # complete list of NEW InPTA pulsars with 7 objects
n2 = 0
for line in f2:
    s2 = line.split()
    data.append(s2)
    n2 = n2 +1

for j in range(0,n2):
    
    ggl1.append(float(data[j][0]))
    ggb1.append(float(data[j][1]))



f2.close()

M=j



gl1 = ggl1 * u.degree
gb1 = ggb1 * u.degree

c1 = SkyCoord(l=gl1, b=gb1, frame='galactic')
l1_rad = c1.l.wrap_at(180 * u.deg).radian
b1_rad = c1.b.radian

plt.figure(figsize=(8,4.2))
plt.subplot(111, projection="aitoff")
plt.title("Location of IPTA and NEW InPTA pulsars", y=1.08)
plt.grid(True)

plt.scatter(l_rad, b_rad, c="grey", s=90, alpha=0.6) # IPTA pulsars plotted as red circles
plt.scatter(l1_rad, b1_rad, c="red", s=30, marker="*", alpha=0.6) # InPTA new pulsars plotted as red stars

plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('l (deg)')
plt.ylabel('b (deg)')

plt.subplots_adjust(top=0.95, bottom=0.0)
plt.show()

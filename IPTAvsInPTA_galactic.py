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

ggl1=[]
ggb1=[]

ggl3=[]
ggb3=[]


f2 = open('InPTANew_LB.txt','r') # complete list of NEW InPTA pulsars with 7 objects
n2 = 0
for line in f2:
    s2 = line.split()
    data.append(s2)
    n2 = n2 +1

for j in range(0,n2):
    
    ggl1.append(float(data[j][0]))
    ggb1.append(float(data[j][1]))



f2.close()






f3 = open('InPTAOld_LB.txt','r') # complete list of OLD InPTA pulsars with 19 objects
n3 = 0
for line in f3:
    s3 = line.split()
    data.append(s3)
    n3 = n3 +1

for j in range(0,n3):
    
    ggl3.append(float(data[j][0]))
    ggb3.append(float(data[j][1]))



f3.close()



#

M=j



gl1 = ggl1 * u.degree
gb1 = ggb1 * u.degree




gl3 = ggl3 * u.degree
gb3 = ggb3 * u.degree


c1 = SkyCoord(l=gl1, b=gb1, frame='galactic')
l1_rad = c1.l.wrap_at(180 * u.deg).radian
b1_rad = c1.b.radian



c3 = SkyCoord(l=gl3, b=gb3, frame='galactic')
l3_rad = c3.l.wrap_at(180 * u.deg).radian
b3_rad = c3.b.radian



plt.figure(figsize=(8,4.2))
plt.subplot(111, projection="aitoff")
plt.title("Location of InPTA and IPTA pulsars", y=1.08, fontsize=20)
plt.grid(True)

P1=plt.scatter(l_rad, b_rad, c="grey", s=400, marker="h", alpha=0.7) # IPTA pulsars plotted as gray diamonds
P2=plt.scatter(l1_rad, b1_rad, c="blue",s=500, marker="*",alpha=0.5) # InPTA new pulsars plotted as blue stars
P3=plt.scatter(l3_rad, b3_rad, c="red",s=100,alpha=0.9)  # InPTA old pulsars plotted as red circles

plt.legend((P1,P2,P3),('IPTA Pulsars','InPTA New Plusars','InPTA Old Pulsars'),bbox_to_anchor=(1.1,1.00),fontsize=10) #legend

plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('l (deg)', fontsize=20)
plt.ylabel('b (deg)', fontsize=20)

plt.subplots_adjust(top=0.95, bottom=0.0)
plt.show()



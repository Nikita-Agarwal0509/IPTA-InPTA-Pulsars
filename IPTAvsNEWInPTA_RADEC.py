from astropy import units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import numpy as np

dat = []

ra1=[]

dec1=[]

f = open('/home/nikita/Documents/IPTA_RADEC.txt','r')  #list of IPTA pulsars with 64 objects
n = 0
for line in f:
 s = line.split()
 dat.append(s)
 n = n +1  

for i in range(0,n):
     
     ra1.append(dat[i][0])  #  coordinates input
     dec1.append(dat[i][1])


 
f.close()

#

c = SkyCoord(ra=ra1, dec=dec1, unit=(u.hour, u.deg))
ra_rad = c.ra.wrap_at(180 * u.deg).radian
dec_rad = c.dec.radian


data = []

ra11=[]
dec11=[]

#

f1 = open('/home/nikita/Documents/InPTANew_RADEC.txt','r') # complete list of NEW InPTA pulsars with 7 objects
n1 = 0
for line in f1:
    s1 = line.split()
    data.append(s1)
    n1 = n1 +1

for j in range(0,n1):
    
    ra11.append(float(data[j][0]))
    dec11.append(float(data[j][1]))

f1.close()

#

c2 = SkyCoord(ra=ra11, dec=dec11, unit=(u.hour, u.deg))
ra2_rad = c2.ra.wrap_at(180 * u.deg).radian
dec2_rad = c2.dec.radian

plt.figure(figsize=(8,4.2))
plt.subplot(111, projection="aitoff")
plt.title("Location of IPTA and NEW InPTA pulsars", y=1.08)
plt.grid(True)

plt.scatter(ra_rad, dec_rad, c="blue") # IPTA pulsars plotted as blue circles
plt.scatter(ra2_rad, dec2_rad, c="green") # InPTA new pulsars plotted as green circles

plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('RA')
plt.ylabel('DEC')
plt.show()

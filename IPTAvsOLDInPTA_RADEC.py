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
ra12=[]
dec12=[]

#

f2 = open('/home/nikita/Documents/InPTAOld_RADEC.txt','r') # complete list of OLD InPTA pulsars with 19 objects
n2 = 0
for line in f2:
    s2 = line.split()
    data.append(s2)
    n2 = n2 +1

for j in range(0,n2):
    
    ra12.append(float(data[j][0]))
    dec12.append(float(data[j][1]))



f2.close()

#

c3 = SkyCoord(ra=ra12, dec=dec12, unit=(u.hour, u.deg))
ra3_rad = c3.ra.wrap_at(180 * u.deg).radian
dec3_rad = c3.dec.radian


plt.figure(figsize=(8,4.2))
plt.subplot(111, projection="aitoff")
plt.title("Location of IPTA and OLD InPTA pulsars", y=1.08)
plt.grid(True)

plt.scatter(ra_rad, dec_rad, c="blue") # IPTA pulsars plotted as blue circles
plt.scatter(ra3_rad, dec3_rad, c="red")  # InPTA old pulsars plotted as red circles

plt.subplots_adjust(top=0.95, bottom=0.0)
plt.xlabel('RA')
plt.ylabel('DEC')
plt.show()


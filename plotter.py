import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

m = sio.loadmat("swp_4000_-40dB__YY160622p2_DMLE.mat")

f = m["f"]

z = 20*np.log10(np.absolute(m["z"]))
#zz = np.zeros(z.shape)
plt.plot(f, z, ".")


for i in range(2, 41):
    b = 100*i
    e = b + 99
    z0 = z[b:e]
    delta = z[b-1] - z[b]
    z[b:e] = z0 + delta

plt.plot(f, z, ".")
plt.show()

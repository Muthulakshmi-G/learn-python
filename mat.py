import numpy as np
import matplotlib.pyplot as plt
x=np.arange(5)
y=np.arange(5)


plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.scatter(x,y)
plt.show()

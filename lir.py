import numpy as np
import matplotlib.pyplot as plt

X=np.arange(30)
Y=3*X+2+np.random.randn(X.shape[0])

plt.scatter(X,Y)

w=-1
b=-1




lr=0.001
losse=[]
w_grads=[]

b_grads=[]
w1=[]
b1=[]

for i in range(1000):
    w1.append(w)
    b1.append(b)
    for xi,yi in zip(X,Y):
        h=w*X+b

loss=np.sqrt(pow(yi-h,2))

#compute gradient

w_grad=-2*xi*(yi-(w*xi+b))
b_grad=-2*(yi-(w*xi+b))
w=w-lr*w_grad
b=b-lr*b_grad

loss.append(loses[0])

w_grads.append(w_grad)
b_grads.append(b_grad)

print(w,b)
plt.scatter(X,Y)
plt.plot(X,w*x+b)

plt.plot(X,3*X+2)
plt.show()

plt.plot(w_grads)
plt.show()

plt.plot(b_grads)
plt.show()

plt.plot(w1)
plt.show()

plt.plot(b1)
plt.show()

plt.plot(rand(len(losses)),losses)
plt.show()

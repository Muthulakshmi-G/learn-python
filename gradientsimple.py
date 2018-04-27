x_data=[1.0,2.0,3.0]
y_data=[2.0,4.0,6.0]


w=1.0


def forward(x):
    return x*w

def loss(x,y):

    ypred=forward(x)
    return(ypred-y)*(ypred-y)

def gradient(x,y):
    return 2*x*(x*w-y)

print('before training', forward(4)) 

#training loop

for epoch in range(100):
    for x_val,y_val in zip(x_data,y_data):
        grad=gradient(x_val,y_val)
        w=w-0.01*grad

        print("\tgrad:",x_val,y_val,grad)
        l=loss(x_val,y_val)
 
print("prograss:",epoch,"w=",w,"loss=",l)


print("after traning","4hrs",forward(4))

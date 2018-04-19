import torch
import torch.nn as nn
import numpy as np

from torch.autograd import Variable



input_size = 1
output_size = 1
num_epochs = 60
learning_rate = 0.001

# X_train and Y_train datas
x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], 
                    [9.779], [6.182], [7.59], [2.167], [7.042], 
                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)

y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], 
                    [3.366], [2.596], [2.53], [1.221], [2.827], 
                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)

# Linear Regression Model
class LinearRegression(nn.Module):  #class defined
    def __init__(self, input_size, output_size):#input size and output size
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)  
    
    def forward(self, x):
        out = self.linear(x)
        return out
#namma model-a intializing panrom
model = LinearRegression(input_size, output_size)

# Loss and Optimizer select panrom.namma loss function Mean Squared Error
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)  

# Train the Model 
for epoch in range(num_epochs):  
    # Convert numpy array to torch Variable
    inputs = Variable(torch.from_numpy(x_train)) #x_train values are assign to the variable inputs
    targets = Variable(torch.from_numpy(y_train))#y_train values are assign to the variable outputs

    # Forward + Backward + Optimize
    optimizer.zero_grad()    #optimizer gradient
    outputs = model(inputs) #predicted value find panna inputs pass panrom  
    loss = criterion(outputs, targets)  #loss compute panrom
    loss.backward()  #inga backpropogation nadakuthu ,weights update panrom
    optimizer.step()
    
    if (epoch+1) % 5 == 0:
        print ('Epoch [%d/%d], Loss: %.4f' 
               %(epoch+1, num_epochs, loss.data[0]))
        
#predicted values stored 
predicted = model(Variable(torch.from_numpy(x_train))).data.numpy()


# Save the Model
torch.save(model.state_dict(), 'model.pkl')        

from torch import nn

# neural network class
class Perceptron(nn.Module):
  def __init__(self, input_features):
    # inherit all the features from parent class
    super(Perceptron, self).__init__()
    self.fc1 = nn.Linear(input_features, 5)
    self.fc2 = nn.Linear(5, 4)
    self.fc3 = nn.Linear(4,3)
    self.fc4 = nn.Linear(3, 1)
    self.tanh = nn.Tanh()
    self.sigmoid  = nn.Sigmoid()


  # method to build the network flow
  def forward(self, x):
    out = self.fc1(x)
    out = self.tanh(out)
    out = self.fc2(out)
    out = self.tanh(out)
    out = self.fc3(out)
    out = self.tanh(out)
    out = self.fc4(out)
    out = self.sigmoid(out)

    return out
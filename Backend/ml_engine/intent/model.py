import torch
from torch import nn

class NeuralNet(nn.Module):
    def __init__(self, input_layer:int, hidden_layer:int, num_classes: int):
        super().__init__()

        self.layer1= nn.Linear(input_layer, hidden_layer)
        self.layer2 = nn.Linear(hidden_layer, hidden_layer)
        self.layer3 = nn.Linear(hidden_layer, num_classes)
        self.relu = nn.ReLU()


    def forward(self, x:torch.Tensor) -> torch.Tensor:
        out =self.layer1(x)
        out=self.relu(out)
        out=self.layer2(out)
        out=self.relu(out)
        out=self.layer3(out)
        return out

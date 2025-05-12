import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.tensorboard import SummaryWriter

# 搭建网络模型
class Net(nn.Module):
    def __init__(self, input_dim, layer1_dim,
                 layer2_dim, output_dim):
        super(Net, self).__init__()
        self.flatten = nn.Flatten()
        self.layer1 = nn.Sequential(
            nn.Linear(input_dim, layer1_dim),
            nn.ReLU())
        self.layer2 = nn.Sequential(
            nn.Linear(layer1_dim, layer2_dim),
            nn.ReLU()
        )
        self.out = nn.Sequential(
            nn.Linear(layer2_dim, output_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        x = self.flatten(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.out(x)
        return x
    
# 初始化网络和输入输出
input_dict = {
    'input_dim': 32 * 32,
    'layer1_dim': 512,
    'layer2_dim': 128,
    'output_dim': 10
}
model = Net(**input_dict)
input_data = torch.rand(1, 32, 32)
output_data = model(input_data)

with SummaryWriter(comment='Net') as writer:
    writer.add_graph(model, input_data)
print(output_data)
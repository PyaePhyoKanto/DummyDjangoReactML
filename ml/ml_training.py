import torch
import torch.nn as nn
import torch.optim as optim

# Define a larger neural network
class LargerNet(nn.Module):
    def __init__(self):
        super(LargerNet, self).__init__()
        self.fc1 = nn.Linear(10, 128)
        self.fc2 = nn.Linear(128, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 2)  # Output is 2 classes

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.fc4(x)
        return x

# Function to simulate a more complex training process
def train_larger_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training on {device}")
    model = LargerNet().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Simulate a larger dataset
    inputs = torch.randn(1000, 10).to(device)
    labels = torch.randint(0, 2, (1000,)).to(device)

    # Increase the number of epochs for longer training
    for epoch in range(500):  # Modify the number of epochs as needed
        total_loss = 0
        for i in range(len(inputs)):
            optimizer.zero_grad()
            outputs = model(inputs[i].unsqueeze(0))
            loss = criterion(outputs, labels[i].unsqueeze(0))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(inputs)
        print(f"Epoch {epoch+1}, Avg Loss: {avg_loss}")
    
    print("Training complete")

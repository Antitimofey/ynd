import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error
import torch
from torch import nn


def convert_data():
    train = pd.read_csv('train.csv')
    train.sample(frac=1, replace=True)
    train[9000:].to_csv('my_test.csv', index=False)
    train[:9000].to_csv('my_train.csv', index=False)


#def main():
def baseline():
    #train = pd.read_csv('train.csv')
    #X_train = train.drop('y', axis=1)
    #y_train = train['y']

    train = pd.read_csv('train.csv')
    X_train = train.drop('y', axis=1)
    y_train = train['y']

    #X_test = pd.read_csv('test_x.csv')
    X_test = pd.read_csv('my_test.csv').drop('y', axis=1)

    model = CatBoostRegressor(
        verbose=False,
        random_seed=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    pd.Series(predictions, name='y').to_csv('test_y.csv', index=False)


def decision():
    model_task_1 = None

    device = 'cpu'

    class NeuralNetwork(nn.Module):
        def __init__(self):
            super().__init__()
            self.flatten = nn.Flatten()
            self.linear_relu_stack = nn.Sequential(
                nn.Linear(21, 16),
                nn.ReLU(),
                nn.Linear(21, 16),
                nn.ReLU(),
                nn.Linear(16, 1)
            )

        def forward(self, x):
            x = self.flatten(x)
            logits = self.linear_relu_stack(x)
            return logits
        


        
    model_task_1 = NeuralNetwork().to(device)




    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model_task_1.parameters(), lr=0.01)

    def train(dataloader, model, loss_fn, optimizer):
        size = len(dataloader.dataset)
        model.train()
        for batch, (X, y) in enumerate(dataloader):
            X, y = X.to(device), y.to(device)

            # Compute prediction error
            pred = model(X)
            loss = loss_fn(pred, y)

            # Backpropagation
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            if batch % 100 == 0:
                loss, current = loss.item(), (batch + 1) * len(X)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


    def test(dataloader, model, loss_fn):
        size = len(dataloader.dataset)
        num_batches = len(dataloader)
        model.eval()
        test_loss, correct = 0, 0
        with torch.no_grad():
            for X, y in dataloader:
                X, y = X.to(device), y.to(device)
                pred = model(X)
                test_loss += loss_fn(pred, y).item()
                correct += (pred.argmax(1) == y).type(torch.float).sum().item()
        test_loss /= num_batches
        correct /= size
        print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

    print(1e-1)
    epochs = 15 # 20 -> 0,91 0,883
    for t in range(epochs):
        print(f"Epoch {t+1}\n-------------------------------")
        train(train_data_loader, model_task_1, loss_fn, optimizer)
        test(test_data_loader, model_task_1, loss_fn)
    print("Done!")
            

    model_task_1 = NeuralNetwork().to(device)



def compare_accuracy():
    real = pd.read_csv('my_test.csv')['y']
    #print(real)
    predicted = pd.read_csv('test_y.csv')['y']
    #print(predicted)
    print('baseline MSE is', mean_squared_error(real, predicted))
    


if __name__ == '__main__':
    #main()
    compare_accuracy()


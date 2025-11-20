import numpy as np

# Input data (XOR problem)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Initialize weights and biases
W1 = np.random.rand(2,3)
b1 = np.random.rand(1,3)
W2 = np.random.rand(3,1)
b2 = np.random.rand(1,1)

# Activation function
def sigmoid(x): return 1/(1+np.exp(-x))

# Feedforward step
def feedforward(X):
    h = sigmoid(np.dot(X, W1) + b1)
    out = sigmoid(np.dot(h, W2) + b2)
    return out

print("Feedforward output:\n", feedforward(X))


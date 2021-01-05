import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import regression as reg
from sklearn.neighbors import regression

"""Generating data"""
N = 100  # number of points per class
D = 2  # dimensionality
K = 3  # number of classes
X = np.zeros((N*K, D))  # data matrix (each row = single example)
y = np.zeros(N*K, dtype='uint8')  # class labels
for j in range(K):
  ix = range(N*j, N*(j+1))
  r = np.linspace(0.0,1,N) # radius
  t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*0.2 # theta
  X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
  y[ix] = j
# lets visualize the data:
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
plt.show()

"""Training a Softmax Linear Classifier"""

# initialize parameters randomly
W = 0.01 * np.random.randn(D, K)  # Recall that we D = 2 is the dimensionality and K = 3 is the number of classes.
b = np.zeros((1,K))

# compute class scores for a linear classifier
scores = np.dot(X, W) + b


num_examples = X.shape[0]
# get unnormalized probabilities
exp_scores = np.exp(scores)
# normalize them for each example
probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)


correct_logprobs = -np.log(probs[range(num_examples),y])

# compute the loss: average cross-entropy loss and regularization
data_loss = np.sum(correct_logprobs)/num_examples
reg_loss = 0.5*regularization*np.sum(W*W)
loss = data_loss + reg_loss

import numpy as np
import random
import math

class Layer:

    def __init__(self, numInputs, numNeurons) -> None:
        
        self.weights = 0.10 * np.random.randn(numInputs, numNeurons)
        self.biases = np.zeros((1,numNeurons))
        self.outputs = []
    
    def forward(self, inputs) -> None:
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:

    def forward(self, inputs):
        self.output = np.maximum(0,inputs)

class Activation_Softmax:

    def forward(self, inputs):

        inputs -= np.max(inputs, axis=1, keepdims=True)

        expVals = np.exp(inputs)
        self.output = expVals / np.sum(expVals, axis=1, keepdims=True)



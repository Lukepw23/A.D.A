import numpy as np
import random


class Neuron:

    def __init__(self, inputCount):
        self.inputCount = inputCount
        self.output = 0
        self.weights = []
        self.bias = 0
        if self.inputCount != 0:
            self.setValues()

    def setValues(self):
        tempVals = []
        for _ in range(self.inputCount):
            self.weights.append((random.random() * 2) - 1)
        
        self.bias = (random.random() * 6) - 3


    def calculateOutput(self, inputs):
        if self.inputCount != 0:
            return np.dot(self.weights, inputs)
        else:
            return inputs[0]

    def __str__(self):
        weightsOut = ""
        weightsOut += "["
        for j in self.weights:
            weightsOut = weightsOut + str(j) + ", "
        weightsOut = weightsOut[0:(len(weightsOut)-2)]
        weightsOut += "]\n"


        return "Weights: \n" + weightsOut + "\n" + "Bias: " + str(self.bias)
        

# n = Neuron(3)
# print(n)
# print("\nOutput:" + str(n.calculateOutput([1,2,3])))

class RELU:
    pass

class Layer:

    def __init__(self, inputNodeCount, nodeCount):
        self.nodeCount = nodeCount
        self.inputNodeCount = inputNodeCount
        self.neurons = []
        for _ in range(self.nodeCount):
            n = Neuron(self.inputNodeCount)
            self.neurons.append(n)

    def calculateLayer(self, inputs):
        output = []
        for neuron in self.neurons:
            output.append(neuron.calculateOutput(inputs))
        return output
    
    def setInputNodeCount(self, val):
        self.inputNodeCount = val
        self.neurons = []
        for _ in range(self.nodeCount):
            n = Neuron(self.inputNodeCount)
            self.neurons.append(n)

# l = Layer(8, 5)
# print(l.calculateLayer([1,2,3,4,5,6,7,8]))

class Neural_Network:

    def __init__(self, inputNodeCount, outputNodeCount):
        self.layerCounts = [inputNodeCount, outputNodeCount]
        self.layers = []
        self.hiddenLayerCount = 0
        
        self.inputLayer = Layer(0, self.inputNodeCount)
        self.outputLayer = Layer(self.inputNodeCount, self.outputNodeCount)

    def addHiddenLayer(self, nodeCount):
        l = Layer(self.layerCounts[self.hiddenLayerCount], nodeCount)
        self.layers.append(l)
        self.hiddenLayerCount += 1
        self.outputLayer = Layer(self.inputNodeCount, self.layers[:-1])
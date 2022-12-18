#include "neural_network.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Neuron {

    vector<double> weights;
    double bias;
    
    public:

        Neuron(string type) {
            if (type != "input" || type != "output") {
                /* Randomize Weights */
            }
        }

        double calculate_output(vector<double> inputVals) {
            double output = 0.0;
            double calcTemp = 0.0;
            for (int i = 0; i < inputVals.size(); i++) {
                calcTemp = inputVals[i] * weights[i];
                output += calcTemp;
            }
            output += bias;

            return output;
        }


};

class Layer {

    public:

        Layer() {

        }

};

class Neural_Network {

    public:

        Neural_Network() {

        }

};
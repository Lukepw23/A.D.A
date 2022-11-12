#include "math.h"

int Math::add(vector<int> inputs) { // COMPLETED
    
    int output = 0;
    
    for (int i = 0; i < inputs.size(); i++) {
        output += inputs[i];
    }

    return output;

}

int Math::subtract(vector<int> inputs) { // COMPLETED

    int output = 0;
    
    for (int i = 0; i < inputs.size(); i++) {
        output -= inputs[i];
    }

    return output;

}

int Math::multiply(vector<int> inputs) { // COMPLETED

    int output = 1;
    
    for (int i = 0; i < inputs.size(); i++) {
        output *= inputs[i];
    }

    return output;

}

int Math::divide(vector<int> inputs) { // COMPLETED

    int output = inputs[0];
    
    for (int i = 1; i < inputs.size(); i++) {
        output += inputs[i];
    }

    return output;

}

int Math::power(int inputNumber, int power) { // COMPLETED

    int output = pow(inputNumber, power);

    return output;
}

int Math::root(int inputNumber, int root) { // COMPLETED

    int output = pow(inputNumber, (1/root));

    return output;
    
}

int Math::solve_equation(string inputEquation) { // NOT STARTED
    // "4=x-1" // "3x^2-2x+1" // "4x^3-3x^2+2x-1"
    return 0;
}

int Math::conversion(int inputNumber, string startingUnit, string endingUnit) { // NOT STARTED
    return 0;
}

int Math::trig_functions(int inputAngle) { // NOT STARTED
    return 0;
}

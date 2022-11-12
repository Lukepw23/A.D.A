#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

class Math {

    public:

        int add(vector<int> inputs); // COMPLETED
        int subtract(vector<int> inputs); // COMPLETED
        int multiply(vector<int> inputs); // COMPLETED
        int divide(vector<int> inputs); // COMPLETED
        int power(int inputNumber, int power); // COMPLETED
        int root(int inputNumber, int root); // COMPLETED

        int solve_equation(string inputEquation); // NOT STARTED
        int conversion(int inputNumber, string startingUnit, string endingUnit); // NOT STARTED
        int trig_functions(int inputAngle); // NOT STARTED

};
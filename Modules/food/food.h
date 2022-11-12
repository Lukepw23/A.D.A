#include <iostream>
#include <vector>

using namespace std;

class food_item {

    public:

        string name;
        int calorieCount;
        string time;

        food_item(string n, int cc, string t);

        string get_name();
    
};


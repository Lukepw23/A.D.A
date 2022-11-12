#include "food.h"

food_item::food_item(string n, int cc, string t) {
    name = n;
    calorieCount = cc;
    time = t;
}

string food_item::get_name() {
    return name;
}
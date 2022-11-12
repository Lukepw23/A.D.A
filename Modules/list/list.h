#include <iostream>
#include <vector>
#include <initializer_list>

using namespace std;

class string_list {

    public:

        vector<string> contents;

        void append(string item); // COMPLETED
        void clear(); // COMPLETED
        int count(); // COMPLETED
        int index(string item); // COMPLETED
        void insert(string item, int index); // COMPLETED
        void pop(int index); // COMPLETED
        void remove(string item); // COMPLETED
        void print(); // COMPLETED
};


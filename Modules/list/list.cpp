#include "List.h"

void string_list::append(string item) { // COMPLETED
    contents.push_back(item);
}

void string_list::clear() { // COMPLETED
    contents.clear();
}

int string_list::count() { // COMPLETED
    return contents.size();
}

int string_list::index(string item) { // COMPLETED
    
    for (int i = 0; i < contents.size(); i++) {
        if (contents[i] == item) {
            return i;
        }
    }

    return -1;

}

void string_list::insert(string item, int index) { // COMPLETED

    vector<string> copy = contents;

    contents.clear();

    int count = 0;

    for (int i = 0; i < copy.size()+1; i++) {
        if (i == index) {
            contents.push_back(item);
            count = 1;
        } else {
            contents.push_back(copy[(i-count)]);
        }

    }

}

void string_list::pop(int index) { // COMPLETED

    contents.erase(contents.begin()+index);

}

void string_list::remove(string item) { // COMPLETED

    for (int i = 0; i < contents.size(); i++) {
        if (contents[i] == item) {
            contents.erase(contents.begin() + i);
        }
    }
}

void string_list::print() { // COMPLETED
    cout << "[";
    for (int i = 0; i < contents.size(); i++) {

        if (i == 0) {
            cout << contents[i];
        } else {
            cout << ", " << contents[i];
        }

    }
    cout << "]" << endl;
}
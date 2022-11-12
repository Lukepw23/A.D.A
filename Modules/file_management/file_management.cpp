/* -------------------------------------------------------------------------- */
/*                                  Includes                                  */
/* -------------------------------------------------------------------------- */


#include "file_management.h"


/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


/* ------------------------------ Reading files ----------------------------- */

vector<string> read_from_file(string filePath) { // COMPLETED

    ifstream User(filePath);

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(User, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    User.close();

    return fileOutput;

}

/* ---------------------------- Writing to Files ---------------------------- */

void write_to_file(string filePath, vector<string> newFileContents) { // COMPLETED

    ofstream User(filePath);

    User << "";

    for (int i = 0; i < newFileContents.size(); i++) {
        User << newFileContents[i] << endl;
    }

    User.close();

}

void add_line_to_file(string filePath, string newItem) { // COMPLETED

    vector<string> fileContents = read_from_file(filePath);

    fileContents.push_back(newItem);

    write_to_file(filePath, fileContents);
}

/* --------------------------- Deleting from Files -------------------------- */

void delete_line_from_file(string filePath, string removeItem) { // COMPLETED

    vector<string> fileContents = read_from_file(filePath);

    for (int i = 0; i < fileContents.size(); i++) {
        if (fileContents[i] == removeItem) {
            fileContents.erase(fileContents.begin()+i);
        }
    }

    write_to_file(filePath, fileContents);

}

/* ----------------------------- Other Functions ---------------------------- */

string get_dictionary_value(string filePath, string attributeName) { // COMPLETED

    vector<string> fileOut = read_from_file(filePath);

    int changeIndex;

    for (int i = 0; i < fileOut.size(); i++) {
        int colonIndex = fileOut[i].find(':');

        if (colonIndex == attributeName.size()) {
            if (fileOut[i].substr(0,colonIndex) == attributeName) {
                return fileOut[i].substr(colonIndex+1, fileOut[i].size()-1);
            }
        }
        
    }

    return "NULL";

}


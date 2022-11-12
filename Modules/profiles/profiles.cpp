#include "profiles.h"

/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


const string directoryName = "profile_directory/";
const string setDirectoryFileLocation = "cd ./" + directoryName;
const vector<string> fileNames = {"attributes.txt", "web_history.txt", "relations.txt"};


/* --------------------------- Assistant Functions -------------------------- */

string to_lowercase(string word) { // COMPLETED

    string output;
    
    for (int i = 0; i < word.size(); i++) {
        output.push_back(tolower(word[i]));
    }
    
    return output;

}

string get_profile_folder_path(string first, string last) { // COMPLETED

    string firstName, lastName;

    firstName = to_lowercase(first);
    lastName = to_lowercase(last);

    string fileLocation = directoryName + firstName + "_" + lastName;

    return fileLocation;

}

string get_attribute_file_path(string first, string last) { // COMPLETED

    string fileLocation = directoryName + to_lowercase(first) + '_' + to_lowercase(last) + "/attributes.txt";

    return fileLocation;

}

/* --------------------------- Main User Functions -------------------------- */

string new_profile(string first, string last) { // NEEDS CHECKING
    
    string firstName = to_lowercase(first);
    string lastName = to_lowercase(last);

    vector<string> fileContents = read_from_file(directoryName + "profile_name_dictionary.txt");

    for(int i = 0; i < fileContents.size(); i++) {
        if (fileContents[i] == (directoryName + firstName + '_' + lastName)) {
            return "profile already exists";
        }
    }    
    
    string makeFile = setDirectoryFileLocation + " && mkdir " + firstName + "_" + lastName;
    const char *output = makeFile.c_str();
    system(output);

    for (int i = 0; i < fileNames.size(); i++) {
        ofstream file("./" + directoryName + firstName + "_" + lastName + "/" + fileNames[i]);

        if (fileNames[i] == "attributes.txt") {
            file << "first_name:" << firstName << endl;
            file << "last_name:" << lastName << endl;
        }

        file.close();
    }

    string dictAddition = directoryName + firstName + "_" + lastName;

    add_line_to_file(directoryName + "profile_name_dictionary.txt", dictAddition);

    return "profile created";
    
}

string delete_profile(string first, string last) { // NEEDS CHECKING

    cout << get_profile_folder_path(first, last) << endl;

    if (bool_check_profile_exists(first, last)) {

        string command = "rm -r " + get_profile_folder_path(first, last);

        string dictDeletion = directoryName + first + "_" + last;

        delete_line_from_file(directoryName + "profile_name_dictionary.txt", dictDeletion);

        const char *newCommand = command.c_str();

        system(newCommand);

        return "profile deleted";
    
    } else {

        return "profile does not exist";

    }

}

string change_profile_name(string oldFirst, string oldLast, string newFirstName, string newLastName) { // NEEDS CHECKING 

    try {

        oldFirst = to_lowercase(oldFirst);
        oldLast = to_lowercase(oldLast);

        string command = "mv ./" + directoryName + oldFirst + ' ' + oldLast + " " + "./" + directoryName + newFirstName + '_' + newLastName;

        delete_line_from_file(directoryName + "profile_name_dictionary.txt", (directoryName + oldFirst + ' ' + oldLast));

        string dictAddition = directoryName + newFirstName + '_' + newLastName;

        add_line_to_file(directoryName + "profile_name_dictionary.txt", dictAddition);    
        const char *newCommand = command.c_str();
        system(newCommand);

        return "profile name changed";

    } catch (...) {

        return "profile name change failed";

    }

}

string add_attribute(string firstName, string lastName, string attributeName, string attributeValue) {  // NEEDS CHECKING 

    if (bool_check_profile_exists(firstName, lastName)) {

        vector<string> fileOut = read_from_file(get_attribute_file_path(firstName, lastName));

        fileOut.push_back((attributeName + ':' + attributeValue));

        string path = directoryName + to_lowercase(firstName) + '_' + to_lowercase(lastName) + "/attributes.txt";

        write_to_file(path, fileOut);

        return "attribute added";

    } else {

        return "profile does not exist";

    }

}

string delete_attribute(string firstName, string lastName, string attributeName) { // NEEDS CHECKING 

    if (bool_check_profile_exists(firstName, lastName)) {

        vector<string> fileOut = read_from_file(get_attribute_file_path(firstName, lastName));

        int removeIndex;

        for (int i = 0; i < fileOut.size(); i++) {
            int colonIndex = fileOut[i].find(':');

            if (colonIndex == attributeName.size()) {
                if (fileOut[i].substr(0,colonIndex) == attributeName) {
                    removeIndex = i;
                }
            }

            
        }
        
        fileOut.erase(fileOut.begin()+removeIndex);

        string path = directoryName + to_lowercase(firstName) + '_' + to_lowercase(lastName) + "/attributes.txt";

        write_to_file(path, fileOut);

        return "attribute deleted";

    } else {

        return "profile does not exist";

    }

}

string change_attribute(string firstName, string lastName, string attributeName, string attributeValue) { // NEEDS CHECKING 

    if (bool_check_profile_exists(firstName, lastName)) {

        vector<string> fileOut = read_from_file(get_attribute_file_path(firstName, lastName));

        int changeIndex;

        for (int i = 0; i < fileOut.size(); i++) {
            int colonIndex = fileOut[i].find(':');

            if (colonIndex == attributeName.size()) {
                if (fileOut[i].substr(0,colonIndex) == attributeName) {
                    changeIndex = i;
                }
            }

            
        }

        fileOut.erase(fileOut.begin()+changeIndex);

        fileOut.push_back(attributeName + ':' + attributeValue);

        string path = directoryName + to_lowercase(firstName) + '_' + to_lowercase(lastName) + "/attributes.txt";

        write_to_file(path, fileOut);

        return "attribute changed";

    } else {

        return "profile does not exist";

    }

}

string get_profile_count() { // NEEDS CHECKING
    
    vector<string> fileContents = read_from_file(directoryName + "profile_name_dictionary.txt");

    return "there are " + to_string(fileContents.size()) + " profiles";
    
}

string get_attribute(string first, string last, string attributeName) { // NEEDS CHECKING 

    if (bool_check_profile_exists(first, last)) {

        vector<string> fileOut = read_from_file(get_attribute_file_path(first, last));

        int changeIndex;

        for (int i = 0; i < fileOut.size(); i++) {
            int colonIndex = fileOut[i].find(':');

            if (colonIndex == attributeName.size()) {
                if (fileOut[i].substr(0,colonIndex) == attributeName) {
                    return "the attribute value is " + fileOut[i].substr(colonIndex+1, fileOut[i].size()-1);
                }
            }
            
        }

    } else {

        return "profile does not exist";

    }

    return "";

}

string get_attribute_count(string first, string last) { // NEEDS CHECKING

    if (bool_check_profile_exists(first, last)) {

        vector<string> fileOut = read_from_file(get_attribute_file_path(first, last));

        int count = 0;

        for (int i = 0; i < fileOut.size(); i++) {
            if (fileOut[i] != "") {
                count++;
            }
        }

        return "there are " + to_string(count) + " attributes";

    } else {

        return "profile does not exist";

    }

}

string check_profile_exists(string first, string last) { // NEEDS CHECKING 

    vector<string> fileContents = read_from_file(directoryName + "profile_name_dictionary.txt");

    for (int i = 0; i < fileContents.size(); i++) {
        if (fileContents[i] == get_profile_folder_path(first, last)) {
            return "profile exists";
        }
    }

    return "profile does not exist";

}

bool bool_check_profile_exists(string first, string last) { // NEEDS CHECKING 

    vector<string> fileContents = read_from_file(directoryName + "profile_name_dictionary.txt");

    for (int i = 0; i < fileContents.size(); i++) {
        if (fileContents[i] == get_profile_folder_path(first, last)) {
            return true;
        }
    }

    return false;

}

/* ---------------------------- Family Functions ---------------------------- */

string new_family(string familyName) { // NEEDS CHECKING

    string funcName = "new_family";
    string outFileName = "newFamily";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + familyName + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];

}

string delete_family(string familyName) { // NEEDS CHECKING

    string funcName = "delete_family";
    string outFileName = "deleteFamily";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + familyName + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];
    
} 

string change_family_name(string oldName, string newName) { // NEEDS CHECKING

    string funcName = "change_family_name";
    string outFileName = "changeFamilyName";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + oldName + '"' + ',' + '"' + newName + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];

} 

string add_family_member(string familyName, string profileName) { // NEEDS CHECKING

    string funcName = "add_family_member";
    string outFileName = "addFamilyMember";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + familyName + '"' + ',' + '"' + profileName + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];

}

string remove_family_member(string familyName, string profileName) { // NEEDS CHECKING

    string funcName = "remove_family_member";
    string outFileName = "removeFamilyMember";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + familyName + '"' + ',' + '"' + profileName + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];

}

string move_family_member(string profileName, string oldFamilyName, string newFamilyName) { // NEEDS CHECKING

    string funcName = "move_family_member";
    string outFileName = "moveFamilyMember";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + profileName + '"' + ',' + '"' + oldFamilyName + '"' + ',' + '"' + newFamilyName + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];

}

string edit_member_role(string profileName, string familyName, string newRole) { // NEEDS CHECKING

    string funcName = "edit_member_role";
    string outFileName = "editMemberRole";

    string statement = to_string(0) + "import Modules.profiles.profiles as p; p." + funcName + "(" + '"' + profileName + '"' + ',' + '"' + familyName + '"' + ',' + '"' + newRole + '"' + ")";
    statement.erase(0,1);

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    string fName = "output_files/" + outFileName + "Output";
    ifstream file(fName);

    ///

    string fileLineOut;
    vector<string> fileOutput;

    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            fileOutput.push_back(fileLineOut);
        }
        
    }

    file.close();
    ///

    remove(fName.c_str());

    return fileOutput[0];

}
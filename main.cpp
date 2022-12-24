/* -------------------------------------------------------------------------- */
/*                                  Includes                                  */
/* -------------------------------------------------------------------------- */


#include "Modules/file_management/file_management.h"
#include "Modules/math/math.h"
#include "Modules/reminders/reminders.h"
#include "Modules/schedule/schedule.h"
#include "Modules/security/security.h"
#include "Modules/profiles/profiles.h"
#include "Modules/speech_documentation/speech_documentation.h"


/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


vector<string> get_words(string sentence) { // COMPLETED

    string word;
    vector<string> words;

    for (int i = 0; i < sentence.length(); i++) {
        if (sentence[i] != ' ') {
            word += sentence[i];
        }
        else {
            words.push_back(word);
            word = "";
        }
    }

    words.push_back(word);
    return words;

}

vector<string> get_tag_sentence(int number) { // COMPLETED
    string fName = "output_files/TSoutput_" + to_string(number);
    ifstream file(fName);

    string fileLineOut;
    string line;

    vector<string> output;
    
    while ( getline(file, fileLineOut) ) {
        
        if (fileLineOut != "" || fileLineOut != " ") {
            line = fileLineOut;
        }
        
    }

    int colon = line.find(':');
    string tag = line.substr(0, colon);
    output.push_back(tag);
    string sentence = line.substr(colon+1, line.length()-1);
    output.push_back(sentence);

    return output;

}

void edit_output_file(int number, string fileContents) { // COMPLETED
    string fName = "output_files/TSoutput_" + to_string(number);
    ofstream file(fName);
    file << "";
    file << fileContents;
    file.close();
}

string get_verbal_input(int number, string question) { // COMPLETED

    string statement = "import Modules.voice_recognition.speech_detection as sr; sr.cpp_recognize_speech_from_mic(" + to_string(number) + "," + '"' + question + '"' + ")";

    string command = "python -c '" + statement + "'";

    system(command.c_str());

    cout << "done with py" << endl;

    string fName = "output_files/speechRecOutput_" + to_string(number);
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


/* -------------------------------------------------------------------------- */
/*                      Get Response Assisting Functions                      */
/* -------------------------------------------------------------------------- */


string get_from_response_file(string tag) { // COMPLETED

    string newTag = "";

    for (int i = 0; i < tag.length(); i++) {
        if (tag[i] == ' ') {
            newTag.push_back('_');
        }
        else {
            newTag.push_back(tag[i]);
        }
    }

    string fName = "STORAGE/responses/" + newTag + ".txt";

    vector<string> responses = read_from_file(fName);

    int random = rand() % responses.size();
    string response = responses[random];


    return response;
}

string get_name_from_input(string sentence) { // COMPLETED

    vector<string> words = get_words(sentence);
    string name;

    for (int i = 0; i < words.size(); i++) {
        if ((words[i] == "for") || (words[i] == "name") || (words[i] == "to") || (words[i] == "from")) {

            if (i+1 <= words.size()-1) {
                if (words[i+1] != "please") {
                    name.append(words[i+1]);
                }
            }
            if (i+2 <= words.size()-1) {
                if (words[i+2] != "please") {
                    name.append(' ' + words[i+2]);
                }
            }
            
        }
    }
    return name;
}

string simplify_get_current_profile(string input) { // COMPLETED
    
    string out;

    for (int i = 6; i < input.length(); i++) {

        if (input[i] != '_') {

            out.push_back(input[i]);

        } else {

            out.push_back(' ');

        }

    }

    return out;

}


/* -------------------------------------------------------------------------- */
/*                        Get Response Sorting Function                       */
/* -------------------------------------------------------------------------- */


int get_response(int number) {// IN PROGRESS

    vector<string> tagSentence = get_tag_sentence(number);

    string tag = tagSentence[0];
    string sentence = tagSentence[1];
    string output;

    Time time;

    if (tag == "AVA age"){ // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "AVA freetime") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "hello") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "delete profile") { // COMPLETED
        vector<string> name = get_words(get_name_from_input(sentence));
        output = delete_profile(name[0], name[1]);
        edit_output_file(number, output);
    }

    else if (tag == "add attribute") { // COMPLETED
        vector<string> name = get_words(get_name_from_input(sentence));
        string attrName = get_verbal_input(number, "what is the attribute name?");
        string attrValue = get_verbal_input(number, "what is the attribute value?");
        output = add_attribute(name[0], name[1], attrName, attrValue);
        edit_output_file(number, output);
    }

    else if (tag == "change attribute") { // COMPLETED
        vector<string> name = get_words(get_name_from_input(sentence));
        string attrName = get_verbal_input(number, "what is the attribute name?");
        string attrValue = get_verbal_input(number, "what is the attribute value?");
        output = change_attribute(name[0], name[1], attrName, attrValue);
        edit_output_file(number, output);
    }

    else if (tag == "get attribute") { // NEEDS CHECKING
        vector<string> name = get_words(get_name_from_input(sentence));
        string attrName = get_verbal_input(number, "what is the attribute name?");
        output = get_attribute(name[0], name[1], attrName);
        edit_output_file(number, output);
    }

    else if (tag == "check profile") { // COMPLETED
        vector<string> name = get_words(get_name_from_input(sentence));
        output = check_profile_exists(name[0], name[1]);
        edit_output_file(number, output);
    }

    else if (tag == "AVA purpose") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "new profile") { // COMPLETED
        vector<string> name = get_words(get_name_from_input(sentence));
        output = new_profile(name[0], name[1]);
        edit_output_file(number, output);
    }

    else if (tag == "delete attribute") { // COMPLETED
        vector<string> name = get_words(get_name_from_input(sentence));
        string attrName = get_verbal_input(number, "what is the attribute name?");
        output = delete_attribute(name[0], name[1], attrName);
        edit_output_file(number, output);
    }

    else if (tag == "login") { // COMPLETED 
        edit_output_file(number, "login - file output");
    }

    else if (tag == "get profile count") { // NEEDS CHECKING
        output = get_profile_count();
        edit_output_file(number, output);
    }

    else if (tag == "how are you") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "AVA birthday") { // COMPLETED 
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "AVA home") { // COMPLETED 
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "change profile name") { // NEEDS CHECKING
        vector<string> name = get_words(get_name_from_input(sentence));
        string newFirst = get_verbal_input(number, "what is the new first name?");
        string newLast = get_verbal_input(number, "what is the new last name?");
        output = change_profile_name(name[0], name[1], newFirst, newLast);
        edit_output_file(number, output);
    }

    else if (tag == "AVA name") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "goodbye") { // COMPLETED 
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }
    
    else if (tag == "logout") { // COMPLETED 
        edit_output_file(number, "logout - file output");
    }

    else if (tag == "gender") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "favorite color") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "do you understand") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "more skills") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "do you like me") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "you suck") { // COMPLETED
        output = get_from_response_file(tag);
        edit_output_file(number, output);
    }

    else if (tag == "random") { // COMPLETED
        edit_output_file(number, "random - file output");
    }

    else if (tag == "boot") { // COMPLETED
        edit_output_file(number, "boot");
    }

    else if (tag == "day of week") { // NEEDS CHECKING
        output = time.get_day_of_week();
        edit_output_file(number, output);
    }

    else if (tag == "month") { // NEEDS CHECKING
        output = time.get_month();
        edit_output_file(number, output);
    }

    else if (tag == "day number") { // NEEDS CHECKING
        output = time.get_day_number();
        edit_output_file(number, output);
    }

    else if (tag == "time") { // NEEDS CHECKING
        output = time.get_text_time();
        edit_output_file(number, output);
    }

    else if (tag == "hour") { // NEEDS CHECKING
        output = time.get_hour();
        edit_output_file(number, output);
    }

    else if (tag == "minute") { // NEEDS CHECKING
        output = time.get_minute();
        edit_output_file(number, output);
    }

    else if (tag == "second") { // NEEDS CHECKING
        output = time.get_second();
        edit_output_file(number, output);
    }

    else if (tag == "year") { // NEEDS CHECKING
        output = time.get_year();
        edit_output_file(number, output);
    }

    else if (tag == "day") { // NEEDS CHECKING
        output = time.get_day();
        edit_output_file(number, output);
    }

    else if (tag == "") {
        edit_output_file(number, output);
    } 

    add_to_archive(sentence, output);

    return number;

}


/* -------------------------------------------------------------------------- */
/*                              Main Python Call                              */
/* -------------------------------------------------------------------------- */


int main() { // COMPLETED
    system("/usr/bin/python3 /home/pi/Desktop/A.V.A/main.py");
}


/* -------------------------------------------------------------------------- */
/*                           C++ Function Exporting                           */
/* -------------------------------------------------------------------------- */


extern "C" { // COMPLETED
    int get_response_so(int number) {return get_response(number);}
}







/* -------------------------------------------------------------------------- */
/*                                  Includes                                  */
/* -------------------------------------------------------------------------- */


#include "speech_documentation.h"

Time timeClass;


/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


/* ----------------------------- Other Functions ---------------------------- */

string simplify_date(string date) { // COMPLETED

    string output = "";

    //----------Months----------//

    if (date == "january") {
        output = "Jan";
    } 
    else if (date == "febuary") {
        output = "Feb";
    }
    else if (date == "march") {
        output = "Mar";
    }
    else if (date == "april") {
        output = "Apr";
    }
    else if (date == "may") {
        output = "May";
    }
    else if (date == "june") {
        output = "Jun";
    }
    else if (date == "july") {
        output = "Jul";
    }
    else if (date == "august") {
        output = "Aug";
    }
    else if (date == "september") {
        output = "Sep";
    }
    else if (date == "october") {
        output = "Oct";
    }
    else if (date == "november") {
        output = "Nov";
    }
    else if (date == "december") {
        output = "Dec";
    }

    //----------Days----------//

    if (date == "monday") {
        output = "Mon";
    }
    if (date == "tuesday") {
        output = "Tue";
    }
    if (date == "wednesday") {
        output = "Wed";
    }
    if (date == "thursday") {
        output = "Thu";
    }
    if (date == "friday") {
        output = "Fri";
    }
    if (date == "saturday") {
        output = "Sat";
    }
    if (date == "sunday") {
        output = "Sun";
    }

    return output;

}

bool check_for_archive_file(string date) { // COMPLETED

    date = timeClass.get_speech_archive_file_name(date);

    string fPath = "/home/pi/Desktop/A.D.A/STORAGE/speech_archives" + date + ".txt";
    ifstream f(fPath);
    return f.good();

}

/* --------------------------- Adding to Archives --------------------------- */

void add_to_archive(string userInput, string AVAOutput) { // COMPLETED

    string date = timeClass.get_ctime();

    string output = date + ":" + userInput + ":" + AVAOutput;

    if (!check_for_archive_file(date)) {
        create_archive_file();
    }

    date = timeClass.get_speech_archive_file_name(date);

    string fPath = "/home/pi/Desktop/A.D.A/STORAGE/speech_archives" + date + ".txt";

    add_line_to_file(fPath, output);

}

/* -------------------------- Getting from Archives ------------------------- */

string get_from_archive(string year = "", string month = "", string day = "", string dayOfWeek = "", string hour = "", string minute = "", string second = "") { // NOT STARTED
    
    
    
    return "";
}

vector<string> get_range_from_archive(string startDate, string endDate) { // NOT STARTED
    vector<string> output;
    return output;
}

string get_archive_file_path(string date) { // NOT STARTED
    return "";
}

/* ---------------------------- Creating Archives --------------------------- */

void create_archive_file() { // COMPLETED

    string date = timeClass.get_speech_archive_file_name(timeClass.get_ctime());

    string fPath = "/home/pi/Desktop/A.D.A/STORAGE/speech_archives" + date + ".txt";

    ofstream f(fPath);
    f.close();
}

/* ---------------------------- Deleting Archives --------------------------- */

void delete_archive_file(string date) { // NOT STARTED

}

void delete_from_archive_file(string date, string removeTime) { // NOT STARTED

}

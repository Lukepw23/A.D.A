#include <iostream>
#include <ctime>
#include <string>
#include <vector>

using namespace std;

class Time {

    public:

        void refresh_time(); // COMPLETED

        string get_speech_archive_file_name(string date); // COMPLETED

        string month_unabriviation(string month); // COMPLETED
        string day_unabriviation(string day); // COMPLETED
        string day_number_unabriviation(string number); // COMPLETED

        string day_of_week(); // COMPLETED
        string month(); // COMPLETED
        string day_number(); // COMPLETED
        string hour(); // COMPLETED
        string minute(); // COMPLETED
        string second(); // COMPLETED
        string year(); // COMPLETED

        string get_ctime(); // COMPLETED
        string get_day_of_week(); // COMPLETED
        string get_month(); // COMPLETED
        string get_day_number(); // COMPLETED
        string get_time(); // COMPLETED
        string get_hour(); // COMPLETED
        string get_minute(); // COMPLETED
        string get_second(); // COMPLETED
        string get_year(); // COMPLETED

        string get_day(); // COMPLETED
        string get_text_time(); // COMPLETED

};
#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>

using namespace std;

#include "/home/pi/Desktop/A.D.A/Modules/file_management/file_management.h"
#include "/home/pi/Desktop/A.D.A/Modules/time/time.h"


/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


/* ----------------------------- Other Functions ---------------------------- */

string simplify_date(string date); // COMPLETED

bool check_for_archive_file(string date); // COMPLETED

/* --------------------------- Adding to Archives --------------------------- */

void add_to_archive(string userInput, string ADAOutput); // COMPLETED

/* -------------------------- Getting from Archives ------------------------- */

string get_from_archive(string year, string month, string day, string dayOfWeek, string hour, string minute, string second); // NOT STARTED

vector<string> get_range_from_archive(string startDate, string endDate); // NOT STARTED

string get_archive_file_path(string date); // NOT STARTED

/* ---------------------------- Creating Archives --------------------------- */

void create_archive_file(); // COMPLETED

/* ---------------------------- Deleting Archives --------------------------- */

void delete_archive_file(string date); // NOT STARTED

void delete_from_archive_file(string date, string removeTime); // NOT STARTED
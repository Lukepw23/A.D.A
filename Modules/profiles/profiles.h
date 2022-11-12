#include <iostream>
#include <fstream>
#include <vector>
#include "/home/pi/Desktop/A.D.A/Modules/file_management/file_management.h"

using namespace std;

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */


/* --------------------------- Assistant Functions -------------------------- */

string to_lowercase(string word); // COMPLETED

/* --------------------------- Main User Functions -------------------------- */

string new_profile(string first, string last); // COMPLETED

string delete_profile(string first, string last); // COMPLETED

string change_profile_name(string oldFirst, string oldLast, string newFirstName, string newLastName); // COMPLETED

string add_attribute(string firstName, string lastName, string attributeName, string attributeValue); // COMPLETED

string delete_attribute(string firstName, string lastName, string attributeName); // COMPLETED

string change_attribute(string firstName, string lastName, string attributeName, string attributeValue); // COMPLETED

string get_profile_count(); // IN PROGRESS

string get_profile_folder_path(string first, string last); // COMPLETED

string get_attribute_file_path(string first, string last); // COMPLETED

string get_attribute(string first, string last, string attributeName); // COMPLETED

string get_attribute_count(string first, string last); // COMPLETED

string check_profile_exists(string first, string last); // COMPLETED

string get_name(string firstName, string lastName, string type); // COMPLETED

bool bool_check_profile_exists(string first, string last); // COMPLETED

/* ---------------------------- Family Functions ---------------------------- */

string new_family(string familyName); // COMPLETED

string delete_family(string familyName); // COMPLETED

string change_family_name(string oldName, string newName); // COMPLETED

string add_family_member(string familyName, string profileName);

string remove_family_member(string familyName, string profileName);

string move_family_member(string profileName, string oldFamilyName, string newFamilyName);

string edit_member_role(string profileName, string familyName, string newRole);



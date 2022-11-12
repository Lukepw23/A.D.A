#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


/* ------------------------------ Reading files ----------------------------- */

vector<string> read_from_file(string filePath); // COMPLETED

/* ---------------------------- Writing to Files ---------------------------- */

void write_to_file(string filePath, vector<string> newFileContents); // COMPLETED

void add_line_to_file(string filePath, string newItem); // COMPLETED

/* --------------------------- Deleting from Files -------------------------- */

void delete_line_from_file(string filePath, string removeItem); // COMPLETED

/* ----------------------------- Other Functions ---------------------------- */

string get_dictionary_value(string filePath, string attributeName); // COMPLETED


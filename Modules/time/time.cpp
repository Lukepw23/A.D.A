/* -------------------------------------------------------------------------- */
/*                                  Includes                                  */
/* -------------------------------------------------------------------------- */


#include "time.h"


/* -------------------------------------------------------------------------- */
/*                                  Functions                                 */
/* -------------------------------------------------------------------------- */


string date;

/* --------------------------------- Refresh -------------------------------- */

void Time::refresh_time() { // COMPLETED
    time_t secondsTime = time(NULL);
    date = ctime(&secondsTime);
}

/* -------------------------------- Archiving ------------------------------- */

string Time::get_speech_archive_file_name(string date) { // COMPLETED

    string day = date.substr(0, 10);
    string year = date.substr(19, 5);

    string out = day + year;

    return out;

}

/* ------------------------------ Abriviations ------------------------------ */

string Time::month_unabriviation(string month) { // COMPLETED

    string output;

    if (date == "Jan") {
        output = "January";
    } 
    else if (date == "Feb") {
        output = "Febuary";
    }
    else if (date == "Mar") {
        output = "March";
    }
    else if (date == "Apr") {
        output = "April";
    }
    else if (date == "May") {
        output = "May";
    }
    else if (date == "Jun") {
        output = "June";
    }
    else if (date == "Jul") {
        output = "July";
    }
    else if (date == "Aug") {
        output = "August";
    }
    else if (date == "Sep") {
        output = "September";
    }
    else if (date == "Oct") {
        output = "October";
    }
    else if (date == "Nov") {
        output = "November";
    }
    else if (date == "Dec") {
        output = "December";
    }

    return output;

}

string Time::day_unabriviation(string day) { // COMPLETED

    string output;

    if (date == "Mon") {
        output = "Monday";
    }
    else if (date == "Tue") {
        output = "Tuesday";
    }
    else if (date == "Wed") {
        output = "Wednesday";
    }
    else if (date == "Thu") {
        output = "Thursday";
    }
    else if (date == "Fri") {
        output = "Friday";
    }
    else if (date == "Sat") {
        output = "Saturday";
    }
    else if (date == "Sun") {
        output = "Sunday";
    }

    return output;

}

string Time::day_number_unabriviation(string number) { // COMPLETED
    if (number == "1") return "first";
    else if (number == "2") return "second";
    else if (number == "3") return "third";
    else if (number == "4") return "fourth";
    else if (number == "5") return "fifth";
    else if (number == "6") return "sixth";
    else if (number == "7") return "seventh";
    else if (number == "8") return "eighth";
    else if (number == "9") return "ninth";
    else if (number == "10") return "tenth";
    else if (number == "11") return "eleventh";
    else if (number == "12") return "twelfth";
    else if (number == "13") return "thirteenth";
    else if (number == "14") return "fourteenth";
    else if (number == "15") return "fifteenth";
    else if (number == "16") return "sixteenth";
    else if (number == "17") return "seventeenth";
    else if (number == "18") return "eighteenth";
    else if (number == "19") return "nineteenth";
    else if (number == "20") return "twentieth";
    else if (number == "21") return "twenty first";
    else if (number == "22") return "twenty second";
    else if (number == "23") return "twenty third";
    else if (number == "24") return "twenty fourth";
    else if (number == "25") return "twenty fifth";
    else if (number == "26") return "twenty sixth";
    else if (number == "27") return "twenty seventh";
    else if (number == "28") return "twenty eighth";
    else if (number == "29") return "twenty ninth";
    else if (number == "30") return "thirtieth";
    else if (number == "31") return "thirty first";
    else { return "";}
}

/* ------------------------------- ctime gets ------------------------------- */

string Time::get_ctime() { // COMPLETED

    refresh_time();

    string out;

    for (int i = 0; i < (date.length()); i++) {

        if (date[i] == ' ') {
            out.push_back('-');
        }
        else {
            out.push_back(date[i]);
        }

    }

    out.erase((out.length()-1), 1);

    return out;

}

string Time::get_time() { // COMPLETED
    refresh_time();
    return get_ctime().substr(11,8);
}

/* ----------------------- subscripting time and date ----------------------- */

string Time::day_of_week() { // COMPLETED
    refresh_time();
    return get_ctime().substr(0,3);
}

string Time::month() { // COMPLETED
    refresh_time();
    return get_ctime().substr(4,3);
}

string Time::day_number() { // COMPLETED
    refresh_time();
    return get_ctime().substr(8,2);
}

string Time::hour() { // COMPLETED
    refresh_time();
    return get_ctime().substr(11,2);
}

string Time::minute() { // COMPLETED
    refresh_time();
    return get_ctime().substr(14,2);
}

string Time::second() { // COMPLETED
    refresh_time();
    return get_ctime().substr(17,2);
}

string Time::year() { // COMPLETED
    refresh_time();
    return get_ctime().substr(20,4);
}

/* -------------------------------- ADA gets -------------------------------- */

string Time::get_day_of_week() { // COMPLETED
    return "it is " + day_of_week();
}

string Time::get_month() { // COMPLETED
    return "it is " + month();
}

string Time::get_day_number() { // COMPLETED
    return "it is the " + day_number_unabriviation(day_number());
}

string Time::get_hour() { // COMPLETED
    return "it is hour " + hour();
}

string Time::get_minute() { // COMPLETED
    return "it is minute " + minute();
}

string Time::get_second() { // COMPLETED
    return "it is second " + second();
}

string Time::get_year() { // COMPLETED
    return "it is " + year();
}

string Time::get_day() { // COMPLETED

    return "it is " + day_unabriviation(get_day_of_week()) + " " + month_unabriviation(get_month()) + " " + get_day_number() + ", " + get_year();

}

string Time::get_text_time() { // COMPLETED

    return "it is " + get_time().substr(0,5) + " and " + get_second() + " seconds";

}




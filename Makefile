o_files/ADA: Modules/file_management/o_files/file_management.o Modules/math/o_files/math.o Modules/reminders/o_files/reminders.o Modules/schedule/o_files/schedule.o Modules/security/o_files/security.o Modules/time/o_files/time.o o_files/main.o Modules/profiles/o_files/profiles.o Modules/speech_documentation/o_files/speech_documentation.o
	gcc -std=c++11 Modules/file_management/o_files/file_management.o Modules/math/o_files/math.o Modules/reminders/o_files/reminders.o Modules/schedule/o_files/schedule.o Modules/security/o_files/security.o Modules/time/o_files/time.o o_files/main.o Modules/profiles/o_files/profiles.o Modules/speech_documentation/o_files/speech_documentation.o  -o o_files/ADA	
	gcc -std=c++11 -shared -W1,-soname,o_files/mainLib.so -o o_files/mainLib.so  Modules/file_management/o_files/file_management.o Modules/math/o_files/math.o Modules/reminders/o_files/reminders.o Modules/schedule/o_files/schedule.o Modules/security/o_files/security.o Modules/time/o_files/time.o o_files/main.o Modules/profiles/o_files/profiles.o Modules/speech_documentation/o_files/speech_documentation.o

o_files/main.o: main.cpp
	gcc -std=c++11 -c main.cpp -o o_files/main.o
	gcc -std=c++11 -c -fPIC main.cpp -o o_files/main.o
	
Modules/profiles/o_files/profiles.o: Modules/profiles/profiles.cpp
	gcc -std=c++11 -c Modules/profiles/profiles.cpp -o Modules/profiles/o_files/profiles.o

Modules/security/o_files/security.o: Modules/security/security.cpp
	gcc -std=c++11 -c Modules/security/security.cpp -o Modules/security/o_files/security.o

Modules/math/o_files/math.o: Modules/math/math.cpp
	gcc -std=c++11 -c Modules/math/math.cpp -o Modules/math/o_files/math.o

Modules/list/o_files/list.o: Modules/list/list.cpp
	gcc -std=c++11 -c Modules/list/list.cpp -o Modules/list/o_files/list.o

Modules/file_management/o_files/file_management.o: Modules/file_management/file_management.cpp
	gcc -std=c++11 -c Modules/file_management/file_management.cpp -o Modules/file_management/o_files/file_management.o

Modules/reminders/o_files/reminders.o: Modules/reminders/reminders.cpp
	gcc -std=c++11 -c Modules/reminders/reminders.cpp -o Modules/reminders/o_files/reminders.o

Modules/schedule/o_files/schedule.o: Modules/schedule/schedule.cpp
	gcc -std=c++11 -c Modules/schedule/schedule.cpp -o Modules/schedule/o_files/schedule.o

Modules/time/o_files/time.o: Modules/time/time.cpp
	gcc -std=c++11 -c Modules/time/time.cpp -o Modules/time/o_files/time.o

Modules/speech_documentation/o_files/speech_documentation.o: Modules/speech_documentation/speech_documentation.cpp
	gcc -std=c++11 -c Modules/speech_documentation/speech_documentation.cpp -o Modules/speech_documentation/o_files/speech_documentation.o

clean:
	rm *.o ADA
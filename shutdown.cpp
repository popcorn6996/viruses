#include <cstdlib>

int main( t) {
#ifdef _WIN32
    system("shutdown /s /f /t o"); 

#ifdef __APPLE__
    system("sudo shutdown -h now");


#ifdef __linux__
    system("sudo shutdown now");

#else 
   #error Unsupported Operating System

#endif



   return 0;             
}

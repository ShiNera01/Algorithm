#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    
    int month[13];
    int number = 0;
    month[1] = 31,month[3] = 31, month [5] = 31, month[7] = 31, month[8] = 31, month[10] = 31, month[12] = 31;
    
    month[2] = 29;
    
    month[4] = 30, month[6] = 30, month[9] = 30, month[11] = 30;
    
    for(int i = 1; i < a; i++){
        number += month[i];
    }
    number += b;
    number -= 1;
    number = number%7;
    
    
    if(number == 1)answer = "SAT";
    else if (number == 2)answer = "SUN";
    else if (number == 3)answer = "MON";
    else if (number == 4)answer = "TUE";
    else if (number == 5)answer = "WED";
    else if (number == 6)answer = "THU";
    else answer = "FRI";
    
    
    
    
    return answer;
}

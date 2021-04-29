#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int number = x;
    int divisor = 0;
    while(number >= 10){
        divisor += number%10;
        number /= 10;
    }
    divisor += number;
    
    if(x % divisor == 0){}
    else answer = false;

    return answer;
}

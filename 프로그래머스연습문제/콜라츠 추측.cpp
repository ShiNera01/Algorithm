#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    int index = 0;
    long long number = num;
    while(index < 500){
        if(number == 1)break;
        if(number % 2 == 0)number/=2;
        else number = (number * 3) + 1;
        answer++;
        index++;
        
        
    }
    
    if(number != 1)answer = -1;
    return answer;
}

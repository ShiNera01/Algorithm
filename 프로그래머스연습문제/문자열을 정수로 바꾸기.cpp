#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solution(string s) {
    int answer = 0;
    int mark = 1;
    int number = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == '-')mark = -1;
        
        else if (s[i] == '+')mark = 1;
        
        else{
            number = s[i] - '0';
            answer +=  number * pow(10,(s.size()-i-1));
        }
    }
    answer = answer * mark;
    return answer;
}

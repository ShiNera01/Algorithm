#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    long long temp = 0;
    if(a<=b) {}
    else {
        temp = a;
        a = b;
        b = temp;
    }
    
    for(long long int i = a; i <= b; i++){
        answer += i;
    }
    
    return answer;
}

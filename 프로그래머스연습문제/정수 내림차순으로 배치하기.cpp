#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

bool compare(int a, int b){
    
    return b < a;
}

long long solution(long long n) {
    long long answer = 0;
    vector<long long int> number;
    
    while (n>=10){
        number.push_back(n%10);
        n = n/10;
    }
    number.push_back(n);
    
    sort(number.begin(), number.end(),compare);
    
    for(long long int i = 0; i < number.size(); i++){
        answer += number[i] * pow(10,number.size()-i-1);
    }
    
    return answer;
}

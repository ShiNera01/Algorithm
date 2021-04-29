#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(char a, char b){
    
    if(a >= 'A' && a <='Z' && b >= 'A' && b <='Z') return a > b;
    
    else if(a >= 'A' && a <='Z' && b >= 'a' && b <='z') return false;
    
    else if(a >= 'a' && a <='z' && b >= 'A' && b <='Z') return true;
    
    else{
        return a > b;
    }
}

string solution(string s) {
    string answer = "";
    sort(s.begin(),s.end(),compare);
    answer = s;
    
    
    return answer;
}

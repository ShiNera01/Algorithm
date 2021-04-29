#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = true;
    
    if(s.size() == 6 || s.size() == 4){}
    else return answer = false;
    
    for(int i = 0; i < s.size(); i++){
        if(s[i] >= '0' && s[i] <= '9'){}
        else {
            answer = false;
            break;
        }
        
    }
    
    return answer;
}

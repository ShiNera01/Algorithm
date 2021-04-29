#include <string>
#include <vector>


using namespace std;

string solution(string s, int n) {
    string answer = "";
  
    for(int i = 0; i < s.size(); i++){
        
        if(s[i] >= 'a' && s[i] <= 'z' && s[i] + n > 'z'){
            s[i] = 'a' + (n-('z' -s[i] + 1));
      
        }
        else if (s[i] >= 'A' && s[i] <= 'Z' && s[i] + n > 'Z'){
            s[i] = 'A' + (n-('Z' - s[i] + 1));
            
        }
        else if(s[i] == ' '){}
        
        else s[i] = s[i] + n;
    
        
        answer += s[i];
    }
    
    
    return answer;
}

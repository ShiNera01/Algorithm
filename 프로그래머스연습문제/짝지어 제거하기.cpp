#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string s)
{
    int answer = 0;
    
    vector <char> st;
 
    for(int i = 0; i < s.size(); i++){
        if(st.empty()){
            st.push_back(s[i]);
        }
        else{
            if(st.back() == s[i]){
                st.pop_back();

            }
            else{
                st.push_back(s[i]);
            }
        }
    }
    
  
    if(st.empty())answer = 1;
    else answer = 0;
    

    return answer;
}

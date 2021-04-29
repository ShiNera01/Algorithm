#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    
    vector <int> a = {1,2,3,4,5};
    vector <int> b = {2,1,2,3,2,4,2,5};
    vector <int> c = {3,3,1,1,2,2,4,4,5,5};
    
    vector <int> ans = answers;
    vector<int> answer;
    
    int a_count = 0;  
    int b_count = 0;  
    int c_count = 0;  
    
    int a_size = a.size(); //5
    int b_size = b.size(); //8
    int c_size = c.size(); //10
    int ans_size = ans.size();
    
    int j = 0;
    for(int i = 0; i < ans_size; i++){
        if(a[j] == ans[i]) a_count++;
        
        j++;
        
        if(j == a_size ) j = j - a_size ;
            
            
    
    }
    
    j = 0; 
    for(int i = 0; i < ans_size; i++){
        if(b[j] == ans[i]) b_count++;
        j++;
        if(j == b_size) j = j - b_size;
   
    }
    
    j = 0; 
    for(int i = 0; i < ans_size; i++){
        if(c[j] == ans[i]) c_count++;
        j++;
        if(j == c_size) j = j - c_size;
    
    }   
    
    if(a_count >= b_count && a_count >= c_count) answer.push_back(1);
    
    if(b_count >= a_count && b_count >= c_count) answer.push_back(2);
    
    if(c_count >= a_count && c_count >= b_count) answer.push_back(3);
    
    
    
    
    
    return answer;
}

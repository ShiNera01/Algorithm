#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<int> array;
    vector<pair<int, vector<int>>> pa;
    
    int num = 0;
    for(int i = 0; i < s.size(); i++){
        
        if(s[i] == '{')continue;
        
        else if(s[i] == '}'){
            if(s[i - 1] == '}')continue;
            else {
                array.push_back(num);
                pa.push_back(make_pair(array.size(), array));
                num = 0;
                array.clear();
            }
            
        }
        else if(s[i] == ','){
            if(s[i-1] == '}')continue;
            else {
                array.push_back(num);
                num = 0;
            }
        }
        else{
            num = num * 10;
            num += s[i] - '0';
        }
    }
    
    sort(pa.begin(), pa.end());
    set<int> ans;
        
    for(pair<int, vector<int>> ex: pa){
        for(int j:ex.second){
            if(ans.find(j) == ans.end()){
                ans.insert(j);
                answer.push_back(j);
            }
        }
    }
    
    
    
    
    return answer;
}

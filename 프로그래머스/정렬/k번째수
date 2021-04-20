#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    vector<int> new_array;
    
    for(int i = 0; i < commands.size(); i++){
        
        for (int j = commands[i][0] - 1; j <= commands[i][1] - 1 ; j++){
            
            new_array.push_back(array[j]);
        }
        sort(new_array.begin(), new_array.end());
        
        answer.push_back(new_array[commands[i][2] - 1]);
            
        new_array.clear();
    }
    
    
    
    
    
    
    
    return answer;
}

#include <string>
#include <vector>


using namespace std;

int index = 0;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    string temp ="";
    for(int i = 1; i < strings.size(); i++){
        int j = i;
        
        while (j  > 0 && strings[j-1][n] >= strings[j][n]){
            if(strings[j-1][n] > strings[j][n]){
                temp = strings[j-1];
                strings[j-1] = strings[j];
                strings[j] = temp;
            }
            else if(strings[j-1][n] == strings[j][n]){
                if(strings[j-1] > strings[j]){
                temp = strings[j-1];
                strings[j-1] = strings[j];
                strings[j] = temp;
                }
            }
            j--;
        }
        
        
    }
    for(int i = 0; i < strings.size(); i++){
        answer.push_back(strings[i]);
    }
    
    
    return answer;
}

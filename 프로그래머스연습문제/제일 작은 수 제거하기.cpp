#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int index = 0;
    int min = arr[0];
    
    if(arr.size() == 1){
        answer.push_back(-1);
        return answer;
    }
    
    for(int i = 1; i < arr.size(); i++){
        if(arr[i] < min) {
            index = i;
            min = arr[i];
         }
    }
    
    for(int i = 0; i < arr.size(); i++){
        if(i == index)continue;
        else answer.push_back(arr[i]);
    }
    
    
    return answer;
}

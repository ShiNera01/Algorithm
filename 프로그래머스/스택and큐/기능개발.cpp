#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    vector <int> success;
    
    for(int i = 0; i < progresses.size(); i++){
        int number = 0;
        number = (100 - progresses[i]) / speeds[i];
        
        if((100 - progresses[i]) % speeds[i] != 0)number++;
        success.push_back(number);
    }
    int index = 1;
    int standard = success[0];
    int count = 1;
    while (index < success.size()){
        if(success[index] <= standard){
            index++;
            count++;
        }
        else{
            answer.push_back(count);
            standard = success[index];
            index++;
            count = 1;
        }
        
        if (index == success.size() && standard < success[index-1])answer.push_back(1);
        else if(index == success.size() && standard >= success[index-1])answer.push_back(count);
    }
    
    return answer;
}

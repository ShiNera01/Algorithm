#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int count = 0;
    int number = 0;
    for(int i = 0; i < lottos.size(); i++){
        for(int j = 0; j < win_nums.size(); j++){
            if(lottos[i] == 0){
                count++;
                break;
            }
            else if(lottos[i] == win_nums[j])number++;
            
        }
    }
    
    if(number == 6){
        answer.push_back(1);
        answer.push_back(1);
    }

    
    else{
        answer.push_back(7-number-count);
        answer.push_back(7-number);
    }

    if (answer[0] == 7)answer[0] = 6;
    if (answer[1] == 7)answer[1] = 6;
    
    
    return answer;
}

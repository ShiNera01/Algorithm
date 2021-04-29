#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    
    for(int i = 0; i < prices.size() - 1; i++){
        int number = 0;
        for(int j = i + 1; j < prices.size(); j++){
            if(prices[j] < prices[i]){
                number++;
                break;
            }
        number++;
        }
       answer.push_back(number); 
    }
    answer.push_back(0);
    return answer;
}

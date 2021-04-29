#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    vector<int> collect;
    for(int i = 0; i < numbers.size() - 1; i++){
        for(int j = i+1; j < numbers.size(); j++){
            collect.push_back(numbers[i]+numbers[j]);
        }
    }
    sort(collect.begin(), collect.end());
    answer.push_back(collect[0]);
    for(int i = 1; i < collect.size(); i++){
        if(collect[i-1] == collect[i]){}
        else answer.push_back(collect[i]);
    }
    
    return answer;
}

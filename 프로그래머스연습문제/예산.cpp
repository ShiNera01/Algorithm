#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    sort(d.begin(),d.end());
    int sum = 0;
    
    for(int i = 0; i < d.size(); i++){
        if(sum+d[i] > budget)break;
        else {

            sum += d[i];
            answer += 1;
        }
    }
    
    
    
    
    return answer;
}

#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solution(vector<int> people, int limit) {
    int answer = 0;
    int words[50000];
 	sort(people.begin(),people.end());
    
    int right = people.size() - 1;
    int left = 0;
    
    while(left <= right){
        if(people[left]+people[right] < limit){
            left++;
            right--;
            answer++;
        }
        else if(people[left]+people[right] == limit){
            answer++;
            left++;
            right--;
        }
        else if(people[left] + people[right] > limit){
            answer++;
            right--;
        }
        
        
        
    }
    
    
    return answer;
}

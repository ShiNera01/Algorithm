#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int count = 1;
    sort(nums.begin(),nums.end());
    
    for(int i = 1; i < nums.size(); i++){
        if(nums[i-1] == nums[i])continue;
        else count++;
    }
    
    if(count>=nums.size()/2)answer = nums.size()/2;
    else answer = count;
        

    return answer;
}

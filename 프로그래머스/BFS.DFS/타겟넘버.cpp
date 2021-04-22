#include <string>
#include <vector>

using namespace std;

int dfs(int pre, int index, int arr[], int target, int size){
    
    if(index >= size){
        if (target == pre) return 1;
        
        return 0;
    }
    int ans = 0;
    
    int cur_1 = pre + arr[index];
    int cur_2 = pre - arr[index];
    
    
    ans += dfs(cur_1,index+1,arr,target,size);
    ans += dfs(cur_2,index+1,arr,target,size);
    
    return ans;
    
    
}




int solution(vector<int> numbers, int target) {
  
    int answer = 0;
    int arr[21] = {0,};
    int current = numbers[0];
    
    for(int i = 0; i<numbers.size(); i++){
        arr[i] = numbers[i];
    }
    
    answer += dfs(current, 1, arr, target,numbers.size());
    answer += dfs(-current, 1, arr, target,numbers.size());
    
    return answer;
    
}

#include <string>
#include <vector>

using namespace std;



long long solution(int n, vector<int> times) {
    
    long long answer = 0, min_time = 1, max_time = times[times.size()-1] * (long long)n, count = 0,mid_time;
    
    while(min_time <= max_time){
        mid_time = (max_time + min_time)/2;
        
        for(int i = 0; i < times.size(); i++){
            count += mid_time/times[i];
        }
        
        if(n <= count){
            answer = mid_time;
            max_time = mid_time-1;
        }
        else min_time = mid_time + 1;
        
        count = 0;
        
        
        
        
    }
    
    

    
    return answer;
}

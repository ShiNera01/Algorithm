#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    int lost_number = lost.size();
    int reserve_number = reserve.size();
    for(int i = 0; i < lost.size(); i++){
        
        for(int j = 0; j < reserve.size(); j++){
            if(lost[i] == reserve[j]){
                lost[i] = 0;
                reserve[j] = -1;
                lost_number -= 1;
                reserve_number -= 1;
                break;
            }
        }
        
    }
    
    for(int i = 0; i < lost.size(); i++){
        if(lost_number == 0 || reserve_number == 0) break;
        if(lost[i] == 0 )continue;
        
        for(int j = 0; j < reserve.size(); j++){
            if(lost[i] - 1 == reserve[j]){
                lost[i] = 0;
                reserve[j] = -1;
                lost_number -=1;
                reserve_number -=1;
                break;
            }
            else if(lost[i] + 1 == reserve[j]){
                lost[i] = 0;
                reserve[j] = -1;
                lost_number -= 1;
                reserve_number -= 1;
                break;
            }
        }
        
        
        
        
        
    }
    
    
    
    
    
    int count = 0;
    for(int i = 0; i<lost.size();i++){
        if(lost[i] != 0)count++;
    }
    answer = n - count;
    

    return answer;
}

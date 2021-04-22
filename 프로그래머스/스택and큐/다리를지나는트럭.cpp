#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    queue <int> q;
    queue <int> bridge;
    int sum = 0;
    
    for(int i = 0; i < truck_weights.size(); i++){
        q.push(truck_weights[i]);
    }
    
    for(int i = 0; i < bridge_length; i++){
        bridge.push(0);
    }
    
    while(!q.empty() || !bridge.empty() ){
        sum = sum - bridge.front();
        bridge.pop();
        
        if(sum+q.front()<=weight && !q.empty()){
            sum+=q.front();
            bridge.push(q.front());
            q.pop();   
        }
        else if (!q.empty()){
            bridge.push(0);
        }

        
        answer += 1;
        
    }
    
    return answer;
}

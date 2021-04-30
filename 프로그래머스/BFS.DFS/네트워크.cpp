#include <string>
#include <vector>

using namespace std;
int visit[200];
int count = 0;
void dfs(vector<vector<int>> computers,int a){
    
    if(visit[a]) return;
    visit[a] = 1;
    for(int i = 0; i < computers[a].size(); i++){
        if(computers[a][i] == 1)dfs(computers, i);
    }
    
    
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for(int i = 0 ; i < computers.size(); i++){
        if(visit[i] == 0){
            dfs(computers, i);
            count++;
        }
        
    }
    
    answer = count;
    
    
    
    
    return answer;
}

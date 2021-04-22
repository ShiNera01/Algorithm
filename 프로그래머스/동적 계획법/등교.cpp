#include <string>
#include <vector>

using namespace std;

int visit[101][101] = {0,};
int number(int x, int y){
    
    if(x == 0)return 0;
    else if(y == 0)return 0;
    
    if(visit[x][y] > 0)return visit[x][y];
    else if(visit[x][y] == -1)return 0;
    
    
    return visit[x][y] = (number(x-1,y)%1000000007+number(x,y-1)%1000000007);
    
}

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    
    for (int i = 0; i < puddles.size(); i++){
            visit[puddles[i][0]][puddles[i][1]] = -1;  
    }
    
    for (int i = 2; i <= m; i++){
        if(visit[i][1] == 0)visit[i][1] = 1;
        else break;
    }
    for (int i = 2; i<=n; i++){
        if(visit[1][i] == 0)visit[1][i] = 1;
        else break;
    }
    
    
    answer = number(m,n)%1000000007;
    
    return answer;
}

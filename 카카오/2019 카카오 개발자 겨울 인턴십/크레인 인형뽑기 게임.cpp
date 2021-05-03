#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> lines ;
    int last = 0;
    
    for (int i = 0; i < moves.size(); i++){
        last = 0;
        
        for(int j = 0; j < board.size(); j++){
            if(board[j][moves[i]-1] == 0){}
            else {
                last = board[j][moves[i]-1];
                board[j][moves[i]-1] = 0;
                break;
            }
        }
        if(last ==0)continue;
       
        if(lines.size() == 0)lines.push_back(last);
        else if (lines.back() == last){
            answer += 2;
            lines.pop_back();
        }
        else{
            lines.push_back(last);
        }
        
        

    }
    
    
    
    return answer;
}

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int x , y = 0;
    int sum = brown + yellow;
    
    for (int i = 3; i < brown; i++){
        
       if(sum % i == 0 && sum/i > 2 ) {
           x = i;
           y = sum/i;
       } 
    
        if(2*x+2*y-4 == brown && x*y-2*x-2*y+4 == yellow)break;
    }
    int temp = 0;
    if (x < y){
        temp = y;
        y = x;
        x = temp;
    }
    answer.push_back(x);
    answer.push_back(y);
    
    return answer;
}

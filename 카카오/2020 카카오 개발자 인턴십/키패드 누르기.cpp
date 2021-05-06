#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    pair<int,int> left = make_pair(4,1);
    pair<int,int> right = make_pair(4,3);
    pair<int,int> middle;
    int left_dis = 0;
    int right_dis = 0;
    
    for (int i = 0; i < numbers.size(); i++){
        left_dis = 0;
        right_dis = 0;
        
        if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
            left.first = numbers[i] / 3 + 1;
            left.second = 1;
            answer += "L";
        }
        else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
            right.first = numbers[i] / 3;
            right.second = 3;
            answer += "R";
        }
        
        else{
            if(numbers[i] == 0){
                middle.first = 4;
                middle.second = 2;
            }
            else{
                middle.first = numbers[i]/3 + 1;
                middle.second = 2;
            }
            if(middle.first >= left.first){
                left_dis += middle.first - left.first;
            }
            else{
                left_dis += left.first - middle.first;
            }
            left_dis += middle.second - left.second;
            
            if(middle.first >= right.first){
                right_dis += middle.first - right.first;
            }
            else{
                right_dis += right.first - middle.first;
            }
            right_dis += right.second - middle.second;
            
            if(left_dis < right_dis){
                left.first = middle.first;
                left.second = middle.second;
                answer += "L";
            }
            else if(left_dis > right_dis){
                right.first = middle.first;
                right.second = middle.second;
                answer += "R";
            }
            else{
                if(hand == "right"){
                    right.first = middle.first;
                    right.second = middle.second;
                    answer += "R";
                }
                else{
                    left.first = middle.first;
                    left.second = middle.second;
                    answer += "L";
                    
                }
            }
            
        }
        
        
    }
    
    
    return answer;
}

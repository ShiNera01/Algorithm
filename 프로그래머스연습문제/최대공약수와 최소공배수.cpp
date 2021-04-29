#include <vector>
using namespace std;

vector <int> solution (int a,int b){
    vector<int> answer;
    int number = 0;
    int original_a = a;
    int original_b = b;
    int temp = 0;
    int lcd = 0;
    if(a > b){
        temp = b;
        b = a;
        a = temp;
    }
    
    while (b%a !=0){
        number = b%a;
        b = a;
        a = number;
    }
    answer.push_back(a);
    lcd = original_a * original_b / a;
    answer.push_back(lcd);
    

	return answer;
}

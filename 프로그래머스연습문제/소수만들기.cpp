#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

bool prime_number(int number){
    
    for(int i = 2; i <= sqrt(number); i++){
        if(number%i==0)return false;
    }
    return true;
}


int solution(vector<int> nums) {
    int answer = 0;
    int number = 0;
    
    for(int i = 0; i < nums.size()-2; i++){
        for(int j = i + 1; j < nums.size()-1; j++){
            for(int k = j + 1; k < nums.size(); k++){
                number = nums[i] + nums [j] + nums[k];
                cout << number <<endl;
                if(prime_number(number))answer++;

            }
        }
    }
    

    return answer;
}

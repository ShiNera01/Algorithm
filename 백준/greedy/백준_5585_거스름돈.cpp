#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main(){
	
	int number;
	int result = 0;
	
	cin >> number;
	
	
	
	if(number >= 500){
		result += number/500;
		number = number%500;
	}
	
	if(number >= 100){
		result += number/100;
		number = number%100;
	}	
	
	if(number >= 50){
		result += number/50;
		number = number%50;
	}	
	
	if(number >= 10){
		result += number/10;
		number = number%10;
	}	
	
	if(number >= 5){
		result += number/5;
		number = number%5;
	}	
	
	if (number > 0) {
		result +=number;
	}
	
	cout << result;
	
	return 0;
}
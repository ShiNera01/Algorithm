#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	
	vector <int> line;
	int number ;
	int result = 0;
	cin >> number;
	for (int i=0; i<number; i++){
		int a = 0;
		cin >> a;
		line.push_back(a);
		
	}
	sort(line.begin(),line.end());
	
	for (int i = 0; i < number; i++){
	
		result += line[i]*(number-i);
		
	}
	cout << result;

	return 0;
}
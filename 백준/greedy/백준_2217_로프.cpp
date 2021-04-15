#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	
	
	int n;
	int result = 0;
	vector <int> a;
	int max = 0;
	cin >> n;

	for (int i = 0; i < n; i++){
		int x = 0;
		cin >> x;
		a.push_back(x);
	}
	
	sort(a.begin(),a.end());
	
	for (int i = 0; i < n; i++){
		
		if(a[i]*(n-i) >= max){
			max = a[i] * (n-i);
		}
		
	}

	cout << max;

	return 0;
}
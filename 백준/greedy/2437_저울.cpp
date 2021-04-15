#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	

	int n;
	int arr[1001];
	int index = 1;
	
	cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> arr[i];
	}
	
	sort(arr+1,arr+(n+1));
	
	for (int i = 1; i <= n; i++){
		if(index < arr[i])break;
		index += arr[i];
		
		
	}
	cout << index;

	return 0;
}
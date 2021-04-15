#include <iostream>
using namespace std;

int main(){
	
	int N,K;
	int result = 0;
	int arr[10];
	cin >> N >> K;
	
	
	
	for (int i = 0; i < N; i++){
		cin >> arr[i];
	}
	
	for (int i = 1; i <= N; i++){
		if(K >= arr[N-i]){
		result += K/arr[N-i];
		K = K%arr[N-i];
		}
	}
	
	cout << result;
	
	return 0;
}
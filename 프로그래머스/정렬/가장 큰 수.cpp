#include <string>
#include <vector>
#include <algorithm>

using namespace std;


bool compare(string a, string b){
    return a+b > b+a;

}


string solution(vector<int> numbers) {
    string answer = "";
   
    vector<string> words;
    
    int words_size = numbers.size();
    
	for(int i = 0; i < words_size; i++){
		words.push_back(to_string(numbers[i]));
	}
    
	sort(words.begin(), words.end() , compare);	

    
	for(int i = 0; i < words_size; i++){
		answer = answer + words[i];
        
        
    
	}
    if(answer[0] == '0') answer = '0';
	
    
    return answer;
}

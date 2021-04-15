#include <string>
#include <vector>


using namespace std;

int solution(string name) {
    int answer = 0;
    
	vector <int> count;
	char standard ='A';
	char standard_z = 'Z';
	
	
	int index = 0; //현재 위치 
	int direct = 1; //오른쪽 방향으로 이동
	int search = 0; //탐색수 
	int visit[21] = {0,};
	
	for (int i = 1; i < name.size(); i++){
		if(name[i] == 'A'){
			count.push_back(1);
			visit[i] = 1;
		}
	}
	
	while(count.size() != name.size()){
	
	if(name[index] == 'A' && visit[index] == 0 ){
		count.push_back(1);
		visit[index] = 1;
	}		
	
	else{
	    search += min( (int)name[index]-(int)standard, (int)standard_z - (int)name[index] + 1);
	
	    count.push_back(1);
	
	    visit[index] = 1;
    }
	if(count.size() == name.size()) break;
	
	
	int index_right = index;
	int index_left = index;
	int right_count = 0;
	int left_count = 0;
	
	while(1){
		index_right += 1;
		right_count++;
		if(index_right >= name.size()) index_right = index_right - name.size();
		
	
		if(name[index_right] != 'A' && visit[index_right] == 0){
			break;	
		}
	
	}
	
	while(1){
		index_left -= 1;
		left_count++;
		if(index_left < 0) index_left = name.size() + index_left;
	
		if(name[index_left] != 'A' && visit[index_left] == 0){
			break;
		}
	}
	
	if(right_count <= left_count){
		index = index_right;
	}
	else index = index_left;
	
	search += min(right_count,left_count);
	
	}
    answer =search;
    
    return answer;
}
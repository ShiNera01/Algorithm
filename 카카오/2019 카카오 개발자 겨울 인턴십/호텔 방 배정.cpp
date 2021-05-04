#include <string>
#include <vector>
#include <map>
using namespace std;

map <long long ,long long int> m1;

long long get_parent(long long num){
    if(m1[num] == 0)return num;
    else return m1[num] = get_parent(m1[num]);
}

vector<long long> solution(long long k, vector<long long> room_number) {
    vector<long long> answer;
    
    for(long long num:room_number){
        long long room = get_parent(num);
        answer.push_back(room);
        m1[room] = room + 1;
        
    }
    
    
    
    return answer;
}

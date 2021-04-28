#include <string>
#include <vector>
#include <algorithm>


using namespace std;

string solution(string new_id) {
    string answer = "";
    
    for(int i = 0; i < new_id.size(); i++){
        new_id[i] = tolower(new_id[i]);
    }
    
    for (int i = 0; i < new_id.size(); i++){
        if(new_id[i] <= 'z' && new_id[i] >= 'a') continue;
        else if(new_id[i] >= '0' && new_id[i] <='9' )continue;
        else if(new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.')continue;
        else new_id[i] = ' ';
    }
    new_id.erase(remove(new_id.begin(),new_id.end(),' '), new_id.end());
    

    
    int index = 0;
    while(index < new_id.size()){
        if(new_id[index] == new_id[index+1] && new_id[index] == '.'){
            new_id = new_id.substr(0,index)+new_id.substr(index+1,new_id.size()-index-1);
        }
        else index++;
    }
    
    while(1){
        if(new_id[0] == '.')new_id = new_id.substr(1,new_id.size()-1);
        
        if(new_id[new_id.size()-1] == '.') new_id = new_id.substr(0,new_id.size()-1);
        
        if(new_id[0] != '.' && new_id[new_id.size() - 1] != '.')break;
    }
    
    if (new_id.size() == 0)new_id += 'a';
    
    if(new_id.size() >= 16)new_id = new_id.substr(0,15);
    while(new_id[new_id.size()-1] =='.')new_id = new_id.substr(0,new_id.size()-1);
    
    while (new_id.size() <=2 )new_id = new_id + new_id[new_id.size()-1];
    
    answer = new_id;
    
    return answer;
}

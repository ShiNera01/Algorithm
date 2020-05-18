T = int(input())
for i in range(T):
    value = 0
    date = input()
    
    if (int(date[4:6])<1 or int(date[4:6])>12) :
        value = -1
        
    elif(int(date[5])==2):
        
        if(int(date[6:])>28):
            value = -1
            
    elif (int(date[5])==4 or int(date[5])==6 or int(date[5])==9 or int(date[5])==11):
        if(int(date[6:])>30):
            value = -1
          
    elif (int(date[6:])>31):
        value = -1 
    
    if value == -1:
          print("#%d -1"%(i+1))
    else :
          print("#%d %s/%s/%s" %(i+1,date[:4],date[4:6],date[6:]))

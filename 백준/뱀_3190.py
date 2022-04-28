N = int(input())
K = int(input())
x,y = 1,1

apple = []
route = []
route_index = 0
body = [(1,1)]



direction = 0
time = 0

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(K):
    a,b = map(int,input().split())
    graph[a][b] = 1
    
L = int(input())

for i in range(L):
    a,b = input().split()
    route.append((a,b))
    
    
while True:
    
    time += 1
    if direction == 0:
        y += 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    else:
        x -= 1
    
    
    
    if x > N or y > N or x < 1 or y < 1 or (x,y) in body:
        break
    
    body.append((x,y))
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
    else:
        del body[0]

    
    
    if time == int(route[route_index][0]):
        
        if direction < 3 and route[route_index][1] == 'D':
            direction += 1
        elif direction == 3 and route[route_index][1] == 'D':
            direction = 0
        elif direction > 0 and route[route_index][1] == 'L':
            direction -= 1
        else:
            direction = 3

        if route_index + 1 < len(route):
          route_index += 1


print(time)

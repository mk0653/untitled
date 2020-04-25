import copy
map = [list(input()) for _ in range(10)]
temp = copy.deepcopy(map)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    temp[x][y] = "x"
    for n in range(4):
        mx = x + dx[n]
        my = y + dy[n]
        if 0<=mx<10 and 0<=my<10 and temp[mx][my] == "o":
            dfs(mx,my)
    return

def check():
    for n in range(10):
        for m in range(10):
            if temp[n][m] == "o":
                return False
    return True

for n in range(10):
    for m in range(10):
        temp = copy.deepcopy(map)
        dfs(n,m)
        if check() == True:
            print("YES")
            exit()

print("NO")
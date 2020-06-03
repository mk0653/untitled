n,m,x=map(int,input().split())
l=[]

for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
ans=99999999
for i in range(2 ** n):
    bag = []
    for j in range(n):  #bit全探索
        if ((i >> j) & 1):
            bag.append(l[j])
    skill=[0]*m
    enough=[0]*m #各スキルにつき、xを超えているかどうかを判断
    money=0
    for sub in bag:
        money+=sub[0]
        for kk in range(1,m+1):
            skill[kk-1]+=sub[kk]
            if skill[kk-1]>=x:
                enough[kk-1]+=1
    if 0 not in enough: #全てのスキルがxを超えていたら価格を計算
        if ans>money:
            ans=money#最低価格を下回っていたら更新
if ans==99999999: #初期値からの変更がなければ-1を、そうでなければ最低価格を出力
    print(-1)
else:
    print(ans)
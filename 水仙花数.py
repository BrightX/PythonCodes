print("水仙花数",end=':')
for i in range(100,1000,1):
    s = str(i)
    if pow(int(s[0]),3) + pow(int(s[1]),3) + pow(int(s[2]),3) == i:
        print(i,end=',')
# 暴力求解

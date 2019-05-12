s = input().split()
x = int(s[0])
f = s[1]
n = int(pow((x + 1)/2, 1/2))
y = x - 2 * n**2 + 1
for i in range(2*n - 1):
    if i < n:
        print(' '*i,end='')
        print(f*(2*(n-i)-1))
        
    elif i >= n:
        print(' '*(2*n-i-2),end='')
        print(f*(2*(i-n)+3))
        
print(y)

# 分解质因数
print("\n{:-^45}\n".format("分解质因数"))
E = True
while E:
    n = input("请输入一个正整数：")
    if n[0] == '-':
        continue
    for i in n:
        if i > '9'or i < '0':
            E = False
            break
    if E == False:
        print("\n{:-^30}\n".format("结束"))
        break
    n = int(n)
    if n <= 0:
        continue
    s = ''
    m = 0
    for i in range(2,n):
        if n%i == 0:
            k = 0
            for j in range(2,i):
                if i%j == 0:
                    k += 1
                    break
            if k == 0:
                x = n
                m += 1
                if m == 1:
                    s += str(i)
                else:
                    s += '*'+str(i)
                while (x/i)%i == 0:
                    s += '*'+str(i)
                    x /= i
    if s == '':
        s = '为质数'
    else:
        s = '=' + s
    print(str(n)+s+"\n")


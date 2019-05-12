from math import pi
i = 6
n = int(input("请输入一个大于等于12的6的倍数n："))
x = 1.0
s = 6 *pow(3, 1/2)/4
while (i <= n/2):
    h = pow(1 - pow(x/2, 2), 1/2)
    s += i * x *(1- h)/2
    x = pow(pow(x/2, 2)+ pow(1-h, 2), 1/2)
    i *= 2
print("n={}, s={},\n pi的参考值为：{}".format(n,s,pi)) # s为pi的近似值

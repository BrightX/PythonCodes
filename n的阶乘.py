n = eval(input("输入一个n:"))
sum = 1
for i in range(1 ,(n+1)):
    sum = sum * i
print("{}的阶乘为{}".format(n, sum))

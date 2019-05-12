def wp(n):
    for i in range(n):
        if i**2 == n:
            return True
            break

n = 0
while True:
    if wp(n+100)and wp(n+268):
        print(n)
        break
    n += 1

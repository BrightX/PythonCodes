s = input()
i = 0
while i <= 9:
    j = 0
    for k in s:
        if int(k)==i:
              j += 1
    if j!=0:
      print(str(i)+":"+str(j))
    i += 1

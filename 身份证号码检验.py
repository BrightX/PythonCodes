n = int(input())
x = 0
c = 0
m = ''
q = "7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2".split('，')
M = "1 0 X 9 8 7 6 5 4 3 2".split()
for i in range(n):
  s = input()
  a = 0
  b = 0
  for j in s[0:-1]:
    if j >='0' and j <= '9':
      b += int(j)*int(q[a])
      a += 1
    else:
      x += 1
  if x == 0 and M[b%11]== s[-1]:
    c += 1
  else:
    m = m + s + '\n'
if c == n:
  print("All passed")
else:
  print(m,end='')

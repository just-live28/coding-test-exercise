n, m = map(int, input().split())

result = 0
while n > 1:
  if n % m > 0:
    result += 1
    n -= 1
  else:
    result += 1
    n = n//m
print(result)
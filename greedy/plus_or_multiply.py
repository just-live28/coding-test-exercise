s = input()
sum = 0

for i in range(0, len(s)):
  num = int(s[i])
  
  if num <= 1 or sum <= 1:
    sum += num
  else:   
    sum *= num

print(sum)
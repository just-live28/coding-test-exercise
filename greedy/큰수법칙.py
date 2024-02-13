n, m, k = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort(reverse=True)
count = 0
k_limit = 0
result = 0

first_num, second_num = nlist[0], nlist[1]

while count < m :
  if k_limit != k:
    result += first_num
    k_limit += 1
    count += 1
  else:
    result += second_num
    k_limit = 0
    count += 1

print(result)
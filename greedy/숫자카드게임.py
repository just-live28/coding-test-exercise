n, m = map(int, input().split())
min_list = []

for _ in range(n):
  mlist = list(map(int, input().split()))
  # n줄만큼 m개의 카드가 나열되어있으므로, n번만큼 한 줄 씩 받아온다.
  min_num = 10001
  for i in mlist:
    if i < min_num:
      min_num = i
  min_list.append(min_num)
# 각 줄에서의 최솟값을 '최솟값 왕중왕전' 리스트(min_list)에 추가한다.

min_list.sort(reverse = True)
print(min_list[0])
# 범부들의 왕(그나마 제일 큰 친구)을 출력한다.
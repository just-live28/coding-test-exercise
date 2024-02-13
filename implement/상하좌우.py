n = int(input())
x, y = 1, 1
plans = input().split()
# 맵의 크기(n X n), 이동명령모음을 받는다. 초기좌표는 1,1로 설정.

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']
# 각 방향에 맞는 x방향, y방향의 짝 세트이다.

for plan in plans:
# 각 명령에 대해 이동을 한다.
  for i in range(len(dir)):
    if plan == dir[i]:
    # 방향들 만큼 for 문을 돌면서 맞는 방향을 찾는다. 찾은 뒤 그것에 맞는 이동을 한다.
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 그런데 주어진 맵을 벗어난다면 위에서 한 이동은 무효가 된다.
  x, y = nx, ny

print(x, y)
n, m, k = map(int,input().split())
nlist = list(map(int,input().split()))
nlist.sort(reverse=True)
first_num, second_num = nlist[0], nlist[1]

count = m // (k+1) * k + m % (k+1)
# 짱큰수 * k번 + 둘큰수 한번이 하나의 뭉탱이다. >> k+1
# 총 m번의 덧셈 중 뭉탱이는 m을 k+1로 나눈 몫만큼 나올 것이다. >> m // (k+1)
# 짱큰수의 덧셈 횟수(count)는 뭉탱이 당 k번이므로, >> m // (k+1) 이고,(딱 떨어졌을 경우에)
# m이 k+1로 나눠떨어지지 않았을 경우, 그 나머지만큼 짱큰수가 더 더해진다. >> + m % (k+1)
# 결론적으로, count는 위의 식과 같다.

result = count * first_num + (m - count) * second_num
# 둘큰수의 덧셈 횟수는 총 덧셈 횟수에서 count를 뺀 것이다. >> m - count
print(result)
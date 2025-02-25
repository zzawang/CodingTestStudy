import sys

n = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

answer = 0
min_num = price[0]
for i in range(1, n):
    answer += length[i - 1] * min_num
    min_num = min(min_num, price[i])

print(answer)
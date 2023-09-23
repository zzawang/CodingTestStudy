# 그리디 알고리즘
n = int(input())
sum = 1
count = 1
while sum <= n:
    count += 1
    sum += count
    
print(count - 1)
import sys

list1 = sys.stdin.readline().rstrip()
list2 = sys.stdin.readline().rstrip()
len1, len2 = len(list1), len(list2)
dp = [0] * (len2 + 1)
answer = 0

for i in range(1, len1 + 1):
    prev = 0
    for j in range(1, len2 + 1):
        tmp = dp[j]
        if list1[i - 1] == list2[j - 1]:
            dp[j] = prev + 1
            answer = max(answer, dp[j])
        else:
            dp[j] = 0
        prev = tmp

print(answer)
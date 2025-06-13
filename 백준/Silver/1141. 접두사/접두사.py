answer = n = int(input())
arr = sorted([input() for _ in range(n)], key=len)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j][:len(arr[i])]:
            answer -= 1
            break

print(answer)
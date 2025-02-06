import sys

def solution():
    n = int(sys.stdin.readline())
    arr = sorted(list(map(int, sys.stdin.readline().split())))

    min_sum = float('inf')
    answer = []

    for i in range(n - 2):  # 용액 하나는 고정
        start = i + 1
        end = n - 1

        while start < end:
            result = arr[i] + arr[start] + arr[end]
            min_sum = min(min_sum, abs(result))
            if abs(result) == min_sum:
                answer = [arr[i], arr[start], arr[end]]

            if result > 0:
                end -= 1
            elif result < 0:
                start += 1
            else:
                print(" ".join(str(a) for a in answer))
                return

    print(" ".join(str(a) for a in answer))

solution()
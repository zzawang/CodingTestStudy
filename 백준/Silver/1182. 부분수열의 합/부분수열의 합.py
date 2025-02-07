import sys

n, s = 0, 0
nums = []  # 수열
answer = 0  # 원소를 다 더한 값이 S인 부분 수열의 개수

def bt(idx, arr_sum, count): # 인덱스, 부분 수열의 합, 부분 수열에 포함된 수의 개수
    global n, s, nums, answer

    if idx == n:
        if arr_sum == s and count > 0: # 공집합은 포함 안되므로
            answer += 1
        return

    # 현재 인덱스의 값을 포함하는 경우
    bt(idx + 1, arr_sum + nums[idx], count + 1)
    # 현재 인덱스의 값을 포함하지 않는 경우
    bt(idx + 1, arr_sum, count)

def solution():
    global n, s, nums, answer
    n, s = map(int, sys.stdin.readline().split())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    bt(0, 0, 0)
    print(answer)

solution()
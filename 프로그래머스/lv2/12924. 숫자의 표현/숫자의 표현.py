def solution(n):
    answer = 1  # 자기 자신 추가

    left = 1
    right = 1
    sum = 1

    while left != n:
        if sum < n:
            right += 1
            sum += right
        elif sum > n:
            sum -= left
            left += 1
        else:
            answer += 1
            sum -= left
            left += 1

    return answer
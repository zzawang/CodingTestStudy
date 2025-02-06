n, m = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
answer = 0
current_sum = 0  # 누적 합 저장

while right < n:
    # right를 확장하면서 값 추가
    current_sum += nums[right]
    right += 1

    # 현재 합이 m을 초과하면 left를 이동하며 줄이기
    while current_sum > m and left < right:
        current_sum -= nums[left]
        left += 1

    # 원하는 합을 찾으면 정답 카운트 증가
    if current_sum == m:
        answer += 1

print(answer)

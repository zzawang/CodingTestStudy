T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    B = Q + (W-R)*S if W > R else Q
    print(f"#{t} {min(A, B)}")
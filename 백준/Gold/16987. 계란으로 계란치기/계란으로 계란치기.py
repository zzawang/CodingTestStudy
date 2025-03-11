import sys

answer = 0
def back_tracking(depth):
    global answer

    if depth == N:
        result = 0
        for d, w in eggs:
            if d <= 0:
                result += 1
        answer = max(answer, result)
        return


    if eggs[depth][0] <= 0:  # 현재 들고있는 계란이 깨졌을때
        back_tracking(depth + 1)
    else:
        is_all_broken = True
        for i in range(N):  # 다른 계란 중 하나
            if i != depth and eggs[i][0] > 0:
                is_all_broken = False
                # 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
                eggs[i][0] -= eggs[depth][1]
                eggs[depth][0] -= eggs[i][1]
                # 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행
                back_tracking(depth + 1)
                eggs[i][0] += eggs[depth][1]
                eggs[depth][0] += eggs[i][1]

        if is_all_broken:  # 현재 들고 있는 계란 빼고 다 깨졌을 때
            back_tracking(N)

# 계란의 수
N = int(sys.stdin.readline().rstrip())
eggs = []
for _ in range(N):
    # 계란의 내구도와 무게
    durability, weight = map(int, sys.stdin.readline().rstrip().split())
    eggs.append([durability, weight])

back_tracking(0)
print(answer)
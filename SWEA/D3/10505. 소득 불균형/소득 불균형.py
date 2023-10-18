for tc in range(1, int(input()) + 1):
    n = int(input())
    people = list(map(int, input().split()))
    avg = int(sum(people)//n)
    answer = 0
    for p in people:
        if p <= avg:
            answer += 1
    print(f"#{tc} {answer}")
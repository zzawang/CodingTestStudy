for tc in range(1, int(input()) + 1):
    text = input()
    answer = ""
    check = ['a', 'e', 'i', 'o', 'u']
    for t in text:
        if t not in check:
            answer += t

    print(f"#{tc} {answer}")
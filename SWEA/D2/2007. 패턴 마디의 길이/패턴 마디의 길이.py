T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    text = str(input())
    string = text[0]
    for i in range(1, len(text)):
        if text[i] == text[0] and string == text[i:i+len(string)]:
            print(f"#{t} {len(string)}")
        else:
            string += text[i]
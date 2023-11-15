def find_index(n, keypad):
    for i1 in range(len(keypad)):
        for i2 in range(len(keypad[0])):
            if keypad[i1][i2] == str(n):
                return (i1, i2)

def solution(numbers, hand):
    left_n = ["1", "4", "7"]
    right_n = ["3", "6", "9"]
    answer = ''
    hands = [(3, 0), (3, 2)]
    keypad = [["1", "2", "3"],
              ["4", "5", "6"],
              ["7", "8", "9"],
              ["*", "0", "#"]]
    
    for n in numbers:
        if str(n) in left_n:
            answer += "L"
            hands[0] = find_index(n, keypad)
        elif str(n) in right_n:
            answer += "R"
            hands[1] = find_index(n, keypad)
        else:
            x, y = find_index(n, keypad)
            le = abs(hands[0][0] - x) + abs(hands[0][1] - y)
            ri = abs(hands[1][0] - x) + abs(hands[1][1] - y)
            if le < ri:
                answer += "L"
                hands[0] = (x, y)
            elif le > ri:
                answer += "R"
                hands[1] = (x, y)
            else:
                if hand == "left":
                    answer += "L"
                    hands[0] = (x, y)
                else:
                    answer += "R"
                    hands[1] = (x, y)
        
    return answer
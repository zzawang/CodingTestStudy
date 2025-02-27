import sys
def to_decimal(number):
    length = len(number)
    num = 10 ** (length - 1)
    if number[-1] == 'K':
        return str(num * 5)
    return str(num)

num = list(n for n in sys.stdin.readline().rstrip())

start = num[-1]
max_str = []
for i in range(len(num) - 2, -1, -1):
    end = num[i]
    if start[-1] == 'K':
        if end == 'K':
            max_str.append(start)
            start = end
        else:
            start = end + start
    else:
        max_str.append(start)
        start = end
max_str.append(start)
max_str.reverse()


start = num[-1]
min_str = []
for i in range(len(num) - 2, -1, -1):
    end = num[i]
    if start[-1] == 'K':
        min_str.append(start)
        start = end
    else:
        if end == 'K':
            min_str.append(start)
            start = end
        else:
            start = end + start
min_str.append(start)
min_str.reverse()

max_num = ''
for number in max_str:
    max_num += to_decimal(number)

min_num = ''
for number in min_str:
    min_num += to_decimal(number)

print(max_num)
print(min_num)

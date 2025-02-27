import sys

expression_without_minus = sys.stdin.readline().rstrip().split('-')

tmp = []
for expression in expression_without_minus:
    tmp.append(sum(list(map(int, expression.split('+')))))

print(tmp[0] - sum(tmp[1:]))
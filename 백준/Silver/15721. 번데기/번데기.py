a = int(input())
t = int(input())
call = int(input())

people = []
find = 0
count = 1
answer = 0

while True:
    arr = []
    arr += [0, 1, 0, 1]
    arr += ([0] * (count + 1))
    arr += ([1] * (count + 1))
    for index, value in enumerate(arr):
        if value == call:
            find += 1
        if find == t:
            print((len(people) + index) % a)
            exit()

    people.extend(arr)
    count += 1
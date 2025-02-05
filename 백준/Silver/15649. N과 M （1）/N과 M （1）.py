n = 0
m = 0
arr = []

def solution():
    global n, m, arr
    n, m = map(int, input().split())
    arr = [num for num in range(1, n + 1)]
    for i, v in enumerate(arr):
        back_tracking(i, [v])


def back_tracking(index, num_arr):
    global n, m, arr
    if len(num_arr) == m:
        print(" ".join([str(a) for a in num_arr]))
        return

    for i in range(len(arr)):
        if arr[i] not in num_arr:
            num_arr.append(arr[i])
            back_tracking(i, num_arr)
            num_arr.remove(arr[i])

solution()
n = int(input())

total_count = n // 2 + 1
index = 1
sk = [0] * (total_count + 1)
cy = [0] * (total_count + 1)

while index <= total_count:
    sk[index] = sk[index - 1]
    cy[index] = cy[index - 1]
    if sk[index] + 1 + cy[index] == n:
        print("SK")
        break
    sk[index] += 1

    if sk[index] + cy[index] + 1 == n:
        print("CY")
        break
    cy[index] += 1

    index += 1

def main():
    n = int(input())

    for i in range(n//5, 0, -1):
        if (n - 5*i)%3 == 0:
            print(i+(n - 5*i)//3)
            return

    if n%3 == 0:
        print(n//3)
    else:
        print(-1)

main()
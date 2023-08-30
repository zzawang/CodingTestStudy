#include <stdio.h>

int main(int argc, const char * argv[]) {
    int n;
    scanf("%d",&n);

    int cnt = 0;
    if (n == 1)
    {
        cnt = 1;
    }
    else
    {
        int val = 2;
        while (n >= val)
        {
            val += 6 * cnt;
            cnt++;
        }
    }

    printf("%d",cnt);

    return 0;
}
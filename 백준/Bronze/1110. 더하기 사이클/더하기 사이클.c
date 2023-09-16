#include <stdio.h>
int main()
{
    int n,count=0;
    scanf("%d",&n);
    int compare=n;
    while(1)
    {
        n=(n/10+n%10)%10+n%10*10,count++;
        if(n==compare)
        {
            printf("%d",count);
            break;
        }
    }
    return 0;
}
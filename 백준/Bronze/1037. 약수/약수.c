#include <stdio.h>

int main(void)
{
    int n,max = 2,min = 1000000;
    int num[50];

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &num[i]);

    for (int i = 0; i < n; i++){
        if (num[i] > max)
            max = num[i];
        if(num[i] < min)
            min=num[i];
        else
            continue;
    }
    
    printf("%d", max*min);
    return 0;
}

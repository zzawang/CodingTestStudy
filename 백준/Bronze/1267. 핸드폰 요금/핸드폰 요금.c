#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int ntest,ymoney = 0,mmoney=0,y,m;
    scanf("%d", &ntest);

    int* time = (int*)malloc(sizeof(int) * ntest);

    for (int i = 0; i < ntest; i++) {
        scanf("%d", &time[i]);
    }

    for (int j = 0; j < ntest; j++) {
        if ((time[j] / 30)==0) {
            ymoney += 10;
        }
        else if ((time[j] / 30)>0) {
            y = (time[j] / 30);
            ymoney += y * 10;
            ymoney += 10;
            
        }
    }
    for (int k = 0; k < ntest; k++) {
        if ((time[k] / 60)==0) {
            mmoney += 15;
        }
        else if ((time[k] / 60)>0) {
            m = (time[k] / 60);
            mmoney += m * 15;
            mmoney += 15;
        }
    }
    if (ymoney > mmoney) {
        printf("M ");
        printf("%d", mmoney);
    }
    else if (ymoney < mmoney) {
        printf("Y ");
        printf("%d", ymoney);
    }
    else {
        printf("Y M ");
        printf("%d", mmoney);
    }
    return 0;
}
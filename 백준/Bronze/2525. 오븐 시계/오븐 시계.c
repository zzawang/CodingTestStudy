#include <stdio.h>

int main() {
    int si,bun,time;
    scanf("%d %d",&si,&bun);
    scanf("%d",&time);
    bun+=time;
    si+=(bun/60);
    bun=bun%60;
    si=si%24;
    printf("%d %d\n",si,bun);
    return 0;
}

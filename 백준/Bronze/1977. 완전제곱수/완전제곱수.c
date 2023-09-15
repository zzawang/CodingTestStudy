#include <stdio.h>

int main() {
    int m, n, sum = 0, min = 10000;
    scanf("%d %d", &m, &n);
    
    for(int i = 1; i*i<=n; i++){
       if(i*i>=m && i*i<=n){
        sum += i*i;
        if(i*i<min){min = i*i;}
       }
    }
    
    if(sum == 0){printf("-1");}
    else{printf("%d\n%d",sum, min);}
}

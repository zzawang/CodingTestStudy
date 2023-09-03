#include<stdio.h>

int main() {

    int c = 0, n = 0, i, j;
    scanf("%d", &c);

    for( i = 0; i < c; i++) {
        scanf("%d", &n);
        int score[1000], sum = 0;
        double avg = 0.00;
        for( j = 0; j < n; j++) {
            scanf("%d", &score[j]);
            sum += score[j];
        }
        avg = (double)sum / n;

        int count = 0;
        for ( j = 0; j < n; j++) {
            if (avg < score[j])
                count++;
        }
        printf("%.3f%%\n", (double)count * 100 / n);
    }
    return 0;
}
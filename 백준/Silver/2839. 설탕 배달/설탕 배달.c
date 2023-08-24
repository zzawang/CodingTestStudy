#include <stdio.h>

int main(void)
{
   int n;
   int a = 0, b = 0;

   scanf("%d", &n);

   for (a = 0; ; a++) {
      for (b = 0; ; b++) {
         if (3 * a + 5 * b == n) {
            printf("%d", a + b);
            return 0;
         }
         else if (3 * a + 5 * b > n) break;
         else continue;
      }
      if (a + b > 5000) break;
   }
   printf("-1");
   return 0;
}
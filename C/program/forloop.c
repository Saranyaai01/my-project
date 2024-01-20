#include <stdio.h>
int loop() 
{
   int i, j, rows;
   printf("\n Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = rows; i >= 1; --i) 
{
      for (j = 1; j <= i; ++j) 
{
         printf("* ", j);
      }
      printf("\n");
   }
   return 0;
}
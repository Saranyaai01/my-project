#include<stdio.h>
void print_table(int range, int num)
{
    int add;
    for (int i = 1; i <= range; i++)
   {
    add = num + i;
    printf("%d + %d = %d", num, i, add);
    printf("\n");
    }
}

   int addition1()
{
    int range = 10;
    int num = 10;
    print_table(range, num);
    return 0;
}

#include<stdio.h>
void print (int range, int num)
{
    int mul;
    for (int i = 1; i <= range; i++)
   {
    mul = num * i;
    printf("%d * %d = %d", num, i, mul);
    printf("\n");
    }
}

int table()
{
    int range = 10;
    int num = 6;
    print_table(range, num);
    return 0;
}

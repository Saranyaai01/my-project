#include<stdio.h>
int positive()
{
    int i;
    printf("\nEnter the i value: ");
    scanf("%d", &i);
    if(i>0)
    printf("\n %d is positive number",i);
    else if(i<0)
     printf("\n %d is negative number",i);
    else
    printf("\n %d is 0 ",i);
    return 0;
    
}
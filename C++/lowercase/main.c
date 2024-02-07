#include<stdio.h>
    int main()
    {
        char lwr[50];
        printf("Enter the upper case string:");
        gets(lwr);
        printf("\n The lower case string is: %s",strupr(lwr));
        return 0;
    }


#include <stdio.h>
int main() 
{
    char value;
    printf("Enter a character: ");
    scanf("%c", &value);

    if ((value >= 'a' && value <= 'z') || (value >= 'A' && value <= 'Z'))
        printf("%c is an alphabet.", value);
    else
        printf("%c is not an alphabet.", value);

    return 0;
}
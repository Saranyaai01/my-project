
#include <stdio.h>
int main()
{
    int i;
    char ch;
    float a, b,c,a1,b1,c1;
    printf("\n select how many numbers you need: ");
    scanf("%d",&i);
    if (i==2)
  
        {
        printf("\n Enter an operator (+, -, *, /) = \n" );
        scanf(" %c", &ch);
        printf("\n Enter  a  and b value : ");
        scanf("%f %f", &a, &b);

        switch (ch)
        {

        case '+':
            printf("\n the added  value is %f \n", a + b);
            break;
         case '-':
            printf("\n the subtracted value is %f\n", a - b);
            break;
         case '*':
            printf("\n the multiplied value is %f \n", a * b);
            break;
        case '/':
            printf(" \n the divided value is  %f \n", a / b);
            break;
        default:
            printf(" invalid operator \n");
        }
         printf("\n");
        }

        else
        {
  
        printf("\n Enter an operator (+, -, *, /) = \n" );
        scanf(" %c", &ch);
        printf("\n Enter  a1 value: " );
        scanf("%f", &a1) ;
        printf("\n Enter  b1 value: " );
        scanf("%f", &b1) ;
        printf("\n Enter  c1 value: " );
        scanf("%f", &c1) ;

        switch (ch)
        {

        case '+':
            printf("\n the added  value is %f \n", a1 + b1 + c1);
            break;
         case '-':
            printf("\n the subtracted value is %f\n", a1 - b1 - c1);
            break;
         case '*':
            printf("\n the multiplied value is %f \n", a1 * b1 * c1);
            break;
        case '/':
            printf(" \n the divided value is  %f\n", a1 / b1 / c1);
            break;
        default:
            printf(" invalid operator \n");
        }

        printf("\n");
        }
         return 0;
}

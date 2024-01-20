#include <stdio.h>
#include <stdlib.h>

int main()
{
   controlstatementif();
   controlstatementifelse();
   controlstatementnestedif();
   controlstatement4();
   controlstatementswitch();
   controlstatementfor();
   controlstatementwhile();
   controlstatementdowhile();
   return 0;
}
int controlstatementif()
{
    int i = 10;

    if (i > 15)
    {
        printf("\n\t 10 is greater than 15");
    }

    printf("\n\t I am Not in if");
}
int controlstatementifelse()
{
    int i = 20;

    if (i < 15)
        {
            printf("\n\t i is smaller than 15");
        }
    else
        {

        printf("\n\t i is greater than 15");
        }

}
int controlstatementnestedif()
{
    int i = 10;

    if (i == 10)
 {
    if (i < 15)
        printf("\n \t i is smaller than 15\n");

        if (i < 12)
            printf("\n\t i is smaller than 12 \n");
        else
            printf("\n\t i is greater than 15");
    }

}
int controlstatement4()
{
    int i = 20;

    if (i == 10)
        printf("\n\t i is 10");
    else if (i == 15)
        printf("\n\t i is 15");
    else if (i == 20)
        printf("\n\t i is 20");
    else
        printf("\n\t i is not present\n");

}
int controlstatementswitch()
{
     int var = 2;

    switch (var)
    {
    case 1:
        printf("\n\t Case 1 is executed");
        break;
    case 2:
        printf("\n\t Case 2 is executed");
        break;
    default:
        printf("\n\t Default Case is executed");
        break;
    }


}
int controlstatementfor()
{
  int i = 0;

  for (i = 1; i <= 10; i++)
  {
    printf( "\n\t Welcome All\n");
  }

}
int controlstatementwhile()
{
     int i = 2;
  while(i < 10)
  {
    printf( "\n\tHello World\n");
    i++;
  }

}
int controlstatementdowhile()
{
     int i = 2;

  do
  {
    printf( "\n\t How are you\n");

    i++;

  }
  while (i < 1);


}

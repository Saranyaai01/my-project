#include <stdio.h>
int main()
{

     addition( getB(),getA() );
     subtraction( getB(),getA() );
    ////multiplication(a,b);
    //division(a,b);
    //greater(a,b);
     return 0;
}
    int getA()
    {
     int a;
     printf("enter the value a:\n");
     scanf("%d",&a);
     return a;
    }
    int getB()
    {
        int b;
        printf("enter the value b:\n");
        scanf("%d",&b);
        return b;

    }
     int addition(int b,int a)
    {
      int c = a+b;
     printf("\n Added value is......%d\n",c);
    }
    int subtraction(int b,int a)
    {

    int c = a-b;
    printf("\n subtracted value is.......%d\n",c);
    }
    int multiplication(int l,int m)
    {

        int k = l*m;
        printf("\n multiplied value is.......%d\n",k);
    }
    int division(int r, int s)
    {
        float q = r/s;
        printf("\n divided value is..........%f\n",q);
    }
    int greater(int a,int b)
    {
        if(a>b)
           {
               printf("\n a is greater then b\n",a,b);
           }
           else
            {
                printf("\n a is less then b \n", a,b);

            }
    }
    int logic(int a,int b)
    {

            printf("a and b value is.....%d\n",!(a<10 || b<20));

    }






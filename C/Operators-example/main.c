#include <stdio.h>
int main()
{
int a=10;
int b=5;
int c;
     int subtractionprogram ( int a, int b);
     int multiplicationprogram( int a, int b);
     int divisionprogram( int a, int b);
     int modulasprogram( int a, int b);
     int incrementprogram( int a);
     int decrementprogram( int a);
    // int logicalprogram( int a, int b);

     return 0;
}

    int subtractionprogram(int a,int b)
    {

    int c = a-b;
    printf("\n subtracted value is.......%d\n",c);
    }
    int multiplicationprogram(int a,int b)
    {

        int c = a*b;
        printf("\n multiplied value is.......%d\n",c);
    }
    int divisionprogram(int a, int b)
    {
        float c= (float)a/b;
        printf("\n divided value is..........%f\n",c);
    }
    int modulasprogram(int a,int b)
    {
        int c = a%b;
        printf("\n modules value is......... %d\n",c);
    }
    int incrementprogram(int a)
    {
       while(a<20)
    {
        printf(" \n a value is.....%d\n",a);
        a++;
    }
    }
    int decrementprogram(int a)
    {
     while(a>5)
    {
        printf("\n a value is.....%d\n",a);
        a--;

    }

    }
    int logicalprogram(int a,int b)
    {
        if(!(a<10 && b<20)==1)
    {

        additionprogram(a,b);
    }
            printf("a and b value is .....%d\n",(a<10 && b<20));
            printf("a and b value is .....%d\n",(a<10 || b<20));

    }






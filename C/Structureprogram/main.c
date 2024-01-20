#include <stdio.h>
struct mysample
{
    int a,b,c;
    char e[10];
    char letter;
    long d;
    float f;
};
int main()
{
  struct mysample mystruct;
    mystruct.a=15;
    mystruct.b=10;
    mystruct.c=mystruct.a + mystruct.b;
    printf("\n added value is %d",mystruct.a);
struct mysample value;
    value.a = 50;
    value.b= 20;
    value.c= value.a - value.b;
    printf("\n \n subtracted value is %d\n",value.c);
struct mysample name;
    name.letter='A';
    printf("\n letter is %c\n",name.letter);
    struct mysample myname;
    strcpy(myname.e,"saranya");
    printf("\n my name is %s \n", myname.e);
struct mysample f1,f2,f3;
    f1.f=25;
    f2.f=2;
    f3.f=f1.f/f2.f;
    printf("\n divided value is %f\n",f3.f);
struct mysample s2 = {29,'A',"saranya"};
    s2.a=29;
    s2.letter='N';
    strcpy(s2.e,"saranya");
    printf("\n %d %c %s  \n" , s2.a , s2.letter , s2.e);

return 0;
 }

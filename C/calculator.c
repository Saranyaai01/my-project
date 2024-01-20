#include<stdio.h>
int main()
{
int i;
float a,b,c;
char ch;
printf("\n how many values you need to perform:");
scanf("%d",&i);
if(i==2)
{
	printf("\n enter the a value:");
	scanf("%f",&a);
	printf("\n enter the b value:");
	scanf("%f",&b);
	printf("\n Enter an operator (+, -, *, /)= \n" );
	scanf(" %c ", &ch);

switch( ch)
{

case '+':
printf("\n the added  value is %f  \n", a + b);
break;
case '-':
printf("\n the subtracted value is %f \n", a - b);
break;
case '*':
printf("\nthe multiplied value is  %f \n", a * b);
break;
case '/':
printf("\n the divided value is  %f \n",a / b);
break;
}
printf("\n");

}

else  
{

printf("\n enter the a1 value:");
scanf("%f",  & a);
printf("\n enter the b1 value:");
scanf("%f", & b);
printf("\n enter the c1 value:");
scanf("%f", & c);
printf("\n Enter an operator (+, -, *, /)= \n" );
scanf(" %c", &ch);

switch(ch)
{

case '+' :
printf("\n added value is %f \n" ,a+b+c);
break;
case '-' :
printf("\n subtracted value is %f \n",a-b-c);
break;
case '*':
printf("\n multiflied value is  %f \n ",a*b*c);
break;
case '/':
printf("\n divided value is %f \n",a/b/c);
break;
}
printf("\n");
}
return 0;
}



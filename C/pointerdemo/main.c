int main()
{
    char str[10] = "Hello" ;
    printf(" %p \n", &str);
    printf("%s \n", str);

printf("-----------\n");
 char *p="Hello" ;
    printf("value of p                          : %p \t\n", p);
    printf("address of p                        : %p \t\n", *p);
    printf("value stored in the address of p    : %s \t\n", p);
    printf("-----------\n");

char **q=&p;
    printf("value of q                          : %p \t\n", q);
    printf("address of q                        : %p \t\n", *q);
    printf("value stored in the address of q    : %s \t\n", *q);
    printf("-----------\n");

char ***r=&q;
    printf("value of r                         : %p \t\n", r);
    printf("address of r                        : %p \t\n", *r);
    printf("value stored in the address of r    : %s \t\n", **r);
    printf("-----------\n");


    return 0;
}





































/*#include<stdio.h>
int main()
{
    int x=20;
    int *ptr;
    ptr = &x;
    printf("\n Value of ptr :%d",ptr);
    printf("\n Value of x:%d",x);
    printf("\n address of x:%p",&x);
    printf("\n address of *ptr : %p",&*ptr);
    printf("\n address of ptr:%p",&ptr);
    return 0;
}*/























/*#include<stdio.h>
int main()
{
    char string[10];
    printf("Enter the String: ");
    gets(string);
    printf("\n%s",string);
    return 0;
}*/























/*#include <stdio.h>
void swap(int *n1, int *n2);

int main()
{
    int num1 = 15, num2 = 10;


    swap( &num1, &num2);

    printf("num1 = %d\n", num1);
    printf("num2 = %d", num2);
    return 0;
}

void swap(int* n1, int* n2)
{
    int temp;
    temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}*/
































/*#include <stdio.h>
struct str
{
};
void func(int a, int b)
{
};

int main()
{

	int a = 10;
	char c = 'G';
	struct str x;


	int* ptr_int = &a;
	char* ptr_char = &c;
	struct str* ptr_str = &x;
	void (*ptr_func)(int, int) = &func;
	void* ptr_vn = NULL;


	printf("Size of Integer Pointer \t:\t%d bytes\n",sizeof(ptr_int));
	printf("Size of Character Pointer\t:\t%d bytes\n",sizeof(ptr_char));
	printf("Size of Structure Pointer\t:\t%d bytes\n",sizeof(ptr_str));
	printf("Size of Function Pointer\t:\t%d bytes\n",sizeof(ptr_func));
	printf("Size of NULL Void Pointer\t:\t%d bytes",sizeof(ptr_vn));

	return 0;
}*/






































/*#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=10, b=20;
    printf("value of a      : %d \t\n", a);
    printf("Address of a    : %d \n", &a);
    printf("***************************************************************\n");
    printf("value of b      : %d \t\n", b);
    printf("address of B    : %d \n", &b);
    printf("**************************************************************\n");

    int *p=&a;
    printf("value of p          : %d \t\n", p);
    printf("address of p        : %d \t\n", &p);
    printf("value stored in the address of p: %d \t\n", *p);
    printf("****************************************************************\n");

    int **q=&p;
    printf("value of q         : %d \t\n", q);
    printf("address of q       : %d \t\n", &q);
    printf("value stored in the address of q to the address of p: %d \t\n", **q);

    printf("*****************************************************************\n");

    int ***r=&q;
    printf("value of r          : %d \t\n", r);
    printf("address of r         : %d \t\n", &r);
    printf("value stored in the address of r to the address of q in the address of p: %d \t\n", ***r);
    printf("***************************************************************\n");

    void *s=&a;
    printf("value of s           : %d \t\n", s);
    printf("address of s         : %d \t\n", &s);
    printf("value stored  in the address of s in the address of r to the address of q in the address of p    : %d \t\n", *(int*)s);
    printf("***************************************************************\n");

    return 0;
}*/

#include <iostream>
using namespace std;
int main()
{
int number=30;
int *p ;
p= &number;

cout << "Address of number variable is:" << &number << endl;
cout << "Address of p variable is:" << &p << endl;
cout << "Value of p variable is:" << *p <<endl;
*p=15;
cout << "value of p:" << *p;
   return 0;
}























/*#include <iostream>
#include <string>
using namespace std;

int main()
{
    string food = "Pizza";

    string* ptr = &food;

    cout << food << "\n";
    cout << &food << "\n";


    cout << *ptr << "\n";
    *ptr = "burger";
    cout << *ptr <<  "\n";
    cout << food <<endl;
    return 0;
}*/















































/*#include <iostream>
using namespace std;
void demo()
{
    int x = 20;

    int *ptr;

    ptr = &x;


    cout << "Value at ptr = " << ptr << "\n";
    cout << "Value at x = " << x << "\n";
    cout << "Value at *ptr = " << *ptr << "\n";
}

int main()
{
  demo();
  return 0;
}*/


























/*#include <iostream>
using namespace std;

int main()
{
    // declare variables
    int var1 = 3;
    int var2 = 24;
    int var3 = 17;

    // print address of var1
    cout << "Address of var1: "<< &var1 << endl;

    // print address of var2
    cout << "Address of var2: " << &var2 << endl;

    // print address of var3
    cout << "Address of var3: " << &var3 << endl;
}*/

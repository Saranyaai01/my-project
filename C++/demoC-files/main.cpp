#include <iostream>
using namespace std;
class myfirstclass
{
public :
    int a=10;


};
int addition()
{
    int a,b,a1;
    cout << "Enter the a and b values:" ;
    cin >> a >> b;
    a1=a+b;
    cout <<a1;
}
int multiply()
    {
    int x,y;
    cout << "Enter the x and y value:";
    cin >> x >> y;
    cout <<(x*y);
     }

int main()
{

     addition();
     multiply();
     myfirstclass mfc,mfc1;
     cout << mfc.a;
     return 0;
}




#include <iostream>
using namespace std;
class myfirstclass
{
public :
    int a=10;
    void multiply();
int addition()
{
    int a,b,a1;
    cout << "Enter the a and b values:" ;
    cin >> a >> b;
    a1=a+b;
    cout <<a1;
}

    int subtraction()
    {
        int first_value,second_value,total;


    }


};void myfirstclass :: multiply()
    {
    int x,y;
    cout << "Enter the x and y value:";
    cin >> x >> y;
    cout <<(x*y);
     }


int main()
{

     myfirstclass mfc,mfc1;
     cout << mfc.a;
     mfc.addition();
     mfc1.multiply();
     return 0;
}




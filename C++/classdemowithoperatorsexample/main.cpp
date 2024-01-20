#include <iostream>
using namespace std;
class myfirstclass
{

public :
     void division();
     void modulas();

    int a=10;

int addition()
{
    int a,b,a1;
    cout << "\n" << "Enter the a and b values:" ;
    cin  >> a >> b;
    a1=a+b;
    cout << "\n" <<a1;
}
int subtraction()
{
    int first_value,second_value,total;
    cout << "\n" << "Enter the first_value:" ;
    cin >> first_value;
    cout << "\n" << "Enter the second_value:";
    cin >> second_value;
    total = first_value-second_value;
    cout << "\n" << total;

}
int multiplication()
{
    int x,y;
    cout << "\n" << "Enter the x and y value:";
    cin >> x >> y;
    cout << "\n" <<(x*y);
}


};void myfirstclass :: division()
    {
        int dividend_value,divisor_value;
        float quotient;
        cout <<"\n" << "Enter the dividend_value:";
        cin >> dividend_value;
        cout << "\n" <<"Enter the divisor_value:";
        cin >> divisor_value;
        quotient=dividend_value/divisor_value;
        cout << "\n" << quotient;

    }
    void myfirstclass :: modulas()
    {
        int value1,value2,remainder;
        cout << "\n" << "Enter the value1 and value2:";
        cin >> value1 >> value2;
        remainder=value1%value2;
        cout << "\n" << remainder;
    }
    int exponent()
    {
        int expo;
        float base,result =1;
        cout << "\n" << "Enter base and expo:";
        cin >> base >> expo;
        cout << base << "^" << expo;
        while (expo!=0)
        {

            result *=base;
            --expo;
        }
        cout << "\n" <<result;
    }
    int increement()
    {
        int p;
        cout << "Enter the p value:";
        cin >> p;
        for(p;p<10;p++)
        {
            cout << "\n"<<"the increment value is:"<<p;
        }
    }
    int decrement()
    {
        int q;
        cout <<"\n" << "Enter the q value:";
        cin >> q;
        for(q;q>5;q--)
        {
            cout << "\n" <<"the decrement value is:"<<q;
        }
    }



int main()
{
    decrement();
    increement();
     exponent();
     myfirstclass mfc,mfc1,mfc2;
     mfc.addition();
     mfc.subtraction();
     mfc.multiplication();
     mfc.division();
     mfc.modulas();
     return 0;
}




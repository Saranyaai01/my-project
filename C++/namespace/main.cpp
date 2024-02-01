#include<iostream>
using namespace std;

int main()
{
    string firstname;
    cout <<"Enter firstname:" <<endl;
    cin >> firstname;
    string lastname;
    cout <<"Enter the lastname:" <<endl;
    cin >> lastname;
    cout << firstname +" "+lastname<<endl;
    string fullname = firstname. append(lastname);
    cout << fullname <<endl;
    firstname.push_back('N');
    cout << firstname <<endl;
    lastname.push_back('N');
    cout << lastname <<endl;
    cout << fullname.length()<<endl;
    cout << fullname.size()<<endl;


    /*string name;
    cout <<"Enter your name:"<<endl;
    getline(cin,name);
    cout << name;
    //fflush(stdin);
    cout << "Enter your name:"  <<endl;
    getline(cin, name);
    cout << name;
    cout << "Enter your name:"  <<endl;
    getline(cin, name);
    cout << name;*/
    return 0;

}















/*#include <iostream>

using namespace std;//namespace example

namespace number1
{
    int x=2;
   void sample()
   {
     cout << "this is sample number1:"  <<endl;

    }

}
namespace number2
{
 int x=5;
 void sample()
 {
     cout <<"this is sample number2:"<<endl;
 }


}

int main()
{

    cout << number1::x << endl;
    number1::sample();
    cout << number2::x <<endl;
    number2::sample();
    return 0;
}*/

#include<iostream>
using namespace std;
class sample
{
public:
    sample()
{

    int a,a1,a2,a3,a4,a5,a6;
    int b,b1,b2,b3,b4,b5,b6;
    cout << "welcome to the arithmetic operator example!" << endl;
    cout << "Enter the two values:\t";
    cin  >>a >> b;
    cout << a+b <<endl;
    cout <<"Enter the two values:\t";
    cin >> a1 >>b1;
    cout << a1-b1 << endl;
    cout << "Enter the two values:\t";
    cin  >> a2 >>b2;
    cout << a2*b2 << endl;
    cout <<"Enter the two values:\t";
    cin  >>a3 >>b3;
    cout  << a3/b3 << endl;
    cout <<  "Enter the two values:\t";
    cin  >>a4 >>b4;
    cout  << a4%b4 << endl;
    cout <<  "Enter the  value:\t";
    cin >>a5;
    cout << ++a5<< endl;
    cout << "Enter the value:\t";
    cin   >>a6;
    cout<< --a6 << endl;
    cout << "Enter the value:\t";
    cin   >>b5 ;
    cout << b5++ << endl;
    cout << "Enter the value:\t";
    cin   >> b6 ;
    cout << b6-- << endl;
}
};
class example
{
public:
    example()
{
   int p=10;
    cout << "\n the value is:" <<p;
    }
    void print(int i)
    {
        cout << "\n here is int:" <<i;
    }
    void print(double q)
    {
    cout << "\n here is float:" << q;
    }
    void print(string name)
    {
    cout << "\n here is  name:" << name;
    }

};
class student
{
     int rollnumber;
     char name[50];
     double fees;
public:
    student()
    {

        cout <<"\n Enter the rollnumber:";
        cin >> rollnumber;
        cout <<"\n Enter the name:";
        cin >> name;
        cout <<"\n Enter the fees:" ;
        cin >> fees;
    }

    void disply()
    {

         cout << "\n \t"<<rollnumber<<"\t" <<name<<"\t" << fees <<endl;
    }


};


 int main()
 {
    //sample s;
    example e;
    student S;
    e. print(152);
    e. print(251.36);
    e. print("Saranya");
    S.disply();
    return 0;
  }










































/*#include<iostream>
using namespace std;
class myclass{
public:
    myclass(){
    cout << "Welcome to the constructor and function over loading demo class...." <<endl;
    }
    myclass(string name){

    cout << "Hai!" << name << "\t" << "Welcome to the constructor and function over loading demo class...." <<endl;
    }


};
int main()
{
    myclass mc;
    string name;
    cout << "Enter your name:";
    cin >> name;
    myclass mc1(name);
    return 0;
}*/























/*#include<iostream>
using namespace std;
class A{
public:
    A(){
    int arr[5]={1,2,3,4,5};
    for (int i=0;i<5;i++)
    {
        cout <<arr[i] <<endl;
    }
    }
};
int main()
{
    A a;
    return 0;
}*/
























/*#include<iostream>
using namespace std;
class A{
public:
    int i;
    A(int age){

    }
    A(string name){

    }
    A(string name,int age)
    {

    }
};
int main()
{
    A a(int age);
    int age;
    cout <<"Enter the age:";
    cin >> age;
    A a1(string name);
    string name;
        cout <<"Enter the name:";
    cin >> name;
    A a2(string name,int age);
    cout << name << "\t" << age << endl;
    return 0;
}*/



















/*#include<iostream>
using namespace std;
class constructor{
public:
    int a,b;

    constructor(){
    a=10;
    b=20;

    }
};
int main()
{
    constructor c;
    cout << "a:" << c.a << "b:" << c.b;
    return 0;
}*/






















/*#include<iostream>
using namespace std;
class student
{
     int rollnumber;
     char name[50];
     double fees;
public:
    student()
    {
        cout <<"\n Enter the rollnumber:";
        cin >> rollnumber;
        cout <<"\n Enter the name:";
        cin >> name;
        cout <<"\n Enter the fees:";
        cin >> fees;
    }
    void disply()
    {
        cout <<rollnumber<<"\t" <<name<<"\t" << fees;
    }

};
int main()
{
    student s;
    s.disply();
    return 0;
}*/
















/*#include <iostream>
using namespace std;
class demo{
public:
    int a;
    demo()
    {
        a=10;
        cout << "\n the value is:" <<a;
    }
    void print(int i){
        cout << "\n here is int:" <<i;
    }
    void print(double q){
    cout << "\n here is float:" << q;
    }
    void print(char const *c){
    cout << "\n here is char*" << c;
    }

};

int main()
{
    demo demo1;
    demo1.print(10);
    demo1.print(20.52);
    demo1.print("welcome");
    cout << "\n Hello world!" ;
    return 0;
}*/

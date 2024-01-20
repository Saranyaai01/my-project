#include<iostream>
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
}























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

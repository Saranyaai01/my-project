






























/*#include <iostream>
using namespace std;//hybride inhritance

class Meal
{
public:
    void print()
    {
        cout << "Different types of meals are served :"<< endl;

    }
};

class Breakfast : public Meal
{
public:
    void print()
    {
        cout << "\nBreakfast is a type of meal." << endl;
    }
};


class Milk : public Breakfast
{
public:
    void print()
    {
        cout << "Milk served in breakfast." << endl;
    }
};

class Yoghurt : public Milk
{
public:
    void print()
    {
        cout << "Yoghurt made from milk." << endl;
    }
};


class Dessert : public Meal
 {
public:
    void print()
    {
        cout << "\nDessert is a type of meal." << endl;
    }
};


class Sweets : public Dessert
{
public:
    void print()
    {
        cout << "Sweets served in Dessert." << endl;
    }
};


class Pastry : public Sweets
 {
public:
    void print()
    {
        cout << "Pastry is a type of sweet." << endl;
    }
};

int main()
{
    Meal types;
    Breakfast servedBreakfast;
    Milk milk;
    Yoghurt yoghurt;
    Dessert servedDessert;
    Sweets sweet;
    Pastry pastry;

    types.print();
    servedBreakfast.print();
    milk.print();
    yoghurt.print();
    servedDessert.print();
    sweet.print();
    pastry.print();

    return 0;
}*/






































/*#include<iostream>
using namespace std; //multilevel inheritance
class A{
public:
    int a;
    void getAdata(){
    cout <<"Enter the value of a:"<< endl;

    }
};
class B: public A{
public:
    int b;
    void getBdata(){
    cout <<"Enter the value of b:" << endl;

    }

};
class C: public B{

public:
    int c;
void getCdata(){

 cout <<"Enter the value of c:" << endl;

}
void sum(){

int ans = a + b + c;
cout << "sum is:" <<ans;
}
};
int main()
{
    C obj;
    obj.getAdata();
    cin >> obj.a;
    obj.getBdata();
    cin >> obj.b;
    obj.getCdata();
    cin >> obj.c;
    obj.sum();
    return 0;


}*/







































//  hierarchical inheritance

/*#include <iostream>
using namespace std;

class Animal
{
   public:
    void info()
    {
        cout << "I am an animal." << endl;
    }
};


class Dog : public Animal
{
   public:
    void bark()
    {
        cout << "I am a Dog. Woof woof." << endl;
    }
};


class Cat : public Animal
 {
   public:
    void meow()
     {
        cout << "I am a Cat. Meow." << endl;
    }
};

int main() {

    Dog dog1;
    cout << "Dog Class:" << endl;
    dog1.info();
    dog1.bark();


    Cat cat1;
    cout << "\nCat Class:" << endl;
    cat1.info();
    cat1.meow();

    return 0;
}*/




























/*#include <iostream>
using namespace std;

class Mammal //mutiple inheritance
{
  public:
    Mammal()
    {
      cout << "Mammals can give direct birth." << endl;
    }
};

class Animal {
  public:
    Animal()
    {
      cout << "Winged animal can flap." << endl;
    }
};

class Bat: public Mammal, public Animal
{


};

int main()
{
    Bat b1;
    return 0;
}*/






































#include<iostream>
using namespace std;
class person{
private:

    int Id;
    string Name;



public:
    void set_details()
    {
        cout << "Enter the Id:" <<endl;
        cin >> Id;
        cout << "Enter the Name:" <<endl;
        cin >>Name;
    }
    string display_name()
    {
        return Name;
    }
    int display_id()
    {
    return Id;

    }

};
 class student : public person
 {

char course[50];
int fee;
public:
    void set_s()
    {

        cout << "Enter the course Name:";
        cin >> course;
        cout <<"Enter the course fees:";
        cin >> fee;


    }
    string display_course()
    {

       return course;
     }
     int display_fees()
     {
         return fee;
     }


};
int main()
{
    student s;
    s.set_details();
    s.set_s();
    cout << "\n" << s.display_id()<< endl;
    cout << "\n" <<s.display_name()<< endl;
    cout <<"\n" <<s.display_course() <<endl;
    cout <<"\n" <<s.display_fees() <<endl;
    return 0;
}








































/*#include <iostream>
#include <stdio.h>

using namespace std;

class Information
{
  private:
    int roll;
    char name[30];

  public:
    void inputinfo()
    {
        cout <<"Enter Roll: ";
        cin >>roll;
        cout <<"Enter Name: ";
        cin >> name;
    }

    void displayinfo()
    {
        cout<<"Roll: "<<roll<<endl;
        cout<<"Name: "<<name<<endl;
    }
};


class Result : public Information
{
  private:
    int eng;
    int math;
    int comp;
    int total;
    float per;

  public:
    void inputdata()
    {
        inputinfo();
        cout<<"Enter English: ";
        cin>>eng;
        cout<<"Enter Math: ";
        cin>>math;
        cout<<"Enter Computer: ";
        cin>>comp;
        total=eng+math+comp;
        per=(total/300.0)*100;
    }

        void displaydata()
    {
        displayinfo();
        cout<<"English: "<<eng<<endl;
        cout<<"Math: "<<math<<endl;
        cout<<"Computer: "<<comp<<endl;
        cout<<"Total: "<<total<<endl;
        cout<<"Percentage: "<<per<<endl;
    }
};

int main()
{
    Result x;
    x.inputdata();
    x.displaydata();
    return 0;
}*/

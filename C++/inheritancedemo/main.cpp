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

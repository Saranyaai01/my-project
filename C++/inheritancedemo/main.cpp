#include <iostream>
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
        cout<<"Enter Roll: ";
        cin>>roll;
        fflush(stdin);	// clear the input buffer
        cout<<"Enter Name: ";
        gets(name);
    }

    void displayinfo()
    {
        cout<<"Roll: "<<roll<<endl;
        cout<<"Name: "<<name<<endl;
    }
};

// Inherit the class Information into Result
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
        inputinfo();	// calling the inputinfo() method of the parent class Information
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
        displayinfo();	// calling the displayinfo() method of the parent class Information
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
}

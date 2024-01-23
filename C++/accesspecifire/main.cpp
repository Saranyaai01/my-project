#include <iostream>

using namespace std;

class student
{
  protected:
    int eng;
    int math;
};

class result : public student
{
  private:
    int total;
    float per;

  public:
    void input()
    {
        cout<<"Enter English: ";
        cin>>eng;
        cout<<"Enter Math: ";
        cin>>math;
    }


    void calculate()
    {
        total=eng+math;
        per=(total/200.0)*100;
    }

    void show()
    {
        cout<<"English: "<<eng<<endl;
        cout<<"Math: "<<math<<endl;
        cout<<"Total Marks: "<<total<<endl;
        cout<<"Percentage: "<<per<<endl;
    }
};


int main()
{
    result x;
    x.input();
    x.calculate();
    x.show();

    return 0;
}





























/*#include <iostream>

using namespace std;

class student
{
   private:
     int eng;
     int math;
     int total;
     float percentage;
public:

    void setmark()
    {
        int m1, m2;
        eng = m1;
        math = m2;
        cout << "Enter English: " ;
        cin >> eng;
        cout << "Enter Math: " ;
        cin >> math;

        }

    void calculate()
    {
        int t1 ,p1;
        total = t1;
        percentage = p1;
        total=eng+math;
        percentage=(total/200.0)*100;

    }

    void show()
    {
        cout << "English: " << eng << endl;
        cout << "Math: " <<math <<endl;
        cout << "Total Marks: " << total<< endl;
        cout << "Percentage: " << percentage<< endl;
    }
};


int main()
{
    student s;
    s.setmark();
    s.calculate();
    s.show();

    return 0;


}*/













/*#include <iostream>
using namespace std;

class BankAccount
 {
private:
double balance;

public:

BankAccount(double initialBalance)
{
 balance = initialBalance;
}
void CheckBalance()
{
cout << "Your balance is $" << balance << endl;
}

void Deposit(double amount)
{
if (amount > 0)
    {
    balance += amount;
    cout << "Deposited $" << amount << " into your account." << endl;
    }
}
};

int main() {

BankAccount myAccount(1000.0);
myAccount.CheckBalance();
myAccount.Deposit(500.0);
myAccount.CheckBalance();

return 0;
}*/

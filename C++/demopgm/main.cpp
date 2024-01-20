#include <iostream>

using namespace std;

int main()
{
   int value1,value2,op,sum,sub,mul,mod,increment,decrement;
   float div;
   cout<<"\n enter the value 1 and value 2:\n";
   cin>>value1>>value2;
   cout<<"\n Enter the operator(1,2,3,4,5,6,7)\n";
   cin>>op;
   switch(op)
   {

   case 1:
          sum= value1+value2;
        cout<<"added value is:" <<sum;
        break;
   case 2:
        sub=value1-value2;
       cout<<"subtracted value is:"<<sub;
       break;
   case 3:
         mul=value1*value2;
        cout<<"multiplied value is:"<<mul;
        break;
   case 4:
         div=value1/value2;
        cout<<"divided value is:"<<div;
        break;
   case 5:
       mod=value1%value2;
       cout<<"modulas  value is:"<<mod;
       break;
   case 6:
        increment=value1++;
        cout<<"incremented value is:\n"<<increment<<value1;
        break;
   case 7:
    decrement=value1--;
    cout<<"decremented value is:\n"<<decrement<<value1;
    break;

}
   return 0;
   }


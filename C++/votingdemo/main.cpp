#include<iostream>
using namespace std;

class votingCheck{
public:

int addition(int a, int b){
int c;
c=a+b;
cout << c;
}

float addition(float a, float b, float f){
float c;
c=a+b+f;
cout << c;
}
};




int main(){
int v1, v2;
votingCheck vc;
cin >> v1 >> v2;
vc.addition(v1,v2);
float v3,v4,v5;
cin >> v3 >> v4 >> v5;
vc.addition(v3,v4,v5);



return 0;
}


/*#include <iostream>

using namespace std;

int main()
{
    string s;
    cout << "Enter the lowercase string:";
    cin >> s;
    for(auto&x:s)
    {
        cout <<(char)toupper(x);
    }
    return 0;
}*/


#include <iostream>

using namespace std;

int main()
{
    string s;
    cout << "Enter the uppercase string:";
    cin >> s;
    for(auto&x:s)
    {
        cout <<(char)tolower(x);
    }
    return 0;
}

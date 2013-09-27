#include <iostream>
#include <string>

using namespace std;
int main()
{
    string s("Expressions in C++ are composed...");
    string ::iterator it = s.begin();
    while (it != s.end() && !isspace(*it)){
        *it = toupper(*it);
        cout << *it << endl;
        ++it;
    }




    return 0;
}

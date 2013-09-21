#include <iostream>
#include <string>

using namespace std;
int main()
{
    string line ;
    while (getline(cin,line))
        cout << line << line.size() << line.empty() << endl;
    return 0;
}

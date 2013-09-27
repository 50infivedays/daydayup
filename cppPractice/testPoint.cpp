#include <iostream>
#include <string>

using namespace std;

int main()
{
    int a = 10;
    int *p2 = &a;

    cout << a << " " << p2 << ' ' << *p2 << ' ' << &a << endl;

    return 0;
}

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> ivec;
    int cnt = 10;
    while (cnt > 0)
        ivec.push_back(cnt--);

    vector<int>::iterator iter = ivec.begin();

    while(iter!= ivec.end())
        cout << *iter++ << endl;













    return 0;

}

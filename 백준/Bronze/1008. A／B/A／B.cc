#include <iostream>
using namespace std;
int main() {
    int A, B;
    cin >> A >> B;
    cout.precision(12);
    cout << fixed << (double)A / B;
    return 0;
}

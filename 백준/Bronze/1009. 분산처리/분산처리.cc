#include <iostream>
using namespace std;
int main() {
    int T;
    cin >> T;
    while (T--) {
        int a, b, res = 1;
        cin >> a >> b;
        for (int i = 0; i < b; i++) res = (res * a) % 10;
        if (res == 0) res = 10;
        cout << res << '\n';
    }
    return 0;
}

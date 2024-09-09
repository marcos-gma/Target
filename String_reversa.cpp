#include <iostream>

using namespace std;

int main(){
    string palavra;
    cout << "Digite uma palavra: ";
    cin >> palavra;

    for(int i = palavra.size() - 1; i >= 0; i--){
        cout << palavra[i];
    }

    return 0;
}
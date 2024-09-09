#include <iostream>
using namespace std;

bool in_fibonacci(int num){
    int a = 0, b = 1, c = 0;
    while(c < num){
        c = a + b;
        a = b;
        b = c;
    }
    if(c == num){
        return true;
    }
    return false;
}

int main (){
    int num; 
    cout << "Digite um número: ";
    cin >> num;

    if(in_fibonacci(num)){
        cout << "O número pertence a sequência";
    }else {
        cout << "O número NÂO pertence a sequência";
    }

    return 0;
}
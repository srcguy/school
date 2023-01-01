#include <iostream> //basic library for input and output

using namespace std;

int n; //defines some variables//'int' means 'integer', in Polish 'liczba całkowita'

int add(int a) //defines function 'add' with parameter 'a'
{
    return a + a; //return 'a + a'//in this case, 'n + n'
}
int main()
{
    cout << "Enter one number\n"; //shows text in firts row
    cin >> n; //requests an integer from user. that number will be stored as 'n'
    cout << add(n); //shows function 'add' that takes 'n' as a parameter 'a', so 'a' in function equals 'n'
    return 0; //gives us '0' as a result
}

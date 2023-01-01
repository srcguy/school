#include <iostream> //basic library for input and output

using namespace std;

int a ,b; //defines some variables//'int' means 'integer', in Polish 'liczba całkowita'

int main()
{
    cout << "Hi! My name is Computek!\nPlease write some numbers!\n"; //shows text in firts and second row
    cin >> a; //requests an integer from user. that number will be stored as 'a'
    cin >> b; //requests an integer from user. that number will be stored as 'b'
    //WARNING! we could use just 'cin >> a >> b;'
    if (b != 0)
    {
        cout << a << "/" << b << "=" << a / b; //shows text and variables and some calculations//we need to use '<<' to separate text from variables
    }
    else
    {
        cout << "We couldn't divide by zero!\nI set 'b' to '1'!\n"; //shows text in firts and second row
        b = 1; //defines variable
        cout << a << "/" << b << "=" << a / b; //shows text and variables and some calculations//we need to use '<<' to separate text from variables
    }
    return 0; //gives us '0' as a result
}

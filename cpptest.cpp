
#include <iostream>
using namespace std;

void say_hello() {
	cout << "Hello!" << endl;
}

void reduction_by_halves(int n){
	while (n > 0) {
		cout << n << endl;
		n = n / 2;
	}
}
int main()
{
	int n = 100;
	say_hello();
	reduction_by_halves(n);
	return 0;
}

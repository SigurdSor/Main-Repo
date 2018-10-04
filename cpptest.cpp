
#include <iostream>
#include <cmath>
#include <vector>
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

double stirling(int x){
    return x*log(x)-x;
}

int triangle(int n) {
    int triangle_sum = 0;
    int i = 0;
    while (i < n+1) {
        triangle_sum += i;
        i += 1;
    }
    return triangle_sum;
}


vector<double> linspace(double a, double b, int n) {
    vetctor
}


int main()
{
	int n = 1000;
    vector<int> testvector{2, 5, 10, 50, 100, 1000};
	say_hello();
	reduction_by_halves(n);
    for (int i=0; i<6; i++) {
        double stir = stirling(testvector[i]);
        double real = lgamma(testvector[i]+1);
        cout << stir-real << endl;
    }
    cout << triangle(n) << endl;
	return 0;
}

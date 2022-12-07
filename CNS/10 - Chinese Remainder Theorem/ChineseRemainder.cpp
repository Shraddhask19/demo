#include<bits/stdc++.h>

using namespace std;

// returns x where (a * x) % b == 1
int mul_inv(int a, int b)
{
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

int chinese_remainder(int *n, int *a, int len)
{
	int p, i, prod = 1, sum = 0;

	for (i = 0; i < len; i++)
		prod *= n[i];
		
	cout<<"The Product of Divisors is: "<<prod<<endl;
		
	for (i = 0; i < len; i++) {
		p = prod / n[i];
		sum += a[i] * mul_inv(p, n[i]) * p;
	}

	return sum % prod;
}

int main(void)
{
	int n[] = { 3, 5, 7 };
	int r[] = { 2, 3, 2 };
	
	cout<<"The Divisors are: ";
	
	for(int i = 0;i < 3;i++)
		cout<<n[i]<<" ";
	
	cout<<"and their respective remainder are: ";
	
	for(int i = 0;i < 3;i++)
		cout<<r[i]<<" ";
		
	cout<<endl;
	
	int ans = chinese_remainder(n, r, sizeof(n)/sizeof(n[0]));
	
	cout<<"Output: "<<ans<<endl;
	return 0;
}

#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	int fin, start, mid, end = 0;
	scanf("%d", &n);
	int budg[10001];
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &budg[i]);
		if (budg[i] > end)
			end = budg[i];
	}
	int m;
	scanf("%d", &m);
	while (start <= end)
	{
		fin = 0;
		mid = (end + start) / 2;
		for (int i = 0; i < n; i++)
		{
			if (budg[i] > mid)
			fin += mid;
			else
			fin += budg[i];
		}
		if (fin <= m)
			start = mid + 1;
		else
			end = mid - 1;
	}
	printf("%d", end);
	return 0;
}

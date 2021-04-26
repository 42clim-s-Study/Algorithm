#include <cstdio>
#include <queue>
using namespace std;

int main()
{
	int n,k;
	scanf("%d%d", &n, &k);
	queue <int> que;

	int i = 0;
	for (int i = 1; i <= n; i++)
	{
		que.push(i);
	}
	printf("<");
	while (!que.empty())
	{
		for (int i = 0; i < k - 1; i++)
		{
			int a = que.front();
			que.push(a);
			que.pop();
		}
		if (que.size() == 1)
			printf("%d", que.front());
		else
			printf("%d, ", que.front());
		que.pop();
	}
	printf(">");
	return 0;
}

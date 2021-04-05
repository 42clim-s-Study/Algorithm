#include <stack>
#include <cstdio>

using namespace std;

int main()
{
	stack<int> stack;
	int n;
	scanf("%d", &n);
	int arr[n + 1] = {0,};
	char count[n + 1];
	for (int i = 1; i < n + 1; i++)
		scanf("%d", &arr[i]);
	int j = 1;
	int m = 0;
	int z = 0;
	for (int i = 1; i < n + 1; i++)
	{
		if (stack.empty() && j < n + 1)
		{
			stack.push(j);
			count[m++] = '+';
			j++;
		}
		while (arr[i] != stack.top() && j < n + 1 && j > stack.top())
		{
			stack.push(j);
			count[m++] = '+';
			j++;
		}
		if (arr[i] == stack.top())
		{
			stack.pop();
			count[m++] = '-';
		}
		else
		{
			printf("NO");
			return 0;
		}
	}
	count[m] = '\0';
	for (int i = 0; i < m; i++)
		printf("%c\n", count[i]);
	
	return 0;
}

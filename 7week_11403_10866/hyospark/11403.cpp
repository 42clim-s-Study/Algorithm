#include <cstdio>

using namespace std;

int main()
{
	int arr[100][100];
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			scanf("%d", &arr[i][j]);
	}
	for (int mid = 0; mid < n; mid++)
		for (int start = 0; start < n; start++)
			for (int end = 0; end < n; end++)
				if (arr[start][mid] && arr[mid][end])
					arr[start][end] = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			printf("%d ", arr[i][j]);
		printf("\n");
	}
	return 0;
}

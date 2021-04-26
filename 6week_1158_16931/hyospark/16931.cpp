#include <cstdio>

int main()
{
	int n, m;
	scanf("%d%d", &n, &m);
	int arr[101][101] = {0,};
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%d", &arr[i][j]);
	}
	int result, verti, hori = 0;
	for (int i = 0; i < n; i++)
	{
		hori += arr[i][0];
		for (int j = 1; j < m; j++)
		{
			if (arr[i][j] > arr[i][j - 1])
				hori += arr[i][j] - arr[i][j - 1];
		}
	}

	for (int j = 0; j < m; j++)
	{
		hori += arr[0][j];
		for (int i = 1; i < n; i++)
		{
			if (arr[i][j] > arr[i - 1][j])
				hori += arr[i][j] - arr[i - 1][j];
		}
	}
	result = ((n * m) + verti + hori) * 2;
	printf("%d", result);
	return 0;
}

// N, M = map(int, input().split())
// arr = [list(map(int, input().split())) for _ in range(N)]

// up = N * M

// left = 0
// for i in range(N):
//     for j in range(M):
//         if j == 0:
//             left += arr[i][j]
//         else:
//             if arr[i][j-1] < arr[i][j]:
//                 left += arr[i][j] - arr[i][j-1]

// front = 0
// for j in range(M):
//     for i in range(N):
//         if i == 0:
//             front += arr[i][j]
//         else:
//             if arr[i-1][j] < arr[i][j]:
//                 front += arr[i][j] - arr[i-1][j]
        
// answer = 2 * (up + left + front)
// print(answer)
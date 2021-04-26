#include <stdio.h>

int check(int arr[102][102], int i, int j)
{
	int n = 0;

	if(0 < arr[i][j])
	{
		if (arr[i-1][j] <= 0)
			n++;
		if (arr[i+1][j] <= 0)
			n++;
		if (arr[i][j+1] <= 0)
			n++;
		if (arr[i][j-1] <= 0)
			n++;
	}
	return (n);
}

int	main()
{
	int N, M;
	int arr[102][102] = {0,};
	int res;
	int max = 0;

	scanf("%d %d\n", &N, &M);
	for(int i = 1; i <= M; i++) //입력받기
	{
		for(int j = 1; j <= N; j++)
		{
			scanf("%d", &arr[i][j]);
			if (max < arr[i][j])
				max = arr[i][j];
		}
	}
	res = M * N * 2;
	while(max--)
	{
		for(int i =1; i <= M; i++)
		{
			for(int j = 1; j <= N; j++)
				res += check(arr, i, j);
		}
		for(int i =1; i <= M; i++) //한층씩 내리기
		{
			for(int j = 1; j <= N; j++)		
				arr[i][j]--;
		}
	}
	printf("%d", res);
	return 0;
}
//ㅠㅠ.... 

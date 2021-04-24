#include <stdio.h>

int	LIS(int	*a, int	n)
{
	int dp[n];
	int	max = 0;
	int	lis = 0;

	for (int i = n - 1; i >= 0; i--)
	{
		max = 0;
		for (int j = i + 1; j < n; j++)
			if (a[i] < a[j] && max < dp[j])
				max = dp[j];
		dp[i] = a[i] + max;
		if (lis < dp[i])
			lis = dp[i];
	}
	return (lis);
}

int	main(void)
{
	int	n;

	scanf("%d", &n);

	int	a[n];

	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);

	printf("%d\n", LIS(a, n));
	return (0);
}
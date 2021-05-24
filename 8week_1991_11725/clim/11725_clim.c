#include <stdio.h>
#include <stdbool.h>

bool array[100001][100001] = {0,};
short parent[100001] = {0,};

void mark_parent(int i, int j, int cnt)
{
	if (j >= cnt || i >= cnt)
		return ;
	while (j <= cnt)
	{
		if (array[i][j] == 1 && parent[j] == 0)
		{
			parent[j] = i;
			mark_parent(j, 1, cnt);
		}
		++j;
	}
	return ;
}

int main()
{
	int cnt, i = 1, a, b;

	scanf("%d", &cnt);
	while (i < cnt)
	{
		scanf("%d %d", &a, &b);
		array[a][b] = 1;
		array[b][a] = 1;
		++i;
	}
	mark_parent(1, 1, cnt);
	for (i = 2; i <= cnt; i++)
		printf("%d\n", parent[i]);
}

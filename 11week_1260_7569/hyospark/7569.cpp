#include <vector>
#include <stack>
#include <cstdio>

using namespace std;

int  tomato[100][100][100];
stack <pair<pair<int, int>, int> > stk;
int mh[6] = {0, 0, 1, -1, 0, 0};
int mn[6] = {1, -1, 0, 0, 0, 0};
int mm[6] = {0, 0, 0, 0, 1, -1};
int result = -1;
int m, n, h, tem;
int check = 0;

void	input()
{
	scanf("%d%d%d", &m,&n,&h);
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int z = 0; z < m; z++)
			{
				scanf("%d", &tem);
				tomato[i][j][z] = tem;
				if (tomato[i][j][z] == 1)
					stk.push(make_pair(make_pair(i, j),z));
			}
		}
	}
	while (!stk.empty())
	{
		printf("m : %d  n: %d  h : %d\n", stk.top().first.first, stk.top().first.second, stk.top().second);
		stk.pop();
	}
	
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int z = 0; z < m; z++)
			{
				if (tomato[i][j][z] == 0)
					check = 1;
			}
		}
	}

}

int main()
{
	input();
	int a,b,c;
	if (check == 0)
	{
		printf("%d", 0);
		return 0;
	}
	
	while (!stk.empty())
	{
		a = stk.top().first.first;
		b = stk.top().first.second;
		c = stk.top().second;
		stk.pop();
		for (int i = 0; i < 6; i++)
		{
			if((a + mh[i] < h) && (b + mn[i] < n) && (c + mm[i] < m))
			{
				if (tomato[a + mh[i]][b + mn[i]][c + mm[i]] == 0) 
				{
					tomato[a + mh[i]][b + mn[i]][c + mm[i]] = tomato[a][b][c] + 1;
					a += mh[i];
					b += mn[i];
					c += mm[i];
					result = max(tomato[a][b][c], result);
				}
			}
		}
	}

	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int z = 0; z < m; z++)
			{
				if (tomato[i][j][z] == 0)
				{
					printf("%d", -1);
					return 0;
				}
			}
		}
	}
	printf("%d", result);
	
	return 0;
}

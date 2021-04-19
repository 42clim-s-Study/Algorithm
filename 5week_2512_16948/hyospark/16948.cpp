#include <cstdio>
#include <queue>
using namespace std;
int main()
{
	int n;
	scanf("%d", &n);
	int map[200][200] = {0,};
	int result;

	int r1,c1,r2,c2;
	scanf("%d%d%d%d", &r1, &c1, &r2, &c2);
	queue <pair<int, int> > queue;
	
	int mov_r[6] = {-2, -2, 0, 0, 2, 2};
	int mov_c[6] = {-1, 1, -2, 2, -1, 1};
	queue.push(make_pair(r1,c1));
	while (!queue.empty())
	{
		result = 0;
		for (int i = 0; i < 6; i++)
		{
			int rr = queue.front().first + mov_r[i];
			int cc = queue.front().second + mov_c[i];
			if(rr >= 0 && rr < n && cc >= 0 && cc < n)
			{
				if (map[rr][cc])
					continue ;
				map[rr][cc] = map[queue.front().first][queue.front().second] + 1;
				if (rr == r2 && cc == c2)
				{
					printf("%d", map[rr][cc]);
					return 0;
				}
				queue.push(make_pair(rr,cc));
			}
		}
		queue.pop();
	}
	printf("%d", -1);
	return 0;
}
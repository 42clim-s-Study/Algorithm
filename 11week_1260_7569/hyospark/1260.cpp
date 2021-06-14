#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

vector <int> arr[1001];
bool vis[1001];
bool vis2[1001];

void dfs(int start)
{
	printf("%d ", start);
	int n = arr[start].size();
	sort(arr[start].begin(), arr[start].end());
	for (int i = 0; i < n; i++)
	{
		if (vis[arr[start][i]])
			continue;
		vis[arr[start][i]] = true;
		dfs(arr[start][i]);
	}
}
int main()
{
	int n, m, v;
	queue <int> que;
	scanf("%d%d%d", &n, &m, &v);
	
	int key, val;
	for (int i = 0; i < m; i++)
	{
		scanf("%d%d", &key, &val);
		arr[key].push_back(val);
		arr[val].push_back(key);
	}
	vis[v] = 1;
	dfs(v);
	printf("\n");
	que.push(v);
	vis2[v] = true;
	while(!que.empty())
	{
		int i = que.front();
		que.pop();
		printf("%d ", i);
		int n = arr[i].size();
		for (int j = 0; j < n; j++)
		{
			if (vis2[arr[i][j]])
				continue ;
			vis2[arr[i][j]] = true;
			que.push(arr[i][j]);
		}
	}
}

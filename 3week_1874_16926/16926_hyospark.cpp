#include <cstdio>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
	int n,m,r;
	scanf("%d%d%d",&n,&m,&r);
	int arr[n][m];
	int new_arr[1][1] = {0,};
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			scanf("%d", &arr[i][j]);
	}
	n--;
	m--;
	for (int i = 0; i < r; i++)
	{
		int new_n = n;
		int n_n =0;
		int new_m = m;
		int m_m = 1;
		for (int j = 0; j <= n/2; j++)
		{
			for (int z = m_m; z <= new_m; z++)
			{
				new_arr[j][z - 1] = arr[j][z];
				printf("arr [%d][%d] : %d", j, z,  arr[j][z]);
			}
			m_m++;
			new_m--;
		}		printf("\n");

		m_m = 0;
		new_m = m;
		for (int j = n; j >= n/2; j--)
		{
			for (int z = m_m; z < new_m; z++)
			{
				new_arr[j][z + 1] = arr[j][z];
				printf("arr [%d][%d] : %d", j, z, arr[j][z]);
			}
			m_m++;
			new_m--;
		}		printf("\n");

		for (int j = 0; j <= m/2; j++)
		{
			for (int z = n_n; z < new_n; z++)
			{
				new_arr[z + 1][j] = arr[z][j];
				printf("arr [%d][%d] : %d", z, j, arr[z][j]);

			}
			n_n++;
			new_n--;
		}
		printf("\n");
		n_n = 0;
		new_n = n;
		for (int j = m; j >= m/2; j--)
		{
			for (int z = new_n; z > n_n; z--)
			{
				new_arr[z - 1][j] = arr[z][j];
				printf("arr [%d][%d] : %d", z, j, arr[z][j]);
			}
			n_n++;
			new_n--;
		}		printf("\n");

		for (int i = 0; i <= n; i++)
		{
			for (int j = 0; j <= m; j++)
				arr[i][j] = new_arr[i][j];
		}
	}
	
	
	return 0;
}
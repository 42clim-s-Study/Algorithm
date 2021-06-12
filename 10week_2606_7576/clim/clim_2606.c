#include <stdio.h>
#include <stdbool.h>

static int count;
short matrix[101][101] = {0,};
bool check[101] = {0,};

void dfs(int i, int max);

int main()
{
    int i, ii, j, n;

    scanf("%d %d", &n , &ii);
    while (ii--)
    {
        scanf("%d %d", &i, &j);
        matrix[i][j] = true;
        matrix[j][i] = true;
    }
    dfs(1, n);
    printf("%d\n", count);
}

void dfs(int i, int max)
{
    if (i > max)
        return ;
    check[i] = true;
    for (int j = 0; j <= max ; j++)
    {
        if (matrix[i][j] == true && check[j] == false)
        {
            count++;
            dfs(j, max);
        }
    }
}

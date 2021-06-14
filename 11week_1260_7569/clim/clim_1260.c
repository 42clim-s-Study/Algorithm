#include <stdio.h>

short int DFS_visit[1001] = {0,};
short int BFS_visit[1001] = {0,};
short int matrix[1001][1001];
short int queue[1001];
short int q_push_ptr = 0, q_pop_ptr = 0;

void DFS(int search_node, int max);
void BFS(int search_node, int max);

int main(void) {
    int N, M, V, a, b;
    
    scanf("%d %d %d", &N, &M, &V);
        for (int i = 0; i < M; i++)
    {
        scanf("%d %d",&a ,&b);
        matrix[a][b] = 1;
        matrix[b][a] = 1;
    }
    DFS(V, N);
    printf("\n");
    BFS_visit[V] = 1;
    BFS(V, N);
    return 0;
}

void DFS(int search_node, int max)
{
    DFS_visit[search_node] = 1;
    printf("%d ", search_node);
    for (int i = 1; i <= max; i++)
        if (matrix[search_node][i] == 1 && DFS_visit[i] == 0)
            DFS(i, max);
}

void BFS(int search_node, int max)
{
    printf("%d ", search_node);
    for (int i = 1; i <= max; i++)
    {
        if (matrix[search_node][i] == 1 && BFS_visit[i] == 0)
        {
            queue[q_push_ptr++] = i;
            BFS_visit[i] = 1;
        }
    }
    if (q_pop_ptr < q_push_ptr)
        BFS(queue[q_pop_ptr++], max);
}

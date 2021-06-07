#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

static int verti, hori, day;
int matrix[1001][1001] = {0,};
int matrix_cp[1001][1001] = {0,};
int check[1001][1001] = {false,};

void printmap();
void day_after();
int update_matrix();
int check_ripe_all();

int main()
{
    int i = 1, j = 1;

    scanf("%d %d", &hori , &verti);
    while (i <= verti)
    {
        j = 1;
        while (j <= hori)
        {
            scanf("%d", &matrix[i][j]);
            matrix_cp[i][j] = matrix[i][j];
            j++;
        }
        i++;
    }
    if (check_ripe_all() == 1)
    {
        printf("0\n");
        return (0);
    }
    day_after();
    printf("%d\n", day);
    return (0);
}

void day_after()
{
    int i = 1, j = 1;
    
    if (check_ripe_all() == 1)
        return ;
    while (i <= verti)
    {
        j = 1;
        while (j <= hori)
        {
            if (matrix[i][j] == 1 && check[i][j] == false)
            {
                check[i][j] = true;
                if (matrix_cp[i+1][j] != -1)
                    matrix_cp[i+1][j] = 1;
                if (matrix_cp[i-1][j] != -1)
                    matrix_cp[i-1][j] = 1;
                if (matrix_cp[i][j+1] != -1)
                    matrix_cp[i][j+1] = 1;
                if (matrix_cp[i][j-1] != -1)
                    matrix_cp[i][j-1] = 1;
            }
            j++;
        }
        i++;
    }
    day++;
    if (update_matrix() == -1)
    {
        printf("-1\n");
        exit(0);
    }
    day_after();
}

int update_matrix()
{
    bool update = false;
    int i = 1, j = 1;

    while (i <= verti)
    {
        j = 1;
        while (j <= hori)
        {
            if (matrix[i][j] != matrix_cp[i][j])
            {
                matrix[i][j] = matrix_cp[i][j];
                update = true;
            }
            j++;
        }
        i++;
    }
    if (update == false)
        return (-1);
    return (0);
}

int check_ripe_all()
{
    int i = 1, j = 1;

    while (i <= verti)
    {
        j = 1;
        while (j <= hori)
        {
            if (matrix[i][j] == 0)
                return (0);
            j++;
        }
        i++;
    }
    return (1);
}

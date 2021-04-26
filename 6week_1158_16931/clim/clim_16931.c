// 틀린 코드임 !

#include <stdio.h>

int main()
{
  int N, M, i = 0, j, ans = 0;
  scanf("%d %d", &N, &M);
  
  int box[N][M];
  int vertical_max[N];
  int horizontal_max[M];
  while(i < N)
  {
    j = 0;
    while (j < M)
    {
      scanf("%d", &box[i][j]);
      if (box[i][j] > horizontal_max[i])
        horizontal_max[i] = box[i][j];
      j++;
    }
    i++;
  }
  j = 0;
  while(j < M)
  {
    i = 0;
    while (i < N)
    {
      if (vertical_max[j] < box[i][j])
        vertical_max[j] = box[i][j];
      i++;
    }
    j++;
  }
  i = 0;
  j = 0;
  while(i < N)
    ans += horizontal_max[i++] * 2;
  while(j < M)
    ans += vertical_max[j++] * 2;
  ans += (N * M) * 2;
  printf("%d\n", ans);
}

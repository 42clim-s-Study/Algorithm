#include <stdio.h>

int main(void) {
  int size;
  int i = 0, j = 0;
  int input[1000] = {0,} , sum[1000] = {0,};
  int max;

  scanf("%d", &size);
  while(i < size)
  {
    scanf("%d", &input[i]);
    sum[i] = input[i];
    i++;
  }
  max = sum[0];
  for(i = 0; i < size; i++)
  {
    for(j = i + 1; j < size; j++)
    {
      if (input[i] < input[j] && sum[j] < sum[i] + input[j])
      {
        sum[j] = sum[i] + input[j];
        if (sum[j] > max)
          max = sum[j];
      }
    }
  }
  printf("%d", max);
}

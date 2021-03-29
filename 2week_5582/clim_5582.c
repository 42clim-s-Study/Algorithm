//시간 초과 코드..
#include <stdio.h>
#include <string.h>

int main ()
{
  char s1[4001], s2[4001];
  int i, j, tmp, max, s1_len, s2_len;

  i = 0;
  max = 0;
  scanf("%s %s", s1, s2);
  s1_len = strlen(s1);
  s2_len = strlen(s2);
  while (i < s1_len)
  {
    j = 0;
    while (j < s2_len)
    {
      tmp = 0;
      while (s1[i + tmp] == s2[j + tmp] && i + tmp < s1_len && j + tmp < s2_len)
        ++tmp;
      if (tmp > max)
        max = tmp;
      ++j;
    }
    ++i;
  }
  printf("%d", max);
}


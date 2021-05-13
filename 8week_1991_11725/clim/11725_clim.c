nclude <stdio.h>
#include <stdbool.h>

typedef struct node{
  int parent;
} node;

node nd[100000];

int main()
{
  int n, i = 0;
  int i1, i2;
  bool check[100000] = {0,};
  check[1] = 1;
  scanf("%d", &n);
  while(++i < n)
  {
    scanf("%d %d", &i1, &i2);
    if (check[i1] == 1)
    {
      nd[i2].parent = i1;
      check[i2] = 1;
    }
    else if(check[i2] == 1)
    {
      nd[i1].parent = i2;
      check[i1] = 1;
    }
  }
  for(i = 2; i <= n; i++)
  {
    printf("%d\n",nd[i].parent);
  }
}

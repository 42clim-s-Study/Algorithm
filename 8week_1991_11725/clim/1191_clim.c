nclude <stdio.h>

typedef struct node{
  char right;
  char left;
} node;

node nd[28];

void preorder(char c)
{
  if (c == '.')
    return;
  printf("%c", c);
  preorder(nd[c-'A'].left);
  preorder(nd[c-'A'].right);
}

void inorder(char c)
{
  if (c == '.')
    return;
  inorder(nd[c-'A'].left);
  printf("%c", c);
  inorder(nd[c-'A'].right);
}

void postorder(char c)
{
  if (c == '.')
    return;
  postorder(nd[c-'A'].left);
  postorder(nd[c-'A'].right);
  printf("%c", c);
}

int main()
{
  int n, i = 0;
  char c1, c2, c3;

  scanf("%d", &n);
  while(i < n)
  {
    scanf(" %c %c %c", &c1, &c2, &c3);
    nd[c1-'A'].left = c2;
    nd[c1-'A'].right = c3;
    i++;
  }
  preorder('A');
  printf("\n");
  inorder('A');
  printf("\n");
  postorder('A');
}

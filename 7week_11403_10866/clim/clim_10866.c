nclude <stdio.h>
#include <string.h>
#include <stdbool.h>

void pop(int deque[], int *top_cursor, int *bottom_cursor, bool front)
{
  if (*top_cursor < *bottom_cursor)
      printf("-1\n");
  else if (front)
  {
      printf("%d\n", deque[*top_cursor]);
      deque[*top_cursor] = 0;
      --(*top_cursor);
  }
  else
  {
    printf("%d\n", deque[*bottom_cursor]);
    deque[*bottom_cursor] = 0;
    ++(*bottom_cursor);
  }
}

void push(int deque[], int num, int *top_cursor, int *bottom_cursor, bool front)
{
  if (front)
  {
    deque[*top_cursor+1] = num;
    ++(*top_cursor);
  }
  else
  {
    deque[*bottom_cursor-1] = num;
    --(*bottom_cursor);
  }
}

void empty(int top_cursor, int bottom_cursor)
{
  if (top_cursor < bottom_cursor)
    printf("1\n");
  else
    printf("0\n");
}

void size(int top_cursor, int bottom_cursor)
{
  printf("%d\n", top_cursor - bottom_cursor + 1);
}

void print(int deque[], int num, int top_cursor, int bottom_cursor, bool front)
{
  if (top_cursor < bottom_cursor)
    printf("-1\n");
  else if (front)
    printf("%d\n", deque[top_cursor]);
  else
    printf("%d\n", deque[bottom_cursor]);
}

int main(void) {
    int deque[20000] = {0,};
    int bottom_cursor = 0, top_cursor = 0, n, num;
    char command[20];

    top_cursor = 9999;
    bottom_cursor = 10000;
    scanf("%d", &n);
    while(n--)
    {
      scanf("%s", command);
      if (strcmp(command, "push_back") == 0)
      {
        scanf("%d", &num);
        push(deque, num, &top_cursor, &bottom_cursor, 0);
      }
      if (strcmp(command, "push_front") == 0)
      {
        scanf("%d", &num);
        push(deque, num, &top_cursor, &bottom_cursor, 1);
      }
      if (strcmp(command, "pop_back") == 0)
        pop(deque, &top_cursor, &bottom_cursor, 0);
      if (strcmp(command, "pop_front") == 0)
        pop(deque, &top_cursor, &bottom_cursor, 1);
      if (strcmp(command, "size") == 0)
        size(top_cursor, bottom_cursor);
      if (strcmp(command, "empty") == 0)
        empty(top_cursor, bottom_cursor);
      if (strcmp(command, "front") == 0)
        print(deque, num, top_cursor, bottom_cursor, 1);
      if (strcmp(command, "back") == 0)
        print(deque, num, top_cursor, bottom_cursor, 0);
    }
}

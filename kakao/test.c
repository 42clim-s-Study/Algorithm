#include <stdio.h>
int moon[] = {1,2,3,4,5,6,7,8,9,10};
int main(int argc, char const *argv[])
{
	int i , sum = 0;
	for (i = 0; i < 8; i++)
	{
			printf("i : %d\n",i);
		if (moon[i] %2 ==0)
		{
			sum += moon[i];
			printf("sum : %d\n",sum);
		}
	}
	return 0;
}

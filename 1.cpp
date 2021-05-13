#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
	int i = 0;
	int n = s.length();
	for (int i = 0; i < n; i++)
	{
		if (s[i] >= '0' && s[i] <= '9')
			answer = (s[i] - '0') + (answer * 10);
		else
		{
			if (s[i] == 'z')
			{
				answer = 0 + (answer * 10);
				i += 3;
			}
			else if (s[i] == 'o')
			{
				answer = 1 + (answer * 10);
				i += 2;
			}
			else if (s[i] == 't' && s[i + 1] == 'w')
			{
				answer = 2 + (answer * 10);
				i += 2;
			}
			else if (s[i] == 't' && s[i + 1] == 'h')
			{
				answer = 3 + (answer * 10);
				i += 4;
			}
			else if (s[i] == 'f' && s[i + 1] == 'o')
			{
				answer = 4 + (answer * 10);
				i += 3;
			}
			else if (s[i] == 'f' && s[i + 1] == 'i')
			{
				answer = 5 + (answer * 10);
				i += 3;
			}
			else if (s[i] == 's' && s[i + 1] == 'i')
			{
				answer = 6 + (answer * 10);
				i += 2;
			}
			else if (s[i] == 's' && s[i + 1] == 'e')
			{
				answer = 7 + (answer * 10);
				i += 4;
			}
			else if (s[i] == 'e')
			{
				answer = 8 + (answer * 10);
				i += 4;
			}
			else if (s[i] == 'n')
			{
				answer = 9 + (answer * 10);
				i += 3;
			}
		}
	}
    return answer;
}
int main(int argc, char const *argv[])
{
	string art = "one4seveneight";
	printf("%d", solution(art));
	return 0;
}

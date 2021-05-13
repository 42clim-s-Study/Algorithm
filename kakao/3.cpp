#include <string>
#include <vector>
#include <iostream>
#include <stack>
using namespace std;

string solution(int n, int k, vector<string> cmd) {
    string answer = "";
	vector <int> vec;
	stack <pair<int, int> > stack;

	int len = n;
	int cmdn = cmd.size();

	for (int i = 0; i < n; i++)
	{
		vec.push_back(i);
		answer += 'O';
	}
		
	for (int i = 0; i < cmdn; i++)
	{
		if (cmd[i][0] == 'U')
		{
			string tem = cmd[i].substr(2);
			k -= stoi(tem);
			printf("%d\n", k);
		}
		else if (cmd[i][0] == 'D')
		{
			string tem = cmd[i].substr(2);
			k += stoi(tem);
			printf("%d\n", k);
		}
		else if (cmd[i][0] == 'C')
		{
			answer[vec[k]] = 'X';
			stack.push(make_pair(vec[k], k));
			vec.erase(vec.begin() + k);
			len--;
			if (k >= len)
				k = len - 1;
		}
		else if (cmd[i][0] == 'Z')
		{
			answer[stack.top().first] = 'O';
			vec.insert(vec.begin() + stack.top().second, stack.top().first);
			cout << "first" << stack.top().first << '\n';
			prin
			cout << "second" << stack.top().second << '\n';
			stack.pop();
			len++;
		}
	}
    return answer;
}
int main(int argc, char const *argv[])
{
	string str = solution(8, 2,{"D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"} );
	cout << str << '\n';
	return 0;
}

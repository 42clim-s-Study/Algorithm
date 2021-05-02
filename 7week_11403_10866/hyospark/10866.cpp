#include <iostream>
#include <deque>

using namespace std;

deque <int> dq;

void	check_push_val(string str, int num)
{
	if (str == "push_front")
		dq.push_front(num);
	else if (str == "push_back")
		dq.push_back(num);
}

void	check_val(string str)
{
	if (str == "pop_front")
	{
		if (dq.empty())
			cout << -1 << '\n';
		else
		{
			cout << dq.front() << '\n';
			dq.pop_front();
		}
	}
	else if (str == "pop_back")
	{
		if (dq.empty())
			cout << -1 << '\n';
		else
		{
			cout << dq.back() << '\n';
			dq.pop_back();
		}
	}
	else if (str == "size")
		cout << dq.size() << '\n';
	else if (str == "empty")
	{
		if (dq.empty())
			cout << 1 << '\n';
		else
			cout << 0 << '\n';
	}
	else if (str == "front")
	{
		if (dq.empty())
			cout << -1 << '\n';
		else
			cout << dq.front() << '\n';
	}
	else if (str == "back")
	{
		if (dq.empty())
			cout << -1 << '\n';
		else
			cout << dq.back() << '\n';
	}
}

int main()
{
	int n;
	string str;
	int num;
	int result;
	scanf("%d" , &n);
	for (int i = 0; i < n; i++)
	{
		cin >> str;
		if (str[1] == 'u')
		{
			cin >> num;
			check_push_val(str, num);
		}
		else
			check_val(str);
	}
	return 0;
}

#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<vector<string> > places) {
	vector<int> answer;
	int arr[5];
	int i_m[8] = {1, 0, -1, 0, -1, 1, -1, 1};
	int j_m[8] = {0, 1, 0, -1, -1, -1, 1, 1};

	for (int n = 0; n < 5; n++)
	{
		int check = 1;
		for (int i = 0; i < 5; i++)
		{
			for (int j = 0; j < 5; j++)
			{
				if (places[n][i][j] == 'P')
				{
					for (int x = 0; x < 4; x++)
					{
						if ((i + i_m[x] >= 0 && j + j_m[x] >= 0 && i + i_m[x] < 5 && j_m[x] < 5))
						{
							if (places[n][i + i_m[x]][j + j_m[x]] == 'P')
								check = 0;
						}
					}
					for (int x = 4; x < 8; x++)
					{
						if ((i + i_m[x] >= 0 && j + j_m[x] >= 0 && i + i_m[x] < 5 && j_m[x] < 5))
						{
							if (places[n][i + i_m[x]][j + j_m[x]] == 'P' && 
							(places[n][i][j + j_m[x]] == 'O' || places[n][i + i_m[x]][j] == 'O')){
								check = 0;
							}
						}
					}
					
				}
			}
		}
		answer.push_back(check);
	}
	
    return answer;
}

int main(int argc, char const *argv[])
{
	vector <vector <string> > vec = {{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"}, 
	{"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"}, 
	{"PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"}, 
	{"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"}, 
	{"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};
	vector <int> ivec;
	ivec = solution(vec);
	for (int i = 0; i < 5; i++)
	{
		cout << ivec[i] << '\n';
	}
	
	return 0;
}

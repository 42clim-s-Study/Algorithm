# 두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 부분 문자열을 찾는 프로그램을 작성하시오.
# 어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다.
# 예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다.
# 하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

# 두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다.
# 이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다.
# 또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

# 입력 : 첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.
# 출력 : 첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.


# 메모리 초과
def solution_001(s1: str, s2: str):
    joint_set = set()
    subset_s1 = set()
    subset_s2 = set()
    subset_s1.add("")
    subset_s2.add("")
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 > len_s2:
        for i in range(len_s1):
            for j in range(len_s1 - i):
                if len(s1[i:i + j + 1]) < len_s2:
                    subset_s1.add(s1[i:i + j + 1])
        for i in range(len_s2):
            for j in range(len_s2 - i):
                if len(s2[i:i + j + 1]):
                    subset_s2.add(s2[i:i + j + 1])
    else:
        for i in range(len_s1):
            for j in range(len_s1 - i):
                if len(s1[i:i + j + 1]):
                    subset_s1.add(s1[i:i + j + 1])
        for i in range(len_s2):
            for j in range(len_s2 - i):
                if len(s2[i:i + j + 1]) < len_s1:
                    subset_s2.add(s2[i:i + j + 1])

    print(len(subset_s1), subset_s1)
    print(len(subset_s2), subset_s2)
    joint_set = subset_s1 & subset_s2
    print(joint_set)
    joint_list = list(joint_set)
    longest = [0, ""]
    for i in range(len(joint_list)):
        if len(joint_list[i]) >= longest[0]:
            longest[0] = len(joint_list[i])
            longest[1] = joint_list[i]
    print(longest[0])


# 시간 초과
def solution_002(s1: str, s2: str):
    longest = 0
    count = 0
    len_s1 = len(s1)
    len_s2 = len(s2)
    # print(len_s1, len_s2)
    for i in range(len_s1):
        tmp = i
        for j in range(len_s2):
            while s1[i] == s2[j]:
                count += 1
                i += 1
                j += 1
                if i >= len_s1 or j >= len_s2:
                    break
            i = tmp
            if longest < count:
                longest = count
            count = 0
    print(longest)


# DP (pypy3 : 메모리 248472 KB, 448 ms / python3 : 시간 초과)
def solution_003(s1: str, s2: str):
    s1 = '0' + s1
    s2 = '0' + s2
    # print(s1, s2)
    s1_len = len(s1)
    s2_len = len(s2)
    lcs = [[0] * s2_len for _ in range(s1_len)]
    res = 0

    for i in range(1, s1_len):
        for j in range(1, s2_len):
            if s1[i] == s2[j]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
                res = max(res, lcs[i][j])
    print(res)


if __name__ == "__main__":
    # s1 = input()
    # s2 = input()
    # solution_001(s1, s2)
    s1 = "ABRACADABRA"
    s2 = "ECADADABRBCRDARA"
    solution_003(s1, s2)

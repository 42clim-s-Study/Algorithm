"""
16931 겉넓이 구하기

크기가 N×M인 종이가 있고, 종이는 1×1크기의 칸으로 나누어져 있다.
이 종이의 각 칸 위에 1×1×1 크기의 정육면체를 놓아 3차원 도형을 만들었다.
종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오.
"""


def solution_001():
    height, width = map(int, input().split())
    count = height * width * 2
    """
    arr = []
    for _ in range(height):
        row = list(map(int, input().split()))
        assert len(row) == width, "input error"
        arr.append(row)
    """
    arr = [list(map(int, input().split())) for _ in range(height)]
    brr = [[0] * (width + 2) for _ in range(height + 2)]

    for i in range(height):
        for j in range(width):
            brr[i+1][j+1] = arr[i][j]

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            curr = brr[i][j]
            if curr - brr[i-1][j] > 0:
                count += (curr - brr[i-1][j])
            if curr - brr[i][j-1] > 0:
                count += (curr - brr[i][j-1])
            if curr - brr[i+1][j] > 0:
                count += (curr - brr[i+1][j])
            if curr - brr[i][j+1] > 0:
                count += (curr - brr[i][j+1])
    print(count)


if __name__ == "__main__":
    solution_001()

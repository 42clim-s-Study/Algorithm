# Stack
# LIFO (Last In First Out)
# Python list.append() == stack.push()
# Python list.pop() == stack.pop()
# Python list[-1] == stack.top()


# example_01
# a = 8
# b = [4, 3, 6, 8, 7, 5, 2, 1]

# example_02
# a = 5
# b = [1, 2, 5, 3, 4]


def solution_001(n: int, target: list):
    stack = []
    record = []
    flag = True
    seq = 0

    for now in target:
        while seq < now:
            seq += 1
            stack.append(seq)
            record.append("+")
        if stack[-1] == now:
            stack.pop()
            record.append("-")
        else:
            flag = False
            break
    if not flag:
        print("NO")
    else:
        for elem in record:
            print(elem)


if __name__ == "__main__":
    seq_len = int(input())
    to_make = []
    for _ in range(seq_len):
        to_make.append(int(input()))

    solution_001(seq_len, to_make)

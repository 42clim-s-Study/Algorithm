"""
1158 요세푸스 문제 - 자료구조 : 원형 연결리스트

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
양의 정수 K(≤ N)가 주어진다.
순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.

원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""


# 원형 연결리스트
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node('head')
        self.head.next = self.head
        self.current = self.head

    def insert(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.current.next = new_node
        self.current = new_node

    def find_next(self, n):
        for _ in range(n):
            if self.current.next.element == 'head':
                self.current = self.current.next
            self.current = self.current.next
        return self.current.element

    def remove(self, node):
        prev_node = self.head
        while prev_node.next != node:
            prev_node = prev_node.next
        prev_node.next = prev_node.next.next

    def show(self):
        curr_node = self.head
        while curr_node.next.element != 'head':
            print(curr_node.element, end=' -> ')
            curr_node = curr_node.next
        print(curr_node.element)


# 리스트
def solution_001(n, k):
    # init
    arr = [x for x in range(1, n+1)]
    idx = 0
    res = []
    while arr:
        idx += (k-1)
        if idx > len(arr)-1:
            idx %= len(arr)
        res.append((arr.pop(idx)))
    return res


# 원형 연결리스트
def solution_002(n, k):
    corps = CircularLinkedList()
    res = []
    # init
    for i in range(1, n+1):
        corps.insert(i)
    # corps.show()
    for _ in range(n):
        res.append(corps.find_next(k))
        # corps.show()
        corps.remove(corps.current)
    return res


if __name__ == "__main__":
    n, k = map(int, input().split())

    print("\n ===== 리스트 풀이 =====")
    josephus_001 = solution_001(n, k)
    print("<" + str(josephus_001)[1:-1] + ">")

    print("\n ===== 원형 연결리스트 풀이 =====")
    josephus_002 = solution_002(n, k)
    print("<" + str(josephus_002)[1:-1] + ">")


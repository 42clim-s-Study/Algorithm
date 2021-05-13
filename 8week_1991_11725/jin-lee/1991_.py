"""
1991 트리순회
https://www.acmicpc.net/problem/1991

이진 트리를 입력받아
전위 순회(preorder traversal),
중위 순회(inorder traversal),
후위 순회(postorder traversal)한
결과를 출력하는 프로그램을 작성하시오.

노드의 수
for _ in range(노드의 수):
    parent_item, left_item, right_item = input().split()

입력 예1
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

출력 예1
ABDCEFG (preorder traversal)
DBAECFG (inorder traversal)
DBEGFCA (postorder traversal)
"""


class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


# 전위 순회 (parent -> lchild -> rchild)
def preorder(node):
    print(node.item, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


# 중위 순회 (lchild -> parent -> rchild)
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != '.':
        inorder(tree[node.right])


# 후위 순회 (lchild -> rchild -> parent)
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end="")


if __name__ == "__main__":
    size = int(input())
    tree = {}
    for _ in range(size):
        parent, lchild, rchild = input().split()
        tree[parent] = Node(item=parent, left=lchild, right=rchild)
    print(tree)
    print(tree["A"].item, tree["A"].left, tree["A"].right)

    preorder(tree["A"])
    print()
    inorder(tree["A"])
    print()
    postorder(tree["A"])

# python3

import sys
import threading


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def compute_height(n, parents):

    Tree = []

    for i in range(len(parents)):
        Tree.append(Node(parents[i]))

    for t in range(len(Tree)):
        if Tree[t].key == -1:
            Tree[t].key = 'root'
        else:
            if Tree[Tree[t].key].left == None:
                Tree[Tree[t].key].left = Tree[t]
            else:
                Tree[Tree[t].key].right = Tree[t]

    for d in range(len(Tree)):
        if Tree[d].key == 'root':
            Root = Tree[d]
    Tree_Stack = []
    Tree_Stack.append((1, Root))
    deep = 0
    while Tree_Stack != []:
        cur_deep, Root = Tree_Stack.pop()
        if cur_deep > deep:
            deep = cur_deep
        if Root.left != None:
            Tree_Stack.append((cur_deep+1, Root.left))
        if Root.right != None:
            Tree_Stack.append((cur_deep+1, Root.right))
    return deep








def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

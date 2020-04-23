class Node(object):
    def __init__(self, key):
        self.key = key
        self.pre = None
    def __str__(self):
        return '{}--->{}'.format(self.key, self.pre)


class Stack(object):
    def __init__(self):
        self.bottom = Node('tail')
        self.top = Node('Top')

    def plug_in(self, key):
        new_node = Node(key)
        B = self.bottom
        while B.pre :
            B = B.pre
        else :
            B.pre = new_node
            self.top = new_node

    def show(self):
        print('stack:', self.bottom)

    def Pop(self):
        print(self.top)


S = Stack()
S.plug_in(2)
S.plug_in(3)
S.plug_in(5)
S.show()
S.Pop()
S.plug_in(11)
S.show()
S.Pop
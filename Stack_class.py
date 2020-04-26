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
        self.length = 0

    def plug_in(self, key):
        new_node = Node(key)
        B = self.bottom
        while B.pre :
            B = B.pre
        else :
            B.pre = new_node
            self.top = new_node
        self.length = self.length + 1

    def show(self):
        print('stack:', self.bottom, 'length:', self.length)

    def Pop(self):
        i = 0
        B = self.bottom
        while i < self.length-1 :
            B = B.pre
            i = i + 1
        B.pre = None
        self.length = self.length - 1
        return self.top



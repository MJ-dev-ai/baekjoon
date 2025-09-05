class Node():
    def __init__(self, data):
        self.__data = data
        self.__next = None
    def __str__(self):
        return str(self.__data)
    def get_next(self):
        return self.__next
    def set_next(self, node):
        self.__next = node
    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data = data

class Stack():
    def __init__(self):
        self._top = None
        self._len = 0
    def push(self,data):
        if self._top == None:
            self._top = Node(data)
        else:
            next_node = self._top
            self._top = Node(data)
            self._top.set_next(next_node)
        self._len += 1
    def pop(self):
        if self._len == 0:
            return None
        node = self._top
        self._top = node.get_next()
        node.set_next(None)
        self._len -= 1
        return node.get_data()
    def peek(self):
        if self._top == None:
            return None
        return self._top.get_data()
    def is_empty(self):
        return self._top == None
    def __len__(self):
        return self._len
    def __getitem__(self,idx):
        curr = self._top
        if self._len == 0:
            return None
        idx %= self._len
        if idx == 0: return self._top.get_data()
        else:
            for _ in range(idx):
                curr = curr.get_next()
            return curr.get_data()
    def __str__(self):
        result = "["
        if self._top == None: return "[]"
        cur = self._top
        while cur.get_next() != None:
            result += str(cur.get_data())+","
            cur = cur.get_next()
        result += str(cur.get_data())+"]"
        return result
n = int(input())
for _ in range(n):
    valid = input()
    is_vps = True
    bracket = Stack()
    for ps in valid:
        if ps == "(":
            bracket.push(ps)
        else:
            if bracket.pop() == "(":
                continue
            else:
                is_vps = False
                break
    if not bracket.is_empty(): is_vps = False
    print("YES" if is_vps else "NO")
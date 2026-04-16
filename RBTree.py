RED   = 0
BLACK = 1


class Node:
    def __init__(self, data):
        self.data   = data
        self.color  = RED
        self.left   = None
        self.right  = None
        self.parent = None


class RBTree:

    def __init__(self):
        self.NIL        = Node(None)
        self.NIL.color  = BLACK
        self.root       = self.NIL
        self.size       = 0

    def rotate_left(self, x):
        y         = x.right
        x.right   = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left  = y
        else:
            x.parent.right = y

        y.left   = x
        x.parent = y

    def rotate_right(self, x):
        y        = x.left
        x.left   = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left  = y

        y.right  = x
        x.parent = y

    def insert(self, data):
        new_node        = Node(data)
        new_node.left   = self.NIL
        new_node.right  = self.NIL

        parent  = None
        current = self.root

        while current != self.NIL:
            parent = current
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return False

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif data < parent.data:
            parent.left  = new_node
        else:
            parent.right = new_node

        self.size += 1

        if new_node.parent is None:
            new_node.color = BLACK
            return True

        if new_node.parent.parent is None:
            return True

        self._fix_insert(new_node)
        return True

    def _fix_insert(self, node):
        while node.parent and node.parent.color == RED:

            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == RED:
                    node.parent.color        = BLACK
                    uncle.color              = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color        = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == RED:
                    node.parent.color        = BLACK
                    uncle.color              = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color        = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)

        self.root.color = BLACK

    def search(self, data):
        current = self.root
        while current != self.NIL:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def get_height(self):
        return self._height(self.root)

    def _height(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def get_black_height(self):
        return self._black_height(self.root)

    def _black_height(self, node):
        if node == self.NIL:
            return 1
        left_bh = self._black_height(node.left)
        if node.color == BLACK:
            return left_bh + 1
        return left_bh

    def get_size(self):
        return self.size
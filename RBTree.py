# def create_node(key, tree):
#     return {
#         "key": key,
#         "color": "RED",
#         "left": tree["NIL"],
#         "right": tree["NIL"],
#         "parent": tree["NIL"]
#     }
#
#
# def create_tree():
#     NIL = {
#         "color": "BLACK",
#         "left": None,
#         "right": None,
#         "parent": None
#     }
#     return {
#         "root": NIL,
#         "NIL": NIL
#     }
#
#
# def left_rotate(tree, x):
#     NIL = tree["NIL"]
#     y = x["right"]
#     x["right"] = y["left"]
#     if y["left"] != NIL:
#         y["left"]["parent"] = x
#     y["parent"] = x["parent"]
#     if x["parent"] == NIL:
#         tree["root"] = y
#     elif x == x["parent"]["left"]:
#         x["parent"]["left"] = y
#     else:
#         x["parent"]["right"] = y
#     y["left"] = x
#     x["parent"] = y
#
#
# def right_rotate(tree, x):
#     NIL = tree["NIL"]
#     y = x["left"]
#     x["left"] = y["right"]
#     if y["right"] != NIL:
#         y["right"]["parent"] = x
#     y["parent"] = x["parent"]
#     if x["parent"] == NIL:
#         tree["root"] = y
#     elif x == x["parent"]["right"]:
#         x["parent"]["right"] = y
#     else:
#         x["parent"]["left"] = y
#     y["right"] = x
#     x["parent"] = y
#
#
# def fix_insert(tree, k):
#     NIL = tree["NIL"]
#     while k["parent"]["color"] == "RED":
#         if k["parent"] == k["parent"]["parent"]["left"]:
#             u = k["parent"]["parent"]["right"]
#             if u["color"] == "RED":
#                 k["parent"]["color"] = "BLACK"
#                 u["color"] = "BLACK"
#                 k["parent"]["parent"]["color"] = "RED"
#                 k = k["parent"]["parent"]
#             else:
#                 if k == k["parent"]["right"]:
#                     k = k["parent"]
#                     left_rotate(tree, k)
#                 k["parent"]["color"] = "BLACK"
#                 k["parent"]["parent"]["color"] = "RED"
#                 right_rotate(tree, k["parent"]["parent"])
#         else:
#             u = k["parent"]["parent"]["left"]
#             if u["color"] == "RED":
#                 k["parent"]["color"] = "BLACK"
#                 u["color"] = "BLACK"
#                 k["parent"]["parent"]["color"] = "RED"
#                 k = k["parent"]["parent"]
#             else:
#                 if k == k["parent"]["left"]:
#                     k = k["parent"]
#                     right_rotate(tree, k)
#                 k["parent"]["color"] = "BLACK"
#                 k["parent"]["parent"]["color"] = "RED"
#                 left_rotate(tree, k["parent"]["parent"])
#     tree["root"]["color"] = "BLACK"
#
#
# # ⚠️  EDIT: added duplicate check at the top (2 lines added, nothing else changed)
# def insert(tree, key):
#     NIL = tree["NIL"]
#
#     # --- ADDED: reject duplicates ---
#     if search(tree, key) != NIL:
#         return False  # key already exists, do not insert
#
#     node = create_node(key, tree)
#     parent = NIL
#     current = tree["root"]
#     while current != NIL:
#         parent = current
#         if node["key"] < current["key"]:
#             current = current["left"]
#         else:
#             current = current["right"]
#     node["parent"] = parent
#     if parent == NIL:
#         tree["root"] = node
#     elif node["key"] < parent["key"]:
#         parent["left"] = node
#     else:
#         parent["right"] = node
#     node["color"] = "RED"
#     fix_insert(tree, node)
#     return True  # inserted successfully
#
#
# def search(tree, key):
#     NIL = tree["NIL"]
#     current = tree["root"]
#     while current != NIL and key != current["key"]:
#         if key < current["key"]:
#             current = current["left"]
#         else:
#             current = current["right"]
#     return current
#
#
# def print_tree_height(tree):
#     def height(node):
#         if node == tree["NIL"]:
#             return 0
#         return 1 + max(height(node["left"]), height(node["right"]))
#
#     return height(tree["root"])
#
#
# def print_tree_black_height(tree):
#     def black_height(node):
#         if node == tree["NIL"]:
#             return 0
#         return (1 if node["color"] == "BLACK" else 0) + black_height(node["left"])
#
#     return black_height(tree["root"])


# def print_tree_size(tree):
#     def size(node):
#         if node == tree["NIL"]:
#             return 0
#         return 1 + size(node["left"]) + size(node["right"])
#
#     return size(tree["root"])





# ============================================================
#  Red-Black Tree  +  English Dictionary Application
# ============================================================
#
#  HOW TO RUN:
#    python RBTree_Dictionary.py
#
#  Make sure "dictionary.txt" is in the SAME folder as this file.
# ============================================================


# ──────────────────────────────────────────────
#  SECTION 1 – Node & Constants
# ──────────────────────────────────────────────

RED   = 0
BLACK = 1

class Node:
    def __init__(self, data):
        self.data   = data
        self.color  = RED       # new nodes are always RED
        self.left   = None
        self.right  = None
        self.parent = None


# ──────────────────────────────────────────────
#  SECTION 2 – Red-Black Tree
# ──────────────────────────────────────────────

class RBTree:

    def __init__(self):
        # NIL is a shared sentinel BLACK node used instead of None
        self.NIL        = Node(None)
        self.NIL.color  = BLACK
        self.root       = self.NIL
        self.size       = 0          # tracks number of real nodes

    # ── Rotations ──────────────────────────────

    def rotate_left(self, x):
        y         = x.right
        x.right   = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent  = x.parent

        if x.parent is None:          # x was root
            self.root = y
        elif x == x.parent.left:
            x.parent.left  = y
        else:
            x.parent.right = y

        y.left    = x
        x.parent  = y

    def rotate_right(self, x):
        y         = x.left
        x.left    = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent  = x.parent

        if x.parent is None:          # x was root
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left  = y

        y.right   = x
        x.parent  = y

    # ── Insert ─────────────────────────────────

    def insert(self, data):
        new_node         = Node(data)
        new_node.left    = self.NIL
        new_node.right   = self.NIL

        # --- standard BST insert ---
        parent  = None
        current = self.root

        while current != self.NIL:
            parent = current
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return False          # duplicate – do not insert

        new_node.parent = parent

        if parent is None:            # tree was empty
            self.root = new_node
        elif data < parent.data:
            parent.left  = new_node
        else:
            parent.right = new_node

        self.size += 1

        # if new node is root, just color it BLACK and done
        if new_node.parent is None:
            new_node.color = BLACK
            return True

        # if grandparent is missing (parent is root), nothing to fix
        if new_node.parent.parent is None:
            return True

        # --- fix Red-Black violations ---
        self._fix_insert(new_node)
        return True

    def _fix_insert(self, node):
        # keep fixing while the parent is RED (violation)
        while node.parent and node.parent.color == RED:

            if node.parent == node.parent.parent.left:   # parent is LEFT child
                uncle = node.parent.parent.right

                if uncle.color == RED:
                    # Case 1 – uncle is RED → recolor
                    node.parent.color         = BLACK
                    uncle.color               = BLACK
                    node.parent.parent.color  = RED
                    node = node.parent.parent  # move up

                else:
                    if node == node.parent.right:
                        # Case 2 – node is RIGHT child → rotate to make it Case 3
                        node = node.parent
                        self.rotate_left(node)

                    # Case 3 – node is LEFT child → recolor + rotate right
                    node.parent.color        = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)

            else:                                          # parent is RIGHT child (mirror)
                uncle = node.parent.parent.left

                if uncle.color == RED:
                    # Case 1 mirror
                    node.parent.color         = BLACK
                    uncle.color               = BLACK
                    node.parent.parent.color  = RED
                    node = node.parent.parent

                else:
                    if node == node.parent.left:
                        # Case 2 mirror
                        node = node.parent
                        self.rotate_right(node)

                    # Case 3 mirror
                    node.parent.color        = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)

        self.root.color = BLACK    # root must always be BLACK

    # ── Search ─────────────────────────────────

    def search(self, data):
        """Return True if data is in the tree, False otherwise."""
        current = self.root
        while current != self.NIL:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    # ── Height ─────────────────────────────────

    def get_height(self):
        """Longest path from root to any leaf node."""
        return self._height(self.root)

    def _height(self, node):
        if node == self.NIL:
            return 0
        left_h  = self._height(node.left)
        right_h = self._height(node.right)
        return 1 + max(left_h, right_h)

    # ── Black Height ────────────────────────────

    def get_black_height(self):
        """
        Number of BLACK nodes on any path from root down to a leaf.
        (Does NOT count the root itself, but counts NIL as 1.)
        """
        return self._black_height(self.root)

    def _black_height(self, node):
        if node == self.NIL:
            return 1              # NIL nodes are BLACK
        left_bh = self._black_height(node.left)
        # only count current node if it is BLACK
        if node.color == BLACK:
            return left_bh + 1
        else:
            return left_bh

    # ── Size ────────────────────────────────────

    def get_size(self):
        return self.size


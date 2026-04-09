# creation **************************************************************************
def create_node(key):
    return {
        "key": key,
        "color": "RED",
        "left": None,
        "right": None,
        "parent": None
    }

def create_tree():
    NIL = {"color": "BLACK"}
    return {
        "root": NIL,
        "NIL": NIL
    }

# insertion and fixing **************************************************************************
def left_rotate(tree, x):
    NIL = tree["NIL"]
    y = x["right"]
    x["right"] = y["left"]

    if y["left"] != NIL:
        y["left"]["parent"] = x

    y["parent"] = x["parent"]

    if x["parent"] is None:
        tree["root"] = y
    elif x == x["parent"]["left"]:
        x["parent"]["left"] = y
    else:
        x["parent"]["right"] = y

    y["left"] = x
    x["parent"] = y

def right_rotate(tree, x):
    NIL = tree["NIL"]
    y = x["left"]
    x["left"] = y["right"]

    if y["right"] != NIL:
        y["right"]["parent"] = x

    y["parent"] = x["parent"]

    if x["parent"] is None:
        tree["root"] = y
    elif x == x["parent"]["right"]:
        x["parent"]["right"] = y
    else:
        x["parent"]["left"] = y

    y["right"] = x
    x["parent"] = y

def fix_insert(tree, k):
    NIL = tree["NIL"]

    while k["parent"] and k["parent"]["color"] == "RED":
        if k["parent"] == k["parent"]["parent"]["left"]:
            u = k["parent"]["parent"]["right"]  # uncle

            if u["color"] == "RED":
                # Case 1: recolor
                k["parent"]["color"] = "BLACK"
                u["color"] = "BLACK"
                k["parent"]["parent"]["color"] = "RED"
                k = k["parent"]["parent"]
            else:
                if k == k["parent"]["right"]:
                    # Case 2: left rotate
                    k = k["parent"]
                    left_rotate(tree, k)

                # Case 3: right rotate
                k["parent"]["color"] = "BLACK"
                k["parent"]["parent"]["color"] = "RED"
                right_rotate(tree, k["parent"]["parent"])
        else:
            u = k["parent"]["parent"]["left"]

            if u["color"] == "RED":
                k["parent"]["color"] = "BLACK"
                u["color"] = "BLACK"
                k["parent"]["parent"]["color"] = "RED"
                k = k["parent"]["parent"]
            else:
                if k == k["parent"]["left"]:
                    k = k["parent"]
                    right_rotate(tree, k)

                k["parent"]["color"] = "BLACK"
                k["parent"]["parent"]["color"] = "RED"
                left_rotate(tree, k["parent"]["parent"])

    tree["root"]["color"] = "BLACK"

def insert(tree, key):
    NIL = tree["NIL"]
    node = create_node(key)
    node["left"] = NIL
    node["right"] = NIL

    parent = None
    current = tree["root"]

    while current != NIL:
        parent = current
        if node["key"] < current["key"]:
            current = current["left"]
        else:
            current = current["right"]

    node["parent"] = parent

    if parent is None:
        tree["root"] = node
    elif node["key"] < parent["key"]:
        parent["left"] = node
    else:
        parent["right"] = node

    node["color"] = "RED"
    fix_insert(tree, node)

# array to tree **************************************************************************
def array_to_tree(arr):
    tree = create_tree()
    for key in arr:
        insert(tree, key)
    return tree

# print tree **************************************************************************     
def print_tree(tree):
    def inorder(node):
        if node != tree["NIL"]:
            inorder(node["left"])
            print(node["key"], end=" ")
            inorder(node["right"])
    inorder(tree["root"])

# search **************************************************************************     
def search(tree, key):
    NIL = tree["NIL"]
    current = tree["root"]
    while current != NIL and key != current["key"]:
        if key < current["key"]:
            current = current["left"]
        else:
            current = current["right"]
    return current

#print tree height **************************************************************************     
def print_tree_height(tree):
    def height(node):
        if node == tree["NIL"]:
            return 0
        return 1 + max(height(node["left"]), height(node["right"]))
    return height(tree["root"])

#print tree black height **************************************************************************     
def print_tree_black_height(tree):
    def black_height(node):
        if node == tree["NIL"]:
            return 0
        return 1 + black_height(node["left"])
    return black_height(tree["root"])

#print tree size **************************************************************************     
def print_tree_size(tree):
    def size(node):
        if node == tree["NIL"]:
            return 0
        return 1 + size(node["left"]) + size(node["right"])
    return size(tree["root"])

# test
arr = [10, 70, 30, 40, 20, 60, 50]
tree = array_to_tree(arr)
print_tree(tree)
print(print_tree_height(tree))
print(print_tree_black_height(tree))
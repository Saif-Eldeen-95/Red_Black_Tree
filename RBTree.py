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
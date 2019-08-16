def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


tree = binary_tree(1)
insert_left(tree, 2)
insert_left(tree, 5)
insert_right(tree, 3)
insert_right(tree, 6)
right_sub_tree = get_right_child(tree)
left_sub_tree = get_left_child(tree)
insert_left(right_sub_tree, 4)
insert_right(left_sub_tree, 7)
print(tree)

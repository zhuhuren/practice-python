class BinarySearchTree:
    def __init__(self):
        self.root = None
        if self.root:
            self.size = self.root.size
        else:
            self.size = 0

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, new_key, new_val):
        new_node = TreeNode(new_key, new_val)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            self._put(current_node, new_node)

    def _put(self, current_node, new_node):
        import operator
        current_key = current_node.key
        left = current_node.leftChild
        right = current_node.rightChild
        if new_node.key > current_key:
            if not right:
                current_node.rightChild = new_node
                current_node.rightChild.parent = current_node
                self._update_size(current_node.rightChild, operator.add)
            else:
                self._put(right, new_node)
        else:
            if not left:
                current_node.leftChild = new_node
                current_node.leftChild.parent = current_node
                self._update_size(current_node.leftChild, operator.add)
            else:
                self._put(left, new_node)

    def _update_size(self, node, oper):
        parent = node.parent
        if parent:
            if node.is_left_child():
                parent.sizeLeft = oper(parent.sizeLeft, 1)
            else:
                parent.sizeRight = oper(parent.sizeRight, 1)
            parent.size = parent.sizeLeft + parent.sizeRight
            self._update_size(parent, oper)
        self.size = self.root.size

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        return self._get(self.root, key).payload

    def _get(self, current_node, key):
        if key == current_node.key:
            result = current_node
        else:
            if key < current_node.key:
                if current_node.has_left_child():
                    result = self._get(current_node.leftChild, key)
                else:
                    result = None
            else:
                if current_node.has_right_child():
                    result = self._get(current_node.rightChild, key)
                else:
                    result = None
        return result

    def __getitem__(self, k):
        return self.get(k)

    def __str__(self):
        if self.root:
            return self._str(self.root, '', 0, 'Root', 0)
        else:
            return ''

    def _str(self, node, result, indent, side, level):
        line1 = indent * '-' + '{}{}: ({} : {}) \n'.format(side, level, node.key, node.payload)
        if node.has_right_child():
            line2 = self._str(node.rightChild, result, indent + 10, 'R', level + 1)
        else:
            line2 = ''
        if node.has_left_child():
            line3 = self._str(node.leftChild, result, indent + 10, 'L', level + 1)
        else:
            line3 = ''
        return line2 + line1 + line3

    def __contains__(self, key):
        return bool(self[key])

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(self.root, key)
            if node_to_remove:
                self.remove(node_to_remove)
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node_to_remove):
        import operator
        # decrease size by 1
        self._update_size(node_to_remove, operator.sub)

        parent_node = node_to_remove.parent
        if node_to_remove.is_leaf():
            if node_to_remove.is_left_child():
                parent_node.left_child = None
            else:
                parent_node.right_child = None
        elif node_to_remove.has_both_children():

        else: #has one child
            if node_to_remove.is_root():
                if node_to_remove.has_left_child():
                    self.root = node_to_remove.left_child
                else: # has right child
                    self.root = node_to_remove.right_child
                self.root.parent = None
                self._update_size(self.root, operator.sub)
            elif node_to_remove.is_left_child():
                if node_to_remove.has_left_child():
                    parent_node.left_child = node_to_remove.left_child
                else: #has right child
                    parent_node.left_child = node_to_remove.right_child
                parent_node.left_child.parent = parent_node
            else: #node_to_remove is right child
                if node_to_remove.has_left_child():
                    parent_node.right_child = node_to_remove.left_child
                else: #has right child
                    parent_node.right_child = node_to_remove.right_child
                parent_node.right_child.parent = parent_node

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        # number of nodes on left side
        self.sizeLeft = 0
        # number of nodes on right side
        self.sizeRight = 0
        # number of nodes in total
        self.size = self.sizeLeft + self.sizeRight

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.leftChild or self.rightChild)

    def has_any_children(self):
        return self.leftChild or self.rightChild

    def has_both_children(self):
        return self.leftChild and self.rightChild

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.has_left_child():
            self.leftChild.parent = self
        if self.has_right_child():
            self.rightChild.parent = self
    
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst[9] = 4
    bst[5] = 2
    bst[10] = 3
    bst[8] = 1
    bst[7] = 5
    bst[13] = 7
    bst[4] = 8
    bst[9.5] = 8
    bst[21] = 8
    bst[2.5] = 8
    bst[18] = 8
    bst[15] = 8
    bst[11] = 8
    bst[4] = 8
    bst[17] = 8
    bst[16] = 8
    bst[12] = 8
    bst[14] = 8
    print(bst)
    print(len(bst))
    print('9: ', bst[9])
    print('5: ', bst[5])
    print(bst.root.sizeRight)
    print('size: ', bst.size)
    print('sizeLeft: ', bst.root.sizeLeft)
    print('sizeRight: ', bst.root.sizeRight)
    print(bst.root.rightChild.sizeRight)
    print(len(bst))

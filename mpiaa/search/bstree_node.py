class BSTreeNode(object):
    """Binary search tree node (subtree)"""

    def __init__(self, item, key, left=None, right=None):
        """
        Tree node constructor.

        :param item: node's item
        :param key: item's key
        :param left (BSTreeNode): left child (subtree)
        :param right (BSTreeNode): right child (subtree)
        """
        self.item = item
        self.key = key
        self.left = left
        self.right = right
        self._size = 1

    def insert(self, item, key):
        """
        Assign item to this node if keys are equal.
        Else insert item into the corresponding subtree.
        If there is no corresponding subtree, create it.

        :param item: item to insert
        :param key: item's key
        """
        if self.key == key:
            self.item = item
        elif self.key < key:
            if self.right:
                self.right.insert(item, key)
            else:
                self.right = BSTreeNode(item, key)
        else:
            if self.left:
                self.left.insert(item, key)
            else:
                self.left = BSTreeNode(item, key)
        # Replace by correct code
        pass

    # def is_sub_tree_unique(self):
    #     if self.left:
    #         flag = self.left.find(self.key)
    #         flag_u = self.left.is_sub_tree_unique()
    #     else:
    #         flag = True
    #         flag_u = True
    #     if self.right:
    #         flag_2 = self.right.find(self.key)
    #         flag_u_2 = self.right.is_sub_tree_unique()
    #     else:
    #         flag_2 = True
    #         flag_u_2 = True
    #     if flag and flag_2 and flag_u and flag_u_2:
    #         return False
    #     else:
    #         return True


    def find(self, key):
        """
        Return node's item if keys are equal.
        Else search in the corresponding subtree and return result.
        Else, if there is no subtree, return None.

        :param key: key of the item to find
        :return: item or None
        """
        if self.key == key:
            return self.item
        elif key > self.key:
            if self.right:
                return self.right.find(key)
        else:
            if self.left:
                return self.left.find(key)
        # Replace by correct code

    def remove(self, key):
        """
        Return modified subtree with item with the key removed.
        :return: modified subtree or old subtree
        """
        if self.key == key:
            if self.left and self.right:
                tmp = self.right
                while tmp.left != None:
                    tmp = tmp.left
                self.item = tmp.item
                self.key = tmp.key
                tmp = tmp.remove(tmp.key)

            if not self.left and not self.right:
                return None
            elif not self.right:
                return self.left
            elif not self.left:
                return self.right
        else:
            if self.right:
                self.right = self.right.remove(key)
            else: return None
            if self.left:
                self.left = self.left.remove(key)
            else: return None
        pass




    def size(self):
        """
        Return number of items in the subtree.

        :return: number of items in the subtree
        """

        # Replace by correct code
        if self.right and self.left:
            return self.left.height() + self.right.height()
        elif not self.right:
            return self.left.size()
        elif not self.left:
            return self.right.size()
        else:
            return self._size

    def height(self):
        """
        Return height of the subtree.

        :return: height of the subtree
        """
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max([left_height, right_height])

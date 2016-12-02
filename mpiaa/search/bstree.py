from mpiaa.search.bstree_node import BSTreeNode

class BSTree(object):
    """Binary search tree"""

    def __init__(self):
        self.root = None
        self.elements = dict()

    def insert(self, item, key=None):
        """
        Insert item into the tree.

        :param item: item to insert
        :param key: item's key (item itself by default)
        """
        if key is None:
            key = item
        if self.root:
            self.root.insert(item, key)
        else:
            self.root = BSTreeNode(item, key)
        if self.elements.__contains__(key):
            self.elements[key] += 1
        else:
            self.elements[key] = 1

    def all_unique(self):
        for k, v in self.elements.items():
            if v > 1:
                return False
        return True

    def find(self, key):
        """
        Find item in the tree by key.

        :param key: key of the item to find
        :return: item or None if item isn't found
        """
        if self.root:
            return self.root.find(key)
        else:
            return None

    def remove(self, key):
        """
        Remove item from the tree by key.

        :param key: key of the item to remove
        """
        if self.root:
            self.root = self.root.remove(key)

    def size(self):
        """
        Get number of items in the tree.

        :return: number of items in the tree
        """
        if self.root:
            return self.root.size()
        else:
            return 0

    def height(self):
        """
        Get height of the tree

        :return: height of the tree
        """
        if self.root:
            return self.root.height()
        else:
            return 0






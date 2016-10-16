from mpiaa.search.bstree_node import BSTreeNode

class BSTree(object):
    """Binary search tree"""

    def __init__(self, get_key=lambda item: item):
        """
        Constructor

        :param get_key (f(item)): function to obtain key for each item
        """
        self.get_key = get_key
        self.root = None

    def insert(self, item):
        """
        Insert item into the tree

        :param item:
        :return:
        """
        if not self.root:
            self.root = BSTreeNode(item, self.get_key(item))
        else:
            self.root.insert(item, self.get_key(item))

    def find(self, key):
        """
        Find an item in the tree by key

        :param key: key of the item to find
        :return: item or None if item isn't found
        """
        if not self.root:
            return None
        else:
            return self.root.find(key)

    def remove(self, key):
        """
        Remove item from the tree by key

        :param key: key of the item to remove
        :return: nothing
        """
        if self.root:
            self.root = self.root.remove(key)


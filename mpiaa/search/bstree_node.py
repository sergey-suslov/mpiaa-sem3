class BSTreeNode(object):
    """Helper class for BSTree"""

    def __init__(self, item, key, left=None, right=None):
        """
        Tree node constructor

        :param item: node's item
        :param key: item's key
        :param left (BSTreeNode): left subtree
        :param right (BSTreeNode): right subtree
        """
        self.item = item
        self.key = key
        self.left = left
        self.right = right

    def insert(self, item, key):
        pass

    def find(self, key):
        pass

    def remove(self, key):
        pass

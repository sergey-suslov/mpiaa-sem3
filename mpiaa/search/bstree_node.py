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

    def insert(self, item, key):
        """
        Assign item to this node if keys are equal.
        Else insert item into the corresponding subtree (if present).

        :param item: item to insert
        :param key: item's key
        """
        # Replace by correct code
        pass

    def find(self, key):
        """
        Return node's item if keys are equal.
        Else search in the corresponding subtree and return result.
        Else, if there is no subtree, return None.

        :param key: key of the item to find
        :return: item or None
        """
        # Replace by correct code
        return None

    def remove(self, key):
        """
        Return modified subtree with item with the key removed.

        :param key: key of the item to remove
        :return: modified subtree or old subtree
        """
        # Replace by correct code
        return self

    def size(self):
        """
        Return number of items in the subtree.

        :return: number of items in the subtree
        """
        # Replace by correct code
        return 1

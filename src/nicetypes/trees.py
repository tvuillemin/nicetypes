class _Node:

    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        if not isinstance(value, type(self)):
            raise TypeError("A node child can only be another node.")
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        if not isinstance(value, type(self)):
            raise TypeError("A node child can only be another node.")
        self._right = value

    @property
    def data(self):
        return self._data


class SortedNumbersTree:  # pylint: disable=too-few-public-methods

    def __init__(self, root_number):
        self._root = _Node(root_number)

    def insert(self, number):
        current_node = self._root
        insertion_done = False
        while not insertion_done:
            if number < current_node.data:
                if current_node.left is None:
                    current_node.left = _Node(number)
                    insertion_done = True
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = _Node(number)
                    insertion_done = True
                else:
                    current_node = current_node.right

# pylint: disable=protected-access
from unittest import TestCase

from nicetypes.trees import SortedNumbersTree, _Node


class TestNode(TestCase):

    def test_invalid_left(self):
        # Given
        node = _Node(100)
        # When
        with self.assertRaises(TypeError) as context:
            node.left = "not_a_node"
        # Then
        self.assertEqual(
            str(context.exception),
            "A node child can only be another node."
        )

    def test_invalid_right(self):
        # Given
        node = _Node(100)
        # When
        with self.assertRaises(TypeError) as context:
            node.right = "not_a_node"
        # Then
        self.assertEqual(
            str(context.exception),
            "A node child can only be another node."
        )


class TestSortedNumbersTree(TestCase):

    def test_init_tree(self):
        # Given
        root_value = 100
        # When
        tree = SortedNumbersTree(root_value)
        # Then
        self.assertIsInstance(tree._root, _Node)
        self.assertEqual(tree._root._data, 100)
        self.assertIsNone(tree._root.left)
        self.assertIsNone(tree._root.right)

    def test_insert_lower_than_root(self):
        # Given
        tree = SortedNumbersTree(100)
        # When
        tree.insert(50)
        # Then
        self.assertIsInstance(tree._root.left, _Node)
        self.assertEqual(tree._root.left.data, 50)
        self.assertIsNone(tree._root.left.left)
        self.assertIsNone(tree._root.left.right)

    def test_insert_greater_than_root(self):
        # Given
        tree = SortedNumbersTree(100)
        # When
        tree.insert(200)
        # Then
        self.assertIsInstance(tree._root.right, _Node)
        self.assertEqual(tree._root.right.data, 200)
        self.assertIsNone(tree._root.right.left)
        self.assertIsNone(tree._root.right.right)

    def test_insert_several_levels(self):
        # Given
        tree = SortedNumbersTree(100)
        # When
        tree.insert(200)
        tree.insert(150)
        tree.insert(50)
        tree.insert(75)
        # Then
        self.assertEqual(tree._root.left.data, 50)
        self.assertEqual(tree._root.left.right.data, 75)
        self.assertEqual(tree._root.data, 100)
        self.assertEqual(tree._root.right.left.data, 150)
        self.assertEqual(tree._root.right.data, 200)

from unittest import TestCase

from nicetypes.lists import UniqList

class TestUniqList(TestCase):

    def test_uniqlist_init_without_arg(self):
        # When
        unq = UniqList()

        # Then
        self.assertListEqual(unq, [])

    def test_uniqlist_init_with_tuple(self):
        # Given
        data = (1, 2, 3, 3, 4, 1)

        # When
        unq = UniqList(data)

        # Then
        self.assertListEqual(unq, [1, 2, 3, 4])

    def test_uniqlist_init_with_list(self):
        # Given
        data = [1, 2, 3, 3, 4, 1]

        # When
        unq = UniqList(data)

        # Then
        self.assertListEqual(unq, [1, 2, 3, 4])

    def test_uniqlist_init_with_generator(self):
        # Given
        data = (i for i in range(1, 5))

        # When
        unq = UniqList(data)

        # Then
        self.assertListEqual(unq, [1, 2, 3, 4])

    def test_uniqlist_append(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.append(1)
        unq.append(5)

        # Then
        self.assertListEqual(unq, [1, 2, 3, 4, 5])

    def test_uniqlist_insert_replace_false(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.insert(0, 3)
        unq.insert(0, 0)

        # Then
        self.assertListEqual(unq, [0, 1, 2, 3, 4])

    def test_uniqlist_insert_replace_true(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.insert(0, 3, replace=True)
        unq.insert(0, 0, replace=True)

        # Then
        self.assertListEqual(unq, [0, 3, 1, 2, 4])

    def test_uniqlist_extend(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.extend([4, 5, 6])

        # Then
        self.assertListEqual(unq, [1, 2, 3, 4, 5, 6])

    def test_uniqlist_add_uniqlist(self):
        # Given
        unq1 = UniqList([1, 2, 3, 4])
        unq2 = UniqList([4, 5, 6])

        # When
        concat = unq1 + unq2

        # Then
        self.assertListEqual(concat, [1, 2, 3, 4, 5, 6])

    def test_uniqlist_add_tuple(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        concat = unq + (4, 5, 5, 5, 6)

        # Then
        self.assertListEqual(concat, [1, 2, 3, 4, 5, 6])

    def test_uniqlist_add_list(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        concat = unq + [4, 5, 5, 5, 6]

        # Then
        self.assertListEqual(concat, [1, 2, 3, 4, 5, 6])

    def test_uniqlist_add_generator(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        concat = unq + (i for i in range(4, 7))

        # Then
        self.assertListEqual(concat, [1, 2, 3, 4, 5, 6])

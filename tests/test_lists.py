from nose.tools import assert_list_equal

from nicetypes.lists import UniqList

class TestUniqList:

    def test_uniqlist_init(self):
        # Given
        data = [1, 2, 3, 3, 4]

        # When
        unq = UniqList(data)

        # Then
        assert_list_equal(unq, [1, 2, 3, 4])

    def test_uniqlist_append(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.append(1)
        unq.append(5)

        # Then
        assert_list_equal(unq, [1, 2, 3, 4, 5])

    def test_uniqlist_insert_replace_false(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.insert(0, 3)
        unq.insert(0, 0)

        # Then
        assert_list_equal(unq, [0, 1, 2, 3, 4])

    def test_uniqlist_insert_replace_true(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.insert(0, 3, replace=True)
        unq.insert(0, 0, replace=True)

        # Then
        assert_list_equal(unq, [0, 3, 1, 2, 4])

    def test_uniqlist_extend(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        unq.extend([4, 5, 6])

        # Then
        assert_list_equal(unq, [1, 2, 3, 4, 5, 6])

    def test_uniqlist_add_uniqlist(self):
        # Given
        unq1 = UniqList([1, 2, 3, 4])
        unq2 = UniqList([4, 5, 6])

        # When
        concat = unq1 + unq2

        # Then
        assert_list_equal(concat, [1, 2, 3, 4, 5, 6])

    def test_uniqlist_add_list(self):
        # Given
        unq = UniqList([1, 2, 3, 4])

        # When
        concat = unq + [4, 5, 5, 5, 6]

        # Then
        assert_list_equal(concat, [1, 2, 3, 4, 5, 6])

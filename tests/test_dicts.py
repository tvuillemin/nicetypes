from unittest import TestCase

from nicetypes.dicts import ImmutableDict


class TestImmutableDict(TestCase):

    def test_immutabledict_init(self):
        # Given
        data = {"foo": 1}
        # When
        imd = ImmutableDict(data)
        # Then
        self.assertDictEqual(data, imd._inner_dict)  # pylint: disable=protected-access

    def test_immutabledict_getitem(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        value = imd["foo"]
        # Then
        self.assertEqual(value, 1)

    def test_immutabledict_str(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        imd_str = str(imd)
        # Then
        self.assertEqual(imd_str, "ImmutableDict({'foo': 1})")

    def test_immutabledict_len(self):
        # Given
        imd = ImmutableDict({"foo": 1, "bar": 2})
        # When
        imd_len = len(imd)
        # Then
        self.assertEqual(imd_len, 2)

    def test_immutabledict_get(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        value = imd.get("foo")
        # Then
        self.assertEqual(value, 1)

    def test_immutabledict_items(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        items = tuple(imd.items())
        # Then
        self.assertSequenceEqual(items, [("foo", 1)])

    def test_immutabledict_keys(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        keys = tuple(imd.keys())
        # Then
        self.assertSequenceEqual(keys, ["foo"])

    def test_immutabledict_values(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        values = tuple(imd.values())
        # Then
        self.assertSequenceEqual(values, [1])

    def test_immutabledict_hashable(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        hash_ = hash(imd)
        # Then
        self.assertIsInstance(hash_, int)

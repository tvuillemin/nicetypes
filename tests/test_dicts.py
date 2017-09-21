from unittest import TestCase

from nicetypes.dicts import _DictWrapper, ImmutableDict, TypedDict, validate_dict


class TestValidateDict(TestCase):

    def test_invalid_dict(self):
        # Given
        data = "not_a_dict"
        # When
        with self.assertRaises(TypeError) as context:
            validate_dict(data)
        # Then
        self.assertEqual(
            str(context.exception),
            "Expected a dict as argument, got a <class 'str'> instead."
        )


class TestDictWrapper(TestCase):

    def test_dictwrapper_init(self):
        # Given
        data = {"foo": 1}
        # When
        dwp = _DictWrapper(data)
        # Then
        self.assertDictEqual(data, dwp._inner_dict)  # pylint: disable=protected-access

    def test_dictwrapper_getitem(self):
        # Given
        dwp = _DictWrapper({"foo": 1})
        # When
        value = dwp["foo"]
        # Then
        self.assertEqual(value, 1)

    def test_dictwrapper_str(self):
        # Given
        dwp = _DictWrapper({"foo": 1})
        # When
        dwp_str = str(dwp)
        # Then
        self.assertEqual(dwp_str, "_DictWrapper({'foo': 1})")

    def test_dictwrapper_len(self):
        # Given
        dwp = _DictWrapper({"foo": 1, "bar": 2})
        # When
        dwp_len = len(dwp)
        # Then
        self.assertEqual(dwp_len, 2)

    def test_dictwrapper_get(self):
        # Given
        dwp = _DictWrapper({"foo": 1})
        # When
        value = dwp.get("foo")
        # Then
        self.assertEqual(value, 1)

    def test_dictwrapper_items(self):
        # Given
        dwp = _DictWrapper({"foo": 1})
        # When
        items = tuple(dwp.items())
        # Then
        self.assertSequenceEqual(items, [("foo", 1)])

    def test_dictwrapper_keys(self):
        # Given
        dwp = _DictWrapper({"foo": 1})
        # When
        keys = tuple(dwp.keys())
        # Then
        self.assertSequenceEqual(keys, ["foo"])

    def test_dictwrapper_values(self):
        # Given
        dwp = _DictWrapper({"foo": 1})
        # When
        values = tuple(dwp.values())
        # Then
        self.assertSequenceEqual(values, [1])


class TestImmutableDict(TestCase):

    def test_immutabledict_hashable(self):
        # Given
        imd = ImmutableDict({"foo": 1})
        # When
        hash_ = hash(imd)
        # Then
        self.assertIsInstance(hash_, int)


class TestTypedDict(TestCase):

    def test_typeddict_valid_key(self):
        # Given
        tpd = TypedDict(key_type=str)
        # When
        tpd["one"] = 1
        # Then
        self.assertEqual(tpd["one"], 1)

    def test_typeddict_invalid_key(self):
        # Given
        tpd = TypedDict(key_type=str)
        # When
        with self.assertRaises(TypeError) as context:
            tpd[1] = 1
        # Then
        self.assertEqual(
            str(context.exception),
            "Expected a <class 'str'> as key, got a <class 'int'> instead."
        )

    def test_typeddict_valid_value(self):
        # Given
        tpd = TypedDict(value_type=float)
        # When
        tpd["one"] = 1.0
        # Then
        self.assertEqual(tpd["one"], 1.0)

    def test_typeddict_invalid_value(self):
        # Given
        tpd = TypedDict(value_type=float)
        # When
        with self.assertRaises(TypeError) as context:
            tpd["one"] = 1
        # Then
        self.assertEqual(
            str(context.exception),
            "Expected a <class 'float'> as value, got a <class 'int'> instead."
        )

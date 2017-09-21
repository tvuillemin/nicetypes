from copy import deepcopy


def validate_dict(dictionnary):
    if not isinstance(dictionnary, dict):
        raise TypeError("Expected a dict as argument, got a %s instead." % type(dictionnary))


class _DictWrapper:

    def __init__(self, dictionnary):
        validate_dict(dictionnary)
        self._inner_dict = deepcopy(dictionnary)

    def __getitem__(self, key):
        return self._inner_dict[key]

    def __len__(self):
        return len(self._inner_dict)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, str(self._inner_dict))

    def get(self, key):
        return self._inner_dict.get(key)

    def items(self):
        return self._inner_dict.items()

    def keys(self):
        return self._inner_dict.keys()

    def values(self):
        return self._inner_dict.values()


class ImmutableDict(_DictWrapper):

    def __init__(self, dictionnary):
        super().__init__(dictionnary)
        self._hash = None

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(tuple(sorted(self._inner_dict.items())))
        return self._hash


FrozenDict = ImmutableDict


class TypedDict(_DictWrapper):

    def __init__(self, key_type=None, value_type=None, copy_from=None):
        dictionnary = copy_from if copy_from else {}
        super().__init__(dictionnary)
        self._key_type = key_type
        self._value_type = value_type

    def __setitem__(self, key, value):
        self.validate_key(key)
        self.validate_value(value)
        self._inner_dict[key] = value

    def validate_key(self, key):
        if self._key_type and not isinstance(key, self._key_type):
            raise TypeError("Expected a %s as key, got a %s instead." %
                            (self._key_type, type(key)))

    def validate_value(self, value):
        if self._value_type and not isinstance(value, self._value_type):
            raise TypeError("Expected a %s as value, got a %s instead." %
                            (self._value_type, type(value)))

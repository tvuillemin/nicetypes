from copy import deepcopy


class ImmutableDict:

    def __init__(self, dictionnary):
        self._hash = None
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

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(tuple(sorted(self._inner_dict.items())))
        return self._hash

FrozenDict = ImmutableDict

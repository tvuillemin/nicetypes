class UniqList:
    """A list-like object that makes sure there is no double in the list.

    When you try to add an element that is already present, UniqList ignores it silently.
    You can view it as a kind of "ordered set", which removes doubles but preserves order.
    An already present element will be prefered over a new one, unless specified otherwise.
    """

    def __init__(self, ordered_iterable=()):
        """Constructor

        _elements_set is a internal set that contains every element in the UniqList.
        This set is used for search operations, because those operations are much
        faster on a set than on a list (complexity O(1) vs O(n)).
        """
        self._elements_list = list()
        self._elements_set = set()
        for element in ordered_iterable:
            self.append(element)

    def __getitem__(self, index):
        return self._elements_list[index]

    def __iter__(self):
        return iter(self._elements_list)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, str(self._elements_list))

    def append(self, element):
        if element not in self._elements_set:
            self._elements_list.append(element)
            self._elements_set.add(element)

    def insert(self, index, element, replace=False):
        if element not in self._elements_set:
            self._elements_list.insert(index, element)
            self._elements_set.add(element)
        elif replace:
            self._elements_list.remove(element)
            self._elements_list.insert(index, element)
        else:  # element already exists but replace is False
            pass

    def extend(self, other):
        for element in other:
            self.append(element)

    def __add__(self, other):
        new_uniq_list = UniqList(self)
        for element in other:
            new_uniq_list.append(element)
        return new_uniq_list

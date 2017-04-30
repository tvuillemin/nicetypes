class UniqList(list):
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
        list.__init__(self)
        self._elements_set = set()
        for element in ordered_iterable:
            self.append(element)

    def append(self, element):
        if element not in self._elements_set:
            list.append(self, element)
            self._elements_set.add(element)

    def insert(self, index, element, replace=False):
        if element not in self._elements_set:
            list.insert(self, index, element)
            self._elements_set.add(element)
        elif replace:
            self.remove(element)
            list.insert(self, index, element)
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

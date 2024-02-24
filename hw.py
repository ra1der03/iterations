class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count1 = 0
        self.count2 = -1
        return self

    def __next__(self):
        if self.count1 < len(self.list_of_list):
            if self.count2 < len(self.list_of_list[self.count1])-1:
                self.count2 += 1
                return self.list_of_list[self.count1][self.count2]
            else:
                self.count1 += 1
                self.count2 = 0
                if self.count1 == len(self.list_of_list):
                    raise StopIteration
                return self.list_of_list[self.count1][self.count2]



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item, [flat_iterator_item, check_item]

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None],\
        [list(FlatIterator(list_of_lists_1))[0:-1]]


if __name__ == '__main__':
    test_1()
import doctest

# Add two numbers
class AddTwoNums:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def addTwoNums(self):

        """Reverse two input lists, add them together and return the value as a reversed list.

        :param l1, l2: Two input lists
        :return: Sum of the two reversed lists as a reversed list

        >>> AddTwoNums([3, 6, 2, 5, 5], [4, 5, 3]).addTwoNums()
        [7, 1, 6, 5, 5]

        """

        tmp = str(int(''.join([*map(str, self.l1[::-1])])) + int(''.join([*map(str, self.l2[::-1])])))
        return [int(s) for s in tmp[::-1]]


#l1 = [2, 4, 3]
#l2 = [5, 6, 4]

#l1 = [4, 5, 2, 1]
#l2 = [3, 6, 2, 5, 5]

l1 = [3, 6, 2, 5, 5]
l2 = [4, 5, 3]

#l1 = [9,9,9,9,9,9,9]
#l2 = [9,9,9,9]

AddTwoNums(l1, l2).addTwoNums()

doctest.testmod()

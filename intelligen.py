# Question 1

class Case:
    def __init__(self, arr1, arr2, arr3):
        self.arr1 = arr1
        self.arr2 = arr2
        self.arr3 = arr3

    def getIntersection(self):

        intersection = set()

        for i in self.arr1:
            if (i in self.arr2) or (i in self.arr3):
                intersection.add(i)

        for i in self.arr2:
            if (i in self.arr1) or (i in self.arr3):
                intersection.add(i)

        for i in self.arr3:
            if (i in self.arr1) or (i in self.arr2):
                intersection.add(i)             

        return list(intersection)
        

## Test 1 
arr1 = [1, 4, 5, 6, 7]
arr2 = [2, 4, 5, 9, 11]
arr3 = [1, 3, 5, 8]

case = Case(arr1, arr2, arr3)
case.getIntersection()

# Question 2
class Case:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def getUnion(self):

        union = set()

        for i in self.arr1:
            union.add(i)

        for i in self.arr2:
            union.add(i)

        return list(union)


## Test 1 
arr1 = [1, 4, 5, 6, 7]
arr2 = [2, 3, 4, 5, 9, 11]

case = Case(arr1, arr2)
case.getUnion()


# Question 3
class Case:
    def __init__(self, string):
        self.string = str(string)

    def checkIfPalindrome(self):

        if self.string == self.string[::-1]:
            return 'Palindrome'
        
        return 'Not palindrome'

## Test 1
string = 'myname'
case = Case(string)
case.checkIfPalindrome()

## Test 2
string = 'lokkol'
Case(string).checkIfPalindrome()


# Question 4
### NOT SOLVED
class Case:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2


    def getLongest(self):

        tmpstr = []
        #tmpstraddr = len(string1) if len(string1)>len(string2) else len(string2)
        tmpstraddr = 

        for idx, i in enumerate(self.string1):
            if i in self.string2:
                i.append(tmpstr)
                tmpstraddr = i


# Question 5
class Case:
    def __init__(self, k):
        self.k = k

    def getN(self):

        # Get prime number lower closest to k
        ## 1 :: Check if num is prime
        ## Reduce 1
        ## Repeat 1

        if self.k > 1:
            if divmod((self.k-1), self.k)[1] != 0:
                self.k -= self.k - 1
                getN()


        # Get prime number higher closes to k


def getN(k):
    if k>1:
        if divmod((k-1), k)[1] != 0:
            k = k-1
            getN(k)

from leetcode import AddTwoNums

def test_addTwoNums():

    t1l1 = [2, 4, 3]
    t1l2 = [5, 6, 4]
    
    t2l1 = [4, 5, 2, 1]
    t2l2 = [3, 6, 2, 5, 5]

    t3l1 = [3, 6, 2, 5, 5]
    t3l2 = [4, 5, 3]

    test1 = AddTwoNums(t1l1, t1l2)
    test2 = AddTwoNums(t2l1, t2l2)
    test3 = AddTwoNums(t3l1, t3l2)

    assert test1.addTwoNums() == [7, 0, 8]
    assert test2.addTwoNums() == [7, 1, 5, 6, 5]
    assert test3.addTwoNums() == [7, 1, 6, 5, 5]

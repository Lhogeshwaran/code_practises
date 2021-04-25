
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))



arr = [7, 2, 1, 4, 3, 5, 8, 9]
arr = sorted(arr)

def split_arrays(arr):
    # Write your code here
    
    arr = sorted(arr)
    left_arr = [arr[0]]
    arr.pop(0)
    max_check = 0

    while sum(left_arr) < sum(arr):
        left_arr.append(arr.pop(0))
        max_check += 1
    
    return max_check

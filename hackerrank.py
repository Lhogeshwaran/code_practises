# Sales by Match
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    
    pairs = 0
    
    for i in set(ar):
        pairs += divmod(ar.count(i), 2)[0]
    
    return pairs

# Counting Valleys
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


def countingValleys(steps, path):

    altitude = 0
    invalley = False
    valleycount = 0

    for i in path:

        if altitude < 0:
            invalley = True
        
        if i=='D':
            altitude -= 1
        else:
            altitude += 1

        if (invalley==True) & (altitude==0):
            invalley = False
            valleycount += 1
        
    return valleycount


# Jumping on the Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

## My solution
def jumpingOnClouds(c):
    
    track = 0
    jumps = 0
    
    while track < len(c)-2:
        if (c[track]==0) & (c[track+2]==0):
            jumps += 1
            track += 2
        elif c[track]==0:
            jumps += 1
            track += 1
        else:
            track += 1
     
    if c[-2]==0:
        jumps += 1

    return jumps


## Best solution
def jumpingOnClouds(c):

    if len(c) == 1: 
        return 0
    if len(c) == 2: 
        return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])


## My first recursion function
def getFact(n):

    return n * getFact(n-1) if n > 0 else 1 

getFact(10)


# Repeated String
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

def repeatedString(s, n):

    size = len(s)
    reps = s.count('a')
    occ = (divmod(n, size)[0]) * reps
    
    if divmod(n, size)[1] > 0:
        sample = s[:divmod(n, size)[1]]
        occ += sample.count('a')
    
    return occ


# Hour glass
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def hourglassSum(arr):
    
    sum = set()
    
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.add(arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
                    arr[i+1][j+1] + 
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
    return max(sum)


def solve(meal_cost, tip_percent, tax_percent):
    
    tip = (tip_percent/100) * meal_cost
    tax = (tax_percent/100) * meal_cost

    total = int(round((meal_cost + tip + tax), 0))

    print(total)

solve(13.00, 20, 8)


def wierdCheck(N):
    
    if (N%2 != 0) or ((N%2 == 0) & (N in range(6, 21))):
        return 'Weird'
    
    return 'Not Weird'

N = 2503243243244325543500
%timeit wierdCheck(2503243243244325543500)


class Case:
    def __init__(self, arr):
        self.arr = arr
        
    def printReverse(self):
        print(*self.arr[::-1])

Case(arr).printReverse()


# Binary Numbers
n = int(input())
ans = max(bin(n)[2:].split('0')).count('1')
print(ans)


# Rotate arrays
d = 4
a = [1, 2, 3, 4, 5]

def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a

rotLeft(a, d)

# Bribes
bribes = 0
for idx, i in enumerate(q):
    if i-idx > :
        print('Too chaotic.')
    elif i-idx==1 or i-idx==2:
        bribes += 1

def minimumBribes(q):

    chaoticTrue = 0
    bribes = 0
    
    for idx, i in enumerate(q, start=1):
        if i-idx > 2:
            chaoticTrue = 1
            break
        elif (i!=idx) & (i>idx):
            bribes += i-idx
            
    if chaoticTrue!=1:
        print(bribes)
    else:
        print('Too chaotic')

## UNDERSTAND THIS AGAIN
def minimumBribes(Q):

    moves = 0

    for idx, i in enumerate(Q, 1):

        if i - idx > 2:
            print("Too chaotic")
            return

        for j in range(max(i-2, 0), idx):


            if Q[j] > i:
                moves += 1

    print(moves)

Q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(Q)

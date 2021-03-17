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

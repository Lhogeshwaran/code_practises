# ROUND A
# Allocation (5pts, 7pts)

class Case:
    def __init__(self, for_sale, budget, cost):
        self.for_sale = for_sale
        self.budget = budget
        self.cost = cost
        
    def buyHouse(self):
        self.cost = (s for s in sorted(self.cost) if s<=self.budget)
        can_buy = 0
        
        for i in self.cost:
            if self.budget - i >= 0:
                self.budget -= i
                can_buy += 1
            else:
                break
            
        return can_buy
            

t = int(input())
for i in range(1, t+1):
    for_sale, budget = [int(s) for s in input().split(" ")]
    cost = [int(s) for s in input().split(" ")]
    case = Case(for_sale, budget, cost)
    print(f'Case #{i}: {case.buyHouse()}')


# ROUND B
# Bike Tour (5pts, 7pts)

class Case:
    def __init__(self, checkpoints, heights):
        self.checkpoints = checkpoints
        self.heights = heights
        
    def countPeaks(self):
        peaks = 0
        
        for idx, i in enumerate(self.heights):
            if (idx>0) & (idx<self.checkpoints-1):
                if (i>self.heights[idx-1]) and (i>self.heights[idx+1]):
                    peaks += 1
        
        return peaks
        

t = int(input())
for i in range(1, t+1):
    checkpoints = int(input())
    heights = [int(s) for s in input().split(" ")]
    case = Case(checkpoints, heights)
    print(f'Case #{i}: {case.countPeaks()}')

# ROUND C
# Countdown (5pts, 7pts)
### DO NOT USE CLASS. Function from 2020_old works without Runtime error.

class Case:
    def __init__(self, mcount, arr):
        self.mcount = mcount
        self.arr = arr
    
    def getMcount(self):

        countdowns = 0
        
        for idx, i in enumerate(self.arr):
            if (i==self.mcount) and (idx+self.mcount-1<len(self.arr)) & (self.arr[idx+self.mcount-1]==1):
                tmparr = self.arr[idx:idx+self.mcount]
                tmpmcount = 0
                        
                for jdx, j in enumerate(tmparr):
                    if j + jdx == self.mcount:
                        tmpmcount +=1 
                    else:
                        break

                if tmpmcount == self.mcount:
                    countdowns += 1
                    tmpmcount = 0
                
        return countdowns


t = int(input())
for i in range(1, t+1):
    arrlen, mcount = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    case = Case(mcount, arr)
    print(f'Case #{i}: {case.getMcount()}')

# ROUND D
# Record Breaker (4pts, 8pts)

class Case:
    def __init__(self, days, visitors):
        self.days = days
        self.visitors = visitors
        
    def checkPeak(self):
        peakdays = 0
        if self.visitors[0]==self.visitors[1]:
            maxvis = self.visitors[0]
        else:
            maxvis = self.visitors[0]-1
        
        for idx, i in enumerate(self.visitors):
            if (idx<(self.days-1)):
                if (i>maxvis) & (i>self.visitors[idx+1]):
                    maxvis = i
                    peakdays += 1
                    
            elif (i>maxvis):
                peakdays += 1
        
        return peakdays


t = int(input())
for k in range(1, t+1):
    days = int(input())
    visitors = [int(s) for s in input().split(" ")]
    case = Case(days, visitors)
    print(f'Case #{k}: {case.checkPeak()}')

# ROUND E
# Longest Arithmetic (4pts, 7pts)

class Case:
    def __init__(self, length, arr):
        self.length = length
        self.arr = arr
    
    def longestArr(self):
        tmparr = [self.arr[0], self.arr[1]]
        longestarr = 2

        for idx, i in enumerate(self.arr):
            if (idx>1):
                if tmparr[-1]-i == tmparr[-2]-tmparr[-1]:
                    tmparr.append(i)
                    if longestarr < len(tmparr):
                        longestarr = len(tmparr)
                else:
                    tmparr = [self.arr[idx-1], i] 
        
        return longestarr
            

T = int(input())
for t in range(1, T+1):
    length = int(input())
    arr = [int(s) for s in input().split(" ")]
    case = Case(length, arr)
    print(f'Case #{t}: {case.longestArr()}')

# Round F
# ATM Queue (4pts, 7pts)

class Case:
    def __init__(self, people, maxamt, amounts):
        self.people = people
        self.maxamt = maxamt
        self.amounts = amounts

    def getOrder(self):
        
        order = {}
        
        for idx, i in enumerate(self.amounts):
            if divmod(i, self.maxamt)[1]>0:
                order[idx+1] = divmod(i, self.maxamt)[0] + 1
            else:
                order[idx+1] = divmod(i, self.maxamt)[0]
        
        order = {k:v for k, v in sorted(order.items(), key=lambda item: item[1])}
        order = [s for s in order.keys()]
        order = ' '.join(str(i) for i in order)
        return order


T = int(input())
for t in range(1, T+1):
    people, maxamt = [int(s) for s in input().split(" ")]
    amounts = [int(s) for s in input().split(" ")]
    case = Case(people, maxamt, amounts)
    print(f'Case #{t}: {case.getOrder()}')

# Round G
# Kick_Start (4pts, 7pts)

class Case:
    def __init__(self, string):
        self.string = string
    
    def luckyStrings(self):
        kicks = 0
        luckystrings = 0
        
        for idx, i in enumerate(self.string):
            if (i=='K') & (idx<len(self.string)-3):
                if (self.string[idx+1]=='I') & (self.string[idx+2]=='C') & (self.string[idx+3]=='K'):
                    kicks += 1
            elif (i=='S') & (idx<len(self.string)-4):
                if (self.string[idx+1]=='T') & (self.string[idx+2]=='A') & (self.string[idx+3]=='R') & (self.string[idx+4]=='T'):
                    luckystrings += kicks

        return luckystrings


T = int(input())
for t in range(1, T+1):
    string = str(input())
    case = Case(string)
    print(f'Case #{t}: {case.luckyStrings()}')

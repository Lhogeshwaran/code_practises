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

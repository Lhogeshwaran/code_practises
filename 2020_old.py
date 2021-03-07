# ROUND A

# Allocation (5pts, 7pts)

def buyHouse(N, B, ls):

    ls = (s for s in sorted(ls) if s <= B)
    ans = 0

    for i in ls:
        if B - i >= 0 :
            B = B - i
            ans += 1

    return ans

# INCOMPLETE # Plates (9pts, 15pts) 

def getPlates(N, K, P, ls):
    
    max_val = 0
    
    for i, j in zip(reversed(range(0, P+1)), range(0, P+1)):
        #if max_val < (sum(ls[0][:i]) + sum(ls[1][:j])):
            print(i, j, (sum(ls[0][:i]) + sum(ls[1][:j])))
    
    return max_val


# ROUND B

# Bike Tour (5pts, 7pts)

def findPeaks(ls, n):
    
    peak = 0

    for i in range(1, n-1):
        if ls[i] > ls[i-1] and ls[i] > ls[i+1]:
            peak += 1
  
    return peak

# Bus routes (10pts, 13pts)

def leastDays(ls, N, D):

  for i in reversed(range(0, N)):
    D = D - (D % ls[i])

  return D


# ROUND C

# Allocation (5pts, 7pts) -- SOLVED

def cntDwn(ls, K):

    cnt = 0

    for idx, i in enumerate(ls):
        if (i == K) and (idx + K - 1 < len(ls)) and (ls[idx+K-1]==1):
            tmp_ls = ls[idx:idx+K]
            tmp_cnt = 0

            for jdx, j in enumerate(tmp_ls):
                if j + jdx == K:
                    tmp_cnt +=1 
                else:
                    break

            if tmp_cnt == K:
                cnt += 1
                tmp_cnt = 0

    return cnt
    
T = int(input())

for i in range(1, T+1):
    N, K = [int(s) for s in input().split(' ')]
    ls = [int(s) for s in input().split(' ')]
    print('Case #{}: {}'.format(i, cntDwn(ls, K)))


# ROUND D

# Record Breaker (5pts, 7pts) -- WORK IN PROGRESS

lsstr = '4 8 15 16 23 42'
ls = [int(x) for x in lsstr.split(' ')]


def recBrk(ls):

    tmp = 0
    cnt = 0

    for idx, i in enumerate(ls):

        if (idx < len(ls)-1):
            if (i > tmp) & (i > ls[idx+1]):
                cnt +=  1
                tmp = i

        if (idx == len(ls)-1) & (i > tmp) & (i > ls[idx-1]):
            cnt += 1

    return cnt


T = int(input())

for i in range(1, T+1):
    N = int(input())
    ls = [int(s) for s in input().split(' ')]
    print('Case #{}: {}'.format(i, recBrk(ls)))

t = int(input())

x = []

for i in range(1,4):
    x.append(t*i)

print(*x)


days_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
t = int(input())
print(days_dict[t])





data = {'product':['base_1', 'base_2', 'rider_1', 'rider_2', 'rider_3', 'rider_4', 'rider_5'], 
        'customer_id':[1, 2, 1, 2, 2, 2, 2], 
        'premium':[29.49, 90.74, 83.75, 83.80, 10.00, 20.00, 30.00]}
df = pd.DataFrame.from_dict(data)


def grp_pdt(x):

    if x in ['rider_3', 'rider_4', 'rider_5']:
        return 'rider_other'
    
    return x


df['product'] = df['product'].apply(grp_pdt)
df.groupby(['product', 'customer_id'])['premium'].sum()

import pandas as pd
data = {'product':['base_1', 'base_2', 'rider_1', 'rider_2', 'rider_3', 'rider_4', 'rider_5'], 'customer_id':[1, 2, 1, 2, 2, 2, 2], 'premium':[29.49, 90.74, 83.75, 83.80, 10.00, 20.00, 30.00]}
df = pd.DataFrame.from_dict(data)


def grp_pdt(x):
    if x in ['rider_3', 'rider_4', 'rider_5']:
        return 'rider_other'
    
    return x


df['product'] = df['product'].apply(grp_pdt)
df = pd.DataFrame(df.groupby(['product', 'customer_id'])['premium'].sum()).reset_index()
df


def collapse(df, columns_list, ls, alias):

    if (type(columns_list) == str) | (type(columns_list) == list):
        pass
    else: 
        raise TypeError('columns_list must be type list or str.')

    if type(columns_list) == str:
        col_ls = []
        col_ls.append(columns_list)

    else:
        col_ls = columns_list
    
    tmp_cols = []
    for i in col_ls:
        if i not in (df.columns):
            tmp_cols.append(i)
    
    if len(tmp_cols) != 0:
        raise ValueError(f'{tmp_cols} not present in DataFrame.')
    

def getPlates(N, K, P, ls):
    
    max_val = 0
    
    for i in range(1, N+1):
        for j in range(0, P+1):
            if sum(ls[i][:j]) > max_val:
                max_val = sum(ls[i][:j])
    
    return max_val

T = int(input())
for T in range(1, T+1):
    N, K, P = [int(s) for s in input().split(' ')]
    ls = []
    for N in range(1, N+1):
        ls.append([int(s) for s in input().split(' ')])
    print('Case #{}: {}'.format(i, getPlates(N, K, P, ls))
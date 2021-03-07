val = 0

for n in range(1,1000):
    
    if (divmod(n, 3)[1] == 0) | (divmod(n, 5)[1] == 0):
        val += n


def fibseq(n):
    
    tmp_lis = []
    i, j = 0, 1

    if n == 1:
        tmp_lis.append(i)
    if n == 2:
        tmp_lis.append(i)
        tmp_lis.append(j)
    else:
        tmp_lis.append(i)
        tmp_lis.append(j)

        for counter in range(n-2):

            tmp = i + j
            tmp_lis.append(tmp)
            i = j
            j = tmp
 
    return tmp_lis


def fibsum(n):
    
    tmp_sum = 0
    i, j = 0, 1

    while tmp_sum < n:
        print(i, j, tmp_sum)
        tmp = i + j
        i = j
        j = tmp
        tmp_sum += tmp

    return tmp_sum

import math
n = 600851475143
nums = []

if n % 2 == 0: 
    nums.append(2)
    n = n/2

for i in range(3, int(math.sqrt(n))):

    if i % 2 == 1 and n % i == 0:
        nums.append(i)
        n = n/
        

import pandas as pd

df = pd.read_csv('train (2).csv')

cols = df.columns

for col in cols:
    print(f'{col} : {df[col].nunique()}')

df['Employment class'] = df['Employment class'].astype('category')
df['Education level'] = df['Education level'].astype('category')
df['Marital status'] = df['Marital status'].astype('category')
df['Occupation'] = df['Occupation'].astype('category')
df['Relationship status'] = df['Relationship status'].astype('category')
df['Race'] = df['Race'].astype('category')
df['Sex'] = df['Sex'].astype('category')
df['Native country'] = df['Native country'].astype('category')
df['Salary'] = df['Salary'].astype('category')

df['Employment class'] = df['Employment class'].cat.codes
df['Education level'] = df['Education level'].cat.codes
df['Marital status'] = df['Marital status'].cat.codes
df['Occupation'] = df['Occupation'].cat.codes
df['Relationship status'] = df['Relationship status'].cat.codes
df['Race'] = df['Race'].cat.codes
df['Sex'] = df['Sex'].cat.codes
df['Native country'] = df['Native country'].cat.codes
df['Salary'] = df['Salary'].cat.codes

df.to_csv('train (2) text.csv')

df = pd.read_csv('test (1).csv')

cols = df.columns

for col in cols:
    print(f'{col} : {df[col].nunique()}')

df['Employment class'] = df['Employment class'].astype('category')
df['Education level'] = df['Education level'].astype('category')
df['Marital status'] = df['Marital status'].astype('category')
df['Occupation'] = df['Occupation'].astype('category')
df['Relationship status'] = df['Relationship status'].astype('category')
df['Race'] = df['Race'].astype('category')
df['Sex'] = df['Sex'].astype('category')
df['Native country'] = df['Native country'].astype('category')
#df['Salary'] = df['Salary'].astype('category')

df['Employment class'] = df['Employment class'].cat.codes
df['Education level'] = df['Education level'].cat.codes
df['Marital status'] = df['Marital status'].cat.codes
df['Occupation'] = df['Occupation'].cat.codes
df['Relationship status'] = df['Relationship status'].cat.codes
df['Race'] = df['Race'].cat.codes
df['Sex'] = df['Sex'].cat.codes
df['Native country'] = df['Native country'].cat.codes
#df['Salary'] = df['Salary'].cat.codes

df.to_csv('test (1) text.csv')

import random
i = 10  # No. of reviews
t = 1000  # No. of trials

ls = []
for j in range(t):
    ls.append(round(sum([1 if random.random() < 0.95 else 0 for x in range(i)])/i, 2))

k = set(ls)
for _ in k:
    print(f'{_} .. {ls.count(_)}')


import pandas as pd

df = pd.DataFrame.from_dict({'ORDER_ID': [1,1,1,2,3],
'PRODUCT_PRICE':  [100, 50,25,500,350],
'COUPON_DISCOUNT': [5,10,10,10,0],
'OTHER_DISCOUNT': [10,0,0,20,0],
'DELIVERY_COST': [5,5,5,2,10]})

df = pd.DataFrame(df.groupby('ORDER_ID')[['PRODUCT_PRICE', 'COUPON_DISCOUNT', 'OTHER_DISCOUNT', 
        'DELIVERY_COST']].agg({'PRODUCT_PRICE':'sum', 'COUPON_DISCOUNT':'sum',
        'OTHER_DISCOUNT':'sum', 'DELIVERY_COST':'mean'})).reset_index()

df['FINAL_PRICE'] = df['PRODUCT_PRICE']-df['COUPON_DISCOUNT']-df['OTHER_DISCOUNT']+df['DELIVERY_COST']
import timeit

# 4. Largest palindrome product
# https://projecteuler.net/problem=4

approach1 = '''

nums = 0
fin_num = 0

for i in range (1000, 99, -1):
    for j in range(1000, 99, -1):
        if str(i*j) == str(i*j)[::-1]:
            if ((i+j) > nums) & ((i*j) > fin_num):
                fin_i, fin_j, fin_num = i, j, (i*j)

print(fin_num)
'''

approach2 = '''

nums = 0
fin_num = 0

for i in range (1000, 99, -1):
    for j in range(1000, 99, -1):
        if ((i+j) > nums) & ((i*j) > fin_num):
            if str(i*j) == str(i*j)[::-1]:        
                fin_i, fin_j, fin_num = i, j, (i*j)

print(fin_num)
'''

approach3 = '''

nums = 0
fin_num = 0

for i in range (1000, 99, -1):
    for j in range(1000, 99, -1):
        if ((i+j) > nums) & ((i*j) > fin_num) & (str(i*j) == str(i*j)[::-1]):
                fin_i, fin_j, fin_num = i, j, (i*j)

print(fin_num)
'''

# 5. Smallest multiple -- SOLVED -- NEEDS OPTIMIZATION
# https://projecteuler.net/problem=5

num = 1
i = 1

while i < 21:

    if divmod(num, i)[1] == 0:
        i += 1
        #print(i, num)
    else:
        num += 1
        i = 1

    if i == 20:
        print(num)
        break
        
# 6. Sum square distance - SOLVED -- NEEDS OPTIMIZATION
# https://projecteuler.net/problem=6

(sum([x for x in range(1, 101)]))**2 - sum([x**2 for x in range(1, 101)])

# 7. 10001st prime
# https://projecteuler.net/problem=7

n = 2
counter = 0

if n == 2: 
    counter += 1

if divmod(n, 2)[1] == 0 and n != 2:
    break

# 8. Largest product in a series
# https://projecteuler.net/problem=8

num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

pdt = 0

for idx, i in enumerate(num):
        if idx <= (len(num)-12):
                
                tmp_str = num[idx:idx+13]
                print(tmp_str)
        
                if '0' in tmp_str:
                        continue
                else:
                        tmp_nums = [int(s) for s in tmp_str]

                tmp_pdt = 1
                for n in tmp_nums:
                        tmp_pdt *= n

                if tmp_pdt > pdt:
                        pdt = tmp_pdt

# 9. Special Pythagorean triplet
# https://projecteuler.net/problem=9

for i in range(1, 998):
    for j in range(1, 997):
        for k in range(1, 996):
            if i < j and j < k:
                if (i**2)+(j**2)==(k**2):
                    if i+j+k == 1000:                
                        print(i,j,k)
                        break

counter = 0 

for i in range(2, 10):
    print(f'i: {i}')
    print(f'counter1: {counter}')

    for j in range(2, i):
        print(f'j: {j}')
        if divmod(i, j)[1] == 0:
            print(divmod(i, j))
            print(f'counter: {counter}')
            break
        else:
            counter += i
            print(f'counter2: {counter}')

        
list_result = [{'name':'John', 'score':5},
        {'name':'John', 'score':6},
        {'name':'James', 'score':7},
        {'name':'James', 'score':8}]

list_result = 

def get_highest(i):
    return list_result.get(max(i))

b('James')
fin_val = [{list(i.values())[0]:list(i.values())[1]} for i in list_result] if i.values[1] > fin_val.get(i.values[0], 0)]
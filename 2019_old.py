def pickTeam(N, P, ls):

    ls = sorted(ls)
    max_diff = max(ls)
    max_strength = 0
    s = 0
    e = 0
    ans = 0

    for i in range(0, N-P+1):
        diff = abs(max(ls[i:i+P]) - min(ls[i:i+P]))
        strength = sum(ls[i:i+P])
        if diff < max_diff and max_strength < strength:
            max_diff = diff
            s = i
            e = i+P
        if max_diff == 0:
            return ans
            break
    
    else:
        tgt = max(ls[s:e])
        for i in ls[s:e]:
            if i  < tgt:
                ans  += (tgt - i)

    return ans


def pickTeam(N, P, ls):
    
    ls = sorted(ls, reverse=True)
    min_diff = ls[0]
    
    for i in range(0, N-P+1):
        diff = (P*ls[i]) - sum(ls[i:i+P])
        if diff < min_diff:
            min_diff = diff

    return min_diff


def pickTeam(N, P, ls):

    ls = sorted(ls, reverse=True)
    ls = sorted(ls, key=ls.count, reverse=True)
    
    def _checkSize():
        if len(ls) > P:
            if ls[0] > sum(ls[1:P]):
                ls.pop(0)
                _checkSize()
    
    _checkSize()

    return (P*ls[0]) - sum(ls[:P])

T = int(input())
for i in range(1, T+1):
    N, P = [int(s) for s in input().split(' ')]
    ls = [int(s) for s in input().split(' ')]
    print('Case #{}: {}'.format(i, pickTeam(N, P, ls)))


ls = [5, 5, 1, 2, 3, 4]

ls = [3, 1, 9, 100, 210, 345, 500]
P = 3


def pickTeam(N, P, ls):

    ls = sorted(ls, reverse=True)
    ls = sorted(ls, key=ls.count, reverse=True)    

    th = ls[0]

    for i in range(0, len(ls)-P+1):
        ls1 = ls[i:i+P]
        if (P*ls1[0]) - sum(ls1) < th:
            th = (P*ls1[0]) - sum(ls1)
    
    return th


def countDown():

    a = '1 2 3 7 9 3 2 1 8 3 2 1'

    tmp = ls[0]
    count = 0

    for i in ls:

        if i = 1:
            if ls.index(i) != 0:
                if tmp == 2:
                    count += 1
                else:
                    tmp = i

    return count


burger_type = [1, 2, 3]
burger_subtype = []
print('1.chick 2.beef 3.veg')

c = [1, 2]
b = [1, 2 , 3]

sel_ls()

def sel_bur(ls):
    burger_choice = int(input())

    if burger_choice > len(burger):
        print('Select a burger dumbass')
        burger_choice = int(input())
    
    else:
        burger_sel = burger[burger_choice-1]
        print(f'selected burger is {burger[burger_sel]}')


ls1 = [1, 43, 66, 3, 53, 3, 2, 1, 1, 11, 42]

a, *b, c = ls1


ls = [1, 2, 3, 7, 9, 3, 2, 1, 8, 3, 2, 1]
K = 3

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






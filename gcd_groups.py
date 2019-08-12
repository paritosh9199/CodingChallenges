import itertools

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
        
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
    
def prod(arr):
    prod = 1
    for i in arr:
        prod *= i
    return prod

def form_group(arr):
    len_arr = len(arr)
    result_groups = []

    # mid = int(len_arr/2)+1
    
    for i in range(1, len_arr):
        res_list = []
        result = itertools.combinations(arr, i)
        for each in result:
            list_a = list(each)
            list_b = Diff(arr, list_a)
            result_groups.append([list_a, list_b])

    return result_groups


n = int(input())
grp = []
while(n > 0):
    a = int(input())
    b = input()
    b = b.strip().split(" ")
    len_b = len(b)
    group_count = 0
    
    for i in range(len_b):
        b[i] = int(b[i])

    
    groups = form_group(b)
    for j in groups:
        if(gcd(prod(j[0]), prod(j[1])) == 1):
            group_count += 1
    

    grp.append(group_count)
    n -= 1

for i in grp:
    print(i)

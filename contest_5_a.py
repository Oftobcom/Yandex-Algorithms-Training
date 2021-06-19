def find_match(n_colours, m_colours):
    i = j = 0
    best_i = i
    best_j = j
    best_diff = 10*7 + 1

    n = len(n_colours)
    m = len(m_colours)

##    print(n)
##    print(m)

    flag = True
    while flag and i < n and j < m:
##        print(i,j)
        diff = abs(n_colours[i] - m_colours[j])
##        print(diff)
        if diff == 0:
            best_i = i
            best_j = j
            flag = False
        elif diff < best_diff:
            best_diff = diff
            best_i = i
            best_j = j

        if n_colours[i] <= m_colours[j]:
            i += 1
        else:
            j += 1

    return [best_i, best_j]

N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

i, j = find_match(lst1, lst2)
result = str(lst1[i]) + ' ' + str(lst2[j])
print(result)

while 1:
    m, k = map(int,input().split())
    if (m == 0 and k == 0):
        break
    day = m
    while m >= k:
        day += m // k
        m = m // k + m % k
    print(day)
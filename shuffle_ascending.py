def solution(a):
    l = 0
    r = len(a) -1
    b = []
    while l <= r:
        if l == r:
            b.append(a[l])
        else:
            b.append(a[l])
            b.append(a[r])
        l+=1
        r-=1
    
    asc = True
    for i in range(len(b)-1):
        if b[i] >= b[i+1]:
            asc = False
    print(b)
    return asc

print(solution([-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]))
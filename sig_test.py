def solution(sequence):
    sequence.sort()
    print(sequence)
    if len(sequence) % 2 == 0:
        mid = len(sequence)//2
        print("mid", mid)
        return sum(sequence[mid-1:mid])/2
    else:
        return sequence[len(sequence)//2]

print(solution([-1, 3, -2, 2]))
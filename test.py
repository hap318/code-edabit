def ArrayChallenge(arr):
    arr.sort()
    # code goes here
    print(arr)
    print(arr[-4:])
    s = sum(arr[:4])
    return s

# keep this function call here 
print(ArrayChallenge([4,7,38,53,2,5]))
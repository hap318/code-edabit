def lengthsOflongestContiguousElems(input):
    #assuming input has at least one element else return None
    output = []
    for i in range(len(input)):
        tmp = 1
        j = i-1
        while j >= 0 and input[i] > input[j]:
            tmp += output[j]
            j -= output[j]
        output.append(tmp)
    return output

print(lengthsOflongestContiguousElems([7,3,4,6,9,1,5,6,3,7,4,8,2,10]))
def getCount(binary):
    # Write your code here
    binary_list = list(binary)
    num_dict = {}
    for i in range(pow(2, 10)-1):
        old_pos = 0
        for b in bin(i)[2:]:
            try:
                pos = binary.index(b, old_pos)
                old_pos=pos
            except:
                break
        else:
            if not i in num_dict:
                num_dict[i] = i
    print(num_dict)
    return len(num_dict)

print(getCount("0101"))
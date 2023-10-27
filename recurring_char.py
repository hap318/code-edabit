def recurring_char(seq):
    seq = list(seq)
    og_seq = seq
    for p, i in enumerate(seq):
        seq.pop(p)
        if i in seq:
            return i
        seq = og_seq

def recurring_char2(seq):
    dic = {}
    for i in seq:
        if i in dic:
            return i
        dic[i] = 1
    return None
        

print(recurring_char2("abac"))
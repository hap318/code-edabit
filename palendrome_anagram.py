def solution(word):
    letter_dict = {}
    for l in word:
        if l in letter_dict:
            letter_dict[l] += 1
        else:
            letter_dict[l] = 1
    odd = []
    for l, c in letter_dict.items():
        if c % 2 != 0:
            odd.append(l)
    return len(odd)-1 if len(odd) > 0 else 0

solution("apple")
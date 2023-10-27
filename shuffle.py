def out_suffle(deck):
    deckLen = len(deck)
    newList = []
    fir = deck[:deckLen//2]
    sec = deck[deckLen//2:]
    while True:
        try:
            newList.append(fir.pop(0))
            newList.append(sec.pop(0))
        except:
            pass
        if len(sec) == 0:
            break
    return newList

def shuffle_count(num):
    if num%2 != 0 or num < 2:
        print("error")
        return False
    deck = []
    for i in range(num):
        deck.append(i)
    count = 0
    og_deck = deck
    while True:
        deck = out_suffle(deck)
        if deck == og_deck:
            print("count: ",count+1)
            return count + 1
        else:
            count+=1

shuffle_count(8)
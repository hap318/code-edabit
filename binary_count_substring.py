def binary(s):
  # convert the input string to a list of binary digits
  bin_list=list(s)

  # create a set to hold all the matches we find
  numbers=set()

  # loop over all the possible valid numbers so if s=111 we have 0..2^3-1 = 0..8 = 0..111
  for i in range(pow(2,len(s))-1):
    # we can start at 0 because I changed the code to add one after we find a match
    pos=0

    # convert the target decimal number to binary - removing the leading 0b and grab each binary digit in turn
    for b in bin(i)[2:]:
      
      try:
        # search for the next binary digit from position pos to the end of the string - index returns the position
        pos=bin_list.index(b,pos) + 1
        # we found the binary digit so add 1 o pos so we start looking at the next position after teh match  
      except:
        # we didn't find teh next digit so no match
        break
    else:
      # this get executed if we didn't break so its a valid number
      numbers.add(i)

  print(numbers)
  return len(numbers)



print(binary("011"))
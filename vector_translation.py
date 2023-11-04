def move(a,b,c,d):

  # make a list to hold all the a,b coordinates we will try
  q = []

  # append the initial values as a tuple - tuples are immutable which is fine in this case and faster than lists
  q.append((a,b))

  # while we still have something to try
  while len(q)>0:
    print(q)
    # take a tuple off the queue and extract the values to try into a,b
    a,b=q.pop(0)
    print(f"trying {a},{b}")

    # terminate if we get to c,d
    if a==c and b==d:
      return "Yes"

    # not there yet so try all possible values
    # there are only 2 possible things we can do
    # so try them both by putting on the queue and looping
    # don't try values that have gone past c or d
    if a+b <= c:
      q.append((a+b,b))
    if b+a <= d:
      q.append((a,b+a))

  # we only get here once we've tried every possible value without finding a match
  return "No"


move(1,1,4,5)
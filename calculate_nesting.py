def nesting_level(nest):
    new_list = []
    #if len(nest) == 0:
    #    return None
    for i in nest:
        print(i)
        if isinstance(i, int):
            new_list.append(i)
            print("new list",new_list)
        nesting_level(i)

nesting_level([1, 4, 4, [1, 1, [1, 2, 1, 1]]])
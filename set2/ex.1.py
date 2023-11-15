deepestLevel = 0
deepestLists = []

def nest(_list):
    global deepestLevel
    global deepestLists

    deepestLevel = 0
    deepestLists = []

    search(_list, 0)

    for  i in deepestLists:
        i.append (i[len(i) - 1] + 1)
    return _list

def search(_list, level):
    global deepestLevel
    global deepestLists

    for i in _list:
        if isinstance(i, list):
            search(i, level+1)
    
    if level > deepestLevel:
        deepestLevel = level
        deepestLists = []
        deepestLists.append(_list)
    elif level == deepestLevel:
        deepestLists.append(_list)

list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
print (str(list1) + " => " +  str(nest(list1)), end='\n\n')
list2 = [1, [2, 3], 4]
print (str(list2) + " => " +  str(nest(list2)), end='\n\n')
list3 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
print (str(list3) + " => " +  str(nest(list3)), end='\n\n')
list4 = [1, [3], [2]]
print (str(list4) + " => " +  str(nest(list4)), end='\n\n')
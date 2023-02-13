def isSubset( a1, a2):
    d=dict(Counter(a1))
    print(d)
    for i in a2:
        if(i in d.keys()):
            if(d.get(i)>1):
                d[i]=d.get(i)+1
                print(d)
            else:
                d.pop(i)
        else:
            return "No"
    return "Yes"

print([11, 1, 13, 21, 3, 7],[11, 3, 7, 1])    
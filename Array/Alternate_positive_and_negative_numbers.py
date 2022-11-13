def rearrange(arr, n):
    ptr1 = 0
    ptr2 = 0
    pos = []
    neg = []
    for i in arr:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    arr.clear()
    while ptr1<len(pos) or ptr2<len(neg):
        if ptr1!=len(pos):
            arr.append(pos[ptr1])
            ptr1+=1
        if ptr2!=len(neg):
            arr.append(neg[ptr2])
            ptr2+=1
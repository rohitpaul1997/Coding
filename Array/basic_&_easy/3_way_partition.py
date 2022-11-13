def threeWayPartition(self, array, a, b):
    l = []
    l1 = []
    l2 = []
    for i in array:
        if i<a:
            l.append(i)
        elif a>=i<=b:
           l1.append(i)
        else:
             l2.append(i)
    d = l+l1+l2 
    array[:] = d[:]
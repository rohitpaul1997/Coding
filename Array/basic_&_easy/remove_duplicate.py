
#best approch

A[::] = sorted(list(set(A)))
	    return len(A)

#better approach
x = 0
        while (x + 1 <= len(A) - 1):
            if A[x] == A[x + 1]:
            #if A[x] in A[x + 1:]:
                A.pop(x)
            else:
                x += 1
        return len(A)        
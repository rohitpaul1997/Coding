
#best approch
def a(A):
    A[::] = sorted(list(set(A)))
    return len(A)

#better approach
def a(A):
    x = 0
    while (x + 1 <= len(A) - 1):
        if A[x] == A[x + 1]:
            A.pop(x)
        else:
            x += 1
    return len(A)        
def areIsomorphic(self, str1, str2):
    if len(str1) != len(str2):
        return False
    dict1, dict2 = {}, {}

    for i, j in zip(str1, str2):
        if i not in dict1 and j not in dict2:
            dict1[i] = j
            dict2[j] = i
        elif i in dict1 and j in dict2 and dict1[i] != j and dict2[j] != i:
            return 0
        elif i in dict1 and j not in dict2:
            return 0
        elif i not in dict1 and j in dict2:
            return 0
    return 1

def minValue(s, k):
        # code here
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        value = list(dic.values())
        for i in range(k):
            val = value.index(max(value))
            value[val] = value[val] - 1
        return sum([i**2 for i in value])

print(minValue("aabcbcbcabcc",3))        
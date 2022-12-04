def genIp(s):
    ans = []
    generate(s, 0, len(s) - 1, 1, '', ans)
    return ans


def generate(s, i, j, level, temp, ans):
    if (i == (j + 1)) and level == 5:
        ans.append(temp[1:])
    k = i
    while k < i + 3 and k <= j:
        ad = s[i: k+1]
        if (s[i] == '0' and len(ad) > 1) or int(ad) > 255:
            return
        generate(s, k + 1, j, level + 1, temp + '.' + ad, ans)
        k = k + 1
    return



print(genIp("55"))
def unique_substrings(s):
    last_pos = [0] * 26
    partitions = 0
    last_end = 0
    for i in range(len(s)):
        if last_pos[ord(s[i]) - ord('a')] >= last_end:
            partitions += 1
            last_end = i + 1
            print("last end : ",last_end)
        last_pos[ord(s[i]) - ord('a')] = i + 1
        print(last_pos)
    return partitions


print(unique_substrings("abacaba"))
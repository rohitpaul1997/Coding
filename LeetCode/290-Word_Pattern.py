def wordPattern(pattern: str, s: str) -> bool:
    d = {}
    text = s.split(" ")
    if len(pattern) != len(text):
        return False
    for i in range(0,len(pattern)):
        if pattern[i] in d:
            if d[pattern[i]] != text[i]:
                return False
        elif text[i] in d.values():
            val_list = list(d.values())
            if len(val_list) > 1:
                return False
            else:
                key_list = list(d.keys())
                position = val_list.index(text[i])
                # print(key_list[position])
                if pattern[i] != key_list[position]:
                    return False
        else:
            d[pattern[i]] = text[i]                
    return True


print(wordPattern('abba','dog dog dog dog'))

from collections import Counter

s = "cccaaa"

freq = Counter(s)
sorted_chars = sorted(freq, key=freq.get, reverse=True)
sorted_string = ''.join([char*freq[char] for char in sorted_chars])
print(sorted_string)
from collections import Counter, deque


def minWindow(s: str, t: str) -> str:
    tCounter = Counter(t)  # counter for t to check with
    window = Counter()  # sliding window
    ans = ""  # answer
    last = 0  # last index in our window
    for i, char in enumerate(s):
        # add this character to our window
        window[char] = window.get(char, 0)+1
        while window >= tCounter:  # while we have all the necessary characters in our window
            # if the answer is better than our last one
            if ans == "" or i - last < len(ans):
                ans = s[last:i+1]  # update ans
            # remove the last element from our counter
            window[s[last]] -= 1
            last += 1  # move the last index forward
    return ans


print(minWindow("ADOBECODEBANC", "ABC"))

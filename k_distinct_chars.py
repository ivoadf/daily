# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def valid(counts, k):
    total = 0
    for _, c in counts.items():
        if c > 0:
            total += 1
    if total <= k:
        return True
    return False

def fun(s,k):
    left = 0
    right = 0
    counts = {}
    max_len = 0
    for i in range(len(s)):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
        right += 1

        while not valid(counts,k):
            counts[s[left]] -= 1
            left += 1

        if right - left > max_len:
            max_len = right-left

    return max_len

print(fun("abcba",2))#3
print(fun("aabacbebebe",3))#7
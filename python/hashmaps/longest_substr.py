def lengthOfLongestSubstring2(s):
    # first run to look for subset
    t = ''
    ss = ''

    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if s[j] not in ss:
                ss = ss +s[j]
            if ss in s and len(ss) > len(t):
                t = ss
        ss = ''

    print(len(t))


lengthOfLongestSubstring2('pwwkew')

# abcabcbb
# pwwkew
# pwke
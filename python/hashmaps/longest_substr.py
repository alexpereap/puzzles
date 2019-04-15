def lengthOfLongestSubstring(s):
    a = [v for v in s]

    # first run to look for subset
    t = ''
    c = 0
    ss = ''

    while c <= len(s):
        for i in range(c, len(s)):
            if s[i] not in ss:
                ss = ss +s[i]
            if ss in s and len(ss) > len(t):
                t = ss
        c = c+1
        ss = ''

    print(len(t))


def lengthOfLongestSubstring(s):
   ss = s[0]
   m = 0
   for i in range(1, len(s)):
       if s[i] in ss:
           m = len(ss)
           break
       else:
           ss = ss + s[i]



lengthOfLongestSubstring('dvdf')

# abcabcbb
# pwwkew
# pwke
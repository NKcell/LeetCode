"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    sdict = {}
    for i in s:
        if i in sdict:
            sdict[i] = sdict[i] + 1
        else:
            sdict[i] = 1

    for key, value in sdict.items():
        if key in s:
            if value == t.count(key):
                pass
            else:
                return False
        else:
            return False

    return True


print(isAnagram('你好','好你'))

"""
return sorted(s) == sorted(t)
"""

"""
return collections.Counter(s) == collections.Counter(t)
"""

"""
 for i in string.ascii_lowercase:
            if s.count(i) != t.count(i):
                return False
        return True
"""

"""
all([s.count(c)==t.count(c) for c in set(s+t)])
"""
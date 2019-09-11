"""
500. Keyboard Row
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    l1 = ['q','w','e','r','t','y','u','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
    l2 = ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
    l3 = ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']

    re = []

    for i in words:
        temp = list(set(list(i)))
        if temp[0] in l1:
            l = l1
        if temp[0] in l2:
            l = l2
        if temp[0] in l3:
            l = l3
        flag = 0
        for character in temp:
            if character not in l:
                flag = 1
                break

        if flag == 0:
            re.append(''.join(i))

    return re

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))


# 正则表达式
"""
def findWords(self, words):
    return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
"""

"""
def findWords(self, words):
        return [w for w in words if any(not set(w.lower()) - row for row in (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")))]
"""
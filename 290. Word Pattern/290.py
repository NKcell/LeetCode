"""
290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space
"""

def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    strlist = str.split()
    str_dict = {}
    if len(pattern) != len(strlist):
        return False

    count = 0
    for i in pattern:
        str_dict[i] = str_dict.get(i, []) + [count]
        count += 1

    if len(set(strlist)) != len(str_dict):
        return False

    for key in str_dict:
        temp = []
        for i in str_dict[key]:
            temp.append(strlist[i])
        if len(set(temp)) != 1:
            return False

    return True

print(wordPattern("abba", "dog dog dog dog"))


"""
other = []
        words = str.split()
        if len(pattern) != len(words):
            return False
        thisDict = dict()
        for i in range(len(pattern)):
            patElem = pattern[i]
            strElem = words[i]
            if patElem in thisDict:
                if words[i] != thisDict[patElem]:
                    return False
            else:
                if strElem in other:
                    return False
                thisDict.update({patElem: strElem})
                other.append(strElem)
        return True
"""
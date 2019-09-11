"""
443. String Compression
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.


Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

"""

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    pre = 0
    new = []
    for i in range(len(chars)-1):
        if chars[pre] == chars[i+1]:
            if type(chars[i]) == int:
                chars[i+1] = chars[i] + 1
            else:
                chars[i+1] = 2
        else:
            new.append(chars[pre])
            if type(chars[i]) == int:
                new.append(chars[i])
            pre = i+1
    new.append(chars[pre])
    if type(chars[-1]) == int:
        new.append(chars[-1])


    re = []
    flag = 0
    for i in new:
        if type(i) == str:
            re.append(i)
            chars[flag] = re[flag]
            flag += 1
        else:
            for j in str(i):
                re.append(j)
                chars[flag] = re[flag]
                flag += 1
    return len(re)




print (compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))




"""
class Solution(object):
    def compress(self, chars):
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left
"""




















"""
Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    my_dict = {}
    for i in nums:
        try:
            del my_dict[i]
        except:
            my_dict[i] = i

    re = []
    for key in my_dict:
        re.append(key)

    return re


print(singleNumber([1,2,1,3,2,5]))


# collections这个模块真的是个神模块啊
"""
from collections import Counter

def singleNumber(nums):
	return [x[0] for x in Counter(nums).most_common()[-2:]]
"""
#这个二进制的方法很有想法啊，先全部异或找出最终两个数不同的位数，找其中一个为线将数分为两组，然后每组异或分别得到这两个数
"""
现在数组中有两个数字只出现1次，直接异或一次只能得到这两个数字的异或结果，但光从这个结果肯定无法得到这个两个数字。因此我们来分析下简化版中“异或”解法的关键点，这个关键点也相当明显——数组只能有一个数字出现1次。

设题目中这两个只出现1次的数字分别为A和B，如果能将A，B分开到二个数组中，那显然符合“异或”解法的关键点了。因此这个题目的关键点就是将A，B分开到二个数组中。由于A，B肯定是不相等的，因此在二进制上必定有一位是不同的。根据这一位是0还是1可以将A，B分开到A组和B组。而这个数组中其它数字要么就属于A组，要么就属于B组。再对A组和B组分别执行“异或”解法就可以得到A，B了。而要判断A，B在哪一位上不相同，只要根据A异或B的结果就可以知道了，这个结果在二进制上为1的位就说明A，B在这一位上是不相同的。

比如

int a[] = {1, 1, 3, 5, 2, 2}
整个数组异或的结果为3^5，即 0x0011 ^ 0x0101 = 0x0110

对0x0110，第1位（由低向高，从0开始）就是1。因此整个数组根据第1位是0还是1分成两组。

a[0] =1  0x0001  第一组

a[1] =1  0x0001  第一组

a[2] =3  0x0011  第二组

a[3] =5  0x0101  第一组

a[4] =2  0x0010  第二组

a[5] =2  0x0010  第二组
第一组有{1,1,5}，第二组有{3,2,3}，然后对这二组分别执行“异或”解法就可以得到5和3了。
"""
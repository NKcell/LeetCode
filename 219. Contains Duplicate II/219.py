class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        nums_dict = {}
        for index,nums_value in enumerate(nums):
            tmp = nums_dict.get(nums_value,[])
            nums_dict[nums_value] = tmp+[index]

        for list_value in nums_dict.values():
            value_differ = []
            for index in range(len(list_value)-1):
                value_differ.append((list_value[index+1]-list_value[index]))
            if len(value_differ)>0:
                tmp_min = (min(value_differ))
                if tmp_min <= k:
                    return True
        return False

    def containsNearbyDuplicate1(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False

a = Solution()
print(a.containsNearbyDuplicate( [1,2,3,1,2,3], k = 4))
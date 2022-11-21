from operator import truediv


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int):
        val_index_map = {}
        for i in range(len(nums)):
            val = nums[i]
            if val not in val_index_map:
                val_index_map[val] = [i]
            else:
                index_list = val_index_map[val]
                if i - index_list[-1] <= k:
                    return True
                index_list.append(i)
        return False
            
        
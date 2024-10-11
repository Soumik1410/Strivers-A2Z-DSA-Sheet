class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        counts = {}
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
                key = str(nums[i]) + "_" + str(counts[nums[i]])
                indices[key] = i
            else:
                counts[nums[i]] += 1
                key = str(nums[i]) + "_" + str(counts[nums[i]])
                indices[key] = i
        #print(indices)
        #print(count)
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            key1 = str(diff) + "_1"
            key2 = str(diff) + "_2"
            if diff != nums[i] and key1 in indices:
                result.append(i)
                result.append(indices[key1])
                break
            if key2 in indices:
                result.append(i)
                result.append(indices[key2])
                break
        return result

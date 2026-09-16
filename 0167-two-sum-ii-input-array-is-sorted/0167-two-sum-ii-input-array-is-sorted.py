class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}  
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[num] = i
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
	if(len(nums) < 2):
		if(nums[0] == target):
			return [0]
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if(nums[i] + nums[j] == target):
				return [i, j]
	return []


nums = list(map(int, input("List 입력 (공백 구분) : ").split()))
target = int(input("Target 입력 : "))
print(str(twoSum(nums, target)) + " (index 기준)")
def bin_search(nums, low, high, x):
	'''
		if high >= low:
			mid = (high+low)//2

			if x==nums[mid]:
				return mid

			elif x<nums[mid]:
				return bin_search(nums, low, mid-1, x)

			elif x>nums[mid]:
				return bin_search(nums, mid+1, high, x)
		else:
			return -1
	'''
	
	while True:
		mid = (high+low)//2

		if x>nums[mid]:
			low = mid+1

		elif x<nums[mid]:
			high = mid-1

		elif x==nums[mid]:
			return mid
		
			
			
	

nums = sorted([43,76,23,7,56,98,36,23,86,35,25,87])
print(nums)
low = 0
high = len(nums)-1
x = 8

print(bin_search(nums, low, high, x))



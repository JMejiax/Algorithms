# Binary search is use to find a value storage into an sorted	# To find the mid value you can use the following formula:
# array. Always start from the half value of the array and if  -->	# m = L + (R-L) // 2 where L is the left index and 
# the value is not the correct value, then it moves right or		# R is the right index.
# left.

#------------------------------------------------------------------------------------------------------------------------------#

# First you campare the value at arr[mid] and if it is equal		# if it is lower than the target value you set R to mid - 1.	
# to the target value you return the index mid. If it is	  -->	# In other words, you change the part of the array used to
# greater than the target value you set L value to mid + 1,			# the left or to the right.

# basic implementation Binary Search
def BinarySearch(arr, target):
	L = 0
	R = len(arr)-1
	while L <= R:
		mid = L + (R-L) // 2
		if arr[mid] == target:
			return mid
		if arr[mid] < target:
			L = mid + 1
		else:
			R = mid - 1
	return -1
	

index = BinarySearch([1,2,3,4,5], 2)
print(index)



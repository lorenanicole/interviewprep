# Algorithms
# Merge Sort Big O(n log n), n merges, log n divides!
def merge_sort(my_list):
	if len(my_list) == 0 or len(my_list) == 1:
		return my_list

	mid = len(my_list) / 2
	left = merge_sort(my_list[:mid])
	right = merge_sort(my_list[mid:])
	return merge(left, right)

def merge(left, right):
	
	merged = []
	left_indx, right_indx = 0, 0

	while left_indx < len(left) and right_indx < len(right):
		if left[left_indx] < right[right_indx]:
			merged.append(left[left_indx])
			# merged_indx += 1 <-- can add this to permit in-place mutation for list
			left_indx += 1
		else:
			merged.append(right[right_indx])
			# merged_indx += 1
			right_indx += 1

	if len(left) != left_indx:
		merged += left[left_indx:]

	if len(right) != right_indx:
		merged += right[right_indx:]

	return merged

# my_arr = [6,3,99,12,15,4,5]
# res = mergesort(my_arr)
# print res, my_arr

# Quick Sort Big O(n log n) best case, worst Big O(n**2), n checks * log n divides! 
# If doesn't split list into half, then approach worst case performance for time complexity.
# Doesn't use additional memory storage.
def quick_sort(my_list, begin=0, end=None):
	if end is None:
		end = len(my_list) - 1
	if begin >= end:
		return
	# Find initial split point with less than and greater than
	split_point = partition(my_list, begin, end)
	quick_sort(my_list, begin, split_point - 1)
	quick_sort(my_list, split_point + 1, end)

def partition(my_list, begin, end):
	pivot = begin

	for indx in range(begin+1, end+1):
		# Sort smaller values to left of pivot
		if my_list[begin] >= my_list[indx]:
			pivot += 1
			my_list[pivot], my_list[indx] = my_list[indx], my_list[pivot]
	# Swap the pivot into new pivot indx
	my_list[begin], my_list[pivot] = my_list[pivot], my_list[begin]

	return pivot
# my_arr = [6,3,99,12,15,4,5]
# quick_sort(my_arr)
# print my_arr


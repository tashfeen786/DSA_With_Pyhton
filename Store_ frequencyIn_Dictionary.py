nums = [5, 6, 7, 7, 1,9,111, 1, 1, 5, 1, 1]
# This code stores the frequency of each number in a dictionary
frequency_dict = dict()

for i in range(0, len(nums)):
    if nums[i] in frequency_dict:
        frequency_dict[nums[i]] += 1
    else:
        frequency_dict[nums[i]] = 1
print("Frequency of each number in the list:", frequency_dict)

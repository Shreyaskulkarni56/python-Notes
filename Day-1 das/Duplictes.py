def dup(nums):
    hashset=set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

duplicates=[1,2,3,4]
result =dup(duplicates)
print(result)
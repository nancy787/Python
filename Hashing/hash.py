# Count Frequincy in list
# hasing = presetore and fetch
def countFrequency(nums) :
    freq = {}
    for val in nums :
        if val in freq :
            freq[val] += 1
        else :
            freq[val] = 1

    return freq

nums = [10,5,10,15,10,5]
print(countFrequency(nums))

# highest orders
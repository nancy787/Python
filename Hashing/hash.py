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

# highest and lowest freqency

def HighandLowFrequency(nums) :
    freq = {} 
    for val in nums :
        if val in freq :
            freq[val] += 1
        else :
            freq[val] = 1

    highest_element = None
    highest_count = 0

    lowest_element = None
    lowest_count = float('inf')

    freq = HighandLowFrequency(nums)

    for key, count in freq.items():
        if count > highest_count:
            highest_count = count
            highest_element = key
        if count < lowest_count:
            lowest_count = count
            lowest_element = key


    print("Highest:", highest_element, "->", highest_count)
    print("Lowest:", lowest_element, "->", lowest_count)

    print(HighandLowFrequency([10,5,10,15,10,5]))

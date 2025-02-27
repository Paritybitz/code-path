def reverse_sentence(sentence):
    rev_arr = sentence.split(" ")[::-1]
    
    print(" ".join(rev_arr))

reverse_sentence("hopefully this works out")


# 2 vars, one for min other for max
# trav thru nums arr
# if int > min && < max, return (break)
# else ret -1

def goldilocks_approved(nums):
    # min = min(nums)
    # max = max(nums)

    for i in nums:
        if i > min(nums) and i < max(nums):
            return i
        else:
            return -1
            
goldilocks_approved([1,2,3,4,5,6,7,8,9,10])
    
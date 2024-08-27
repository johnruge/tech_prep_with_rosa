#three_sum(Rosa's version)
"""
return true if there are three numbers that add up to the target and false if
there is not.
"""

def three_sum(nums, target):
    dict_nums = {}
    for i, v in enumerate(nums):
        dict_nums[v] = i

    for l in range(len(nums) - 2):
        for r in range(l + 1, len(nums) - 1):
            third_num = target - (nums[l] + nums[r])
            if third_num in dict_nums:
                idx = dict_nums[third_num]
                if idx != l and idx != r and idx > r:
                    return True

    return False

def main():
    print(three_sum([1, 2, 3, 4], 9))
    return None

if __name__ == "__main__":
    main()






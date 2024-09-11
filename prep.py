#1 three_sum(Rosa's version)
"""
return true if there're three numbers that add up to the target and false if
there is not.
"""

def three_sum(nums: list[int], target: int) -> bool:
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

#2 two_sum(blind75)
"""
Given an array of integer nums and an integer target, return
indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#3 best time to buy and sell stock
"""
You are given an array of prices where prices[i] is the price of a
given stock on an ith day.
You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that
stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0
"""


def main():
    print(two_sum([0,7,3, 15, 4, 89, 5, 6, 123], 9))
    return None

if __name__ == "__main__":
    main()






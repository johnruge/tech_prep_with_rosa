#1 three_sum(Rosa's version)
"""
return true if there're three numbers that add up to the target and false if
there is not.
"""

#the best i could to is o(n^2)
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

# o(n^2) solution. this is the brute force solution. it is not efficient but uses less space.
def two_sum_brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# o(n) solution. this is a more efficient solution that uses extra space creating a dictionary.
def two_sum_eff(nums: list[int], target: int) -> list[int]:
    dict_nums = {target - nums[0]: [nums[0], 0]}

    for i in range(1, len(nums)):
        if nums[i] in dict_nums:
            return [dict_nums[nums[i]][1], i]
        dict_nums[target - nums[i]] = [nums[i], i]


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

#o(n). this solution is pretty efficient. i used the sliding window technique
def max_profit_stocks(prices: list[int]) -> int:
    min_price, max_profit = prices[0], 0

    for i in range(1, len(prices)):
        if prices[i] <= min_price:
            min_price = prices[i]
        elif prices[i] > min_price:
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)

    return max_profit


#4 contains duplicate
"""
Given an integer array nums, return true if any value appears at
least twice in the array, and return false if every element is
distinct.
Input: nums = [1,2,3,1]
Output: true
"""

#O(n). pretty efficient
def contains_duplicate(nums: list[int]) -> bool:
    set_nums = set()
    for i in range(len(nums)):
        if nums[i] in set_nums:
            return True
        set_nums.add(nums[i])

    return False

#product of array except self
"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[I].
The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.
You must write an algorithm that runs in O(n) time and without
using the division operation.
"""
def main():
    print(contains_duplicate([100,1000, 30,10,4]))
    return None

if __name__ == "__main__":
    main()






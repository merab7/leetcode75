"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""


def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        # checking ig the index is avalable for insertion
        if flowerbed[i] == 0:
            # if the place is avalable than we should check places riget and left to it
            empty_left_plot = (i == 0) or (
                flowerbed[i - 1] == 0
            )  # this variable is eather true or false dependfing if it is index 0 or to the left to current index with value 0
            empty_right_lot = (i == len(flowerbed) - 1) or (
                flowerbed[i + 1] == 0
            )
            # same goes above only for right at first we ar checking if index with value 0 is last if it is wa are considering its right side as emty because it is last element and if it is not las than we are cheking place to its right side
            if empty_left_plot and empty_right_lot:
                # if right and left are empty we are inserting the flower and adding 1 to the count
                # if count is more then n we are returning right aweay
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

    return count >= n

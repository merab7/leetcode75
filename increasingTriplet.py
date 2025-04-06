"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

"""

"""
ამ შემთხვევაში ჩვენ შეგვიძლია ავიღოთ ორი ცვლადი რომელიც ინქნება ტოლი ფლოატ დადებითი ინფინიტისა შესაბამისად თავდაპირველად ყველა შესაძლო მნიშვნელობა 
საცდელ ლისტში იქნება მასზე მცირე შემდეგ კი იტერაცია უნდა მოვახდინოთ ამ ცხრილზე და იფ ელს წინადადებით უნდა გავარკვიოთ მოცემული ლელემენტი არი თუ არა ნაკლებ
ამ ცვლადებზე შესაბამისად ამით თეორიულად მივიღებთ წყვილს რომელიც წრდადობის მიხედვით განლაგდება და მესამე ელს წინადადებაში გავწერთ რომ თუ არცერთზე ნაკლები ან ტოლი არაა ანუ მათზე მეტია და შესაბამისად ტრიპლეტი იკვრება ანუ დავბაბრუნებთ True-ს სხვა შემთხვევაში კი False-ს
"""


def increasingTriplet(self, nums: List[int]) -> bool:
    i = float("inf")
    j = float("inf")
    for x in nums:
        if x <= i:
            i = x
        elif x <= j:
            j = x
        else:
            return True

    return False


"""
O(n)
O(1)
"""

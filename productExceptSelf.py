"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]



Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.



Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    pre = 1
    for i in range(n):
        res[i] = pre
        pre *= nums[i]
    suf = 1
    for j in range(n - 1, -1, -1):
        res[j] *= suf
        suf *= nums[j]

    return res


"""
მოკლედ აქ მთავარი თემა ის არის რომ უნდა მივიღოთ სუმაციური ნამრავლი მყისიერ ინდექსზე არსებული მნიშვნელობის გამოკლებით.
და შეზღვუდვა მოიცავს რომ არ უნდა გავყოთ ამ მნიშვნელობაზე და ასევე დროითი მნიშვნელობა ალგორითმის უნდა იხოს O(n) ხოლო სივრციტი 
O(1). ამ მიზნის მისაღწევად ცალცალკე ხდება მყისიერ მნიშვნელობამდე და მნიშვნელობის შემდეგ სუმაციური ნამრავლის გამოთვლა და შემდეგ მათი გადამრავლებით
სასურველი შედეგის მიღება უბრალოდ ზევიძთ არსებულ მიდგოიმაში არ ხდება ცალ-ცალკე მასივების შექმნა და პრეფიქს/სუფიქსის დინამიკმური ცვლილებით და მათი დამატებით პასუხის მასივში ვიღებთ სასურველ შედეგს.
"""

"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

from math import gcd


str1, str2 = "ABABAB", "ABAB"


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[: gcd(len(str1), len(str2))]


print(gcdOfStrings(str1, str2))

"""
ვაომპორტებთ gcd-ს რომელიც არის ფუნქცია და გვაძლევს უდიდეს საერთო გამყოფს.
ვამოწმებთ ორი სტრინგის ჯამი შეპირაპირებულად არის თუ არა ერთი და იგივე თუ არა ვაბრუნებთ ცარიელ სტრინგს
თუ კი მაშინ ვაბრუნებთ პირველ სტრინგს რომელიც მოიცავს ასოებს იმ რაოდენობით დაწყებული 0 ინდექსიდან რაც წარმოადგენს ორი სტრინგის სიგრძის უდიდეს საერთO გამყოფს
"""

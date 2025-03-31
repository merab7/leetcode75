"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""

word1 = "abcd"
word2 = "pq"


def mergeAlternately(word1: str, word2: str) -> str:
    leng = len(word1) + len(word2)
    result = ""
    if len(word1) == 0 or len(word2) == 0:
        return word1 + word2
    l = 0
    r = 0
    while r <= leng or l <= leng:
        if l < len(word1):
            result += word1[l]
        if r < len(word2):
            result += word2[r]
        r += 1
        l += 1
    return result


print(mergeAlternately(word1=word1, word2=word2))

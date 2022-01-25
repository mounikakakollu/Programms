'''
Given a string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.
The two identified subsequences A and B can use the same ith character from string str
if and only if that ith character has different indices in A and B.

Input:
str = "axxxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x x y
0 1 2 3 4

The longest subsequence is "xx".
It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str


subsequence B
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of str

We are able to use character 'x'
(at index 2 in str) in both subsequences
as it appears on index 1 in subsequence A
and index 0 in subsequence B.
'''
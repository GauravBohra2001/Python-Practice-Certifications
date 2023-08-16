#Question1

# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

#My solution Version1
# s = "luffy is still joyboy"
# without_space = s.strip()
# with_comma = without_space.replace(" ", ",")
# with_comma_lst = list(with_comma)
# count = 0
# for i in range(len(with_comma_lst)-1,-1,-1):
#     if with_comma_lst[i] == ",":
#         break
#     count = count + 1
# print(count)

#My solution version2
# s = "luffy is still joyboy"
# count = 0
# without_space = s.strip()
# for i in range(len(without_space)-1,-1,-1):
#     if without_space[i] == " ":
#         break
#     count = count + 1
# print(count)

#Someone else solution
# aux=s.split()
# print(aux)
# print(len(aux[-1]))


#Question2

# 66. Plus One
# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


#I glanced at the solution then did it on my own
# digits = [1,2,3]
# num_str = ""
# for i in digits:
#     num_str = num_str + str(i)

# num_int = str(int(num_str)+1)

# output_lst = []
# for i in num_int:
#     a = int(i)
#     output_lst.append(a)
# print(output_lst)


#Question3

#136. Single Number

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# nums = [4,1,2,1,2]
# for i in range(0, len(nums)):
#     if nums.count(nums[i]) > 1:
#         continue
#     else:
#         print(nums[i])


#Question4
#414. Third Maximum Number

#Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

#Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

#Not my solution
# nums = [2,2,3,1]
# if len(sorted(set(nums), reverse=True)) < 3:
#     print(max(nums))
# else:
#     print(sorted(set(nums),reverse=True)[2])


#Question5
#448. Find All Numbers Disappeared in an Array

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

#My solution was this but there was time complexity
# nums = [4,3,2,7,8,2,3,1]
# lst = []
# for i in range(1, len(nums)+1):
#     if i not in nums:
#         lst.append(i)
# print(lst)

#So this was suggested by chat gpt
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# nums_set = set(nums)
# lst = []
# for i in range(1, len(nums) + 1):
#     if i not in nums_set:
#         lst.append(i)
# print(lst)


#Question6
#455. Assign Cookies

# Example 1:

# Input: g = [1,2,3], s = [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

# Example 2:

# Input: g = [1,2], s = [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the children, 
# You need to output 2.

# g = [10, 9, 8, 7]
# s = [5, 6, 7, 8]
# g.sort(reverse=True)
# s.sort(reverse=True)
# g_i = 0
# s_i = 0
# content = 0
# while g_i < len(g) and s_i < len(s):
#     if s[s_i] >= g[g_i]:
#         content += 1
#         s_i += 1
#     g_i += 1
# print(content)


#Question7
#202. Happy Number

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# Output: false

#This is mine after understanding from youtube and this is not work for some of the test cases
# n = 19
# s = set()
# while n > 0:
#     sum = 0
#     digits = n % 10
#     n = n // 10
#     sum = sum + digits**2

#     if sum == 1:
#         print("True")
#         break

#     else:
#         if sum in s:
#             print("False")
#             break
#         else:
#             s.add(sum)
#             n = sum

#This is the chatgpt solution
# n = 3
# s = set()

# while n != 1:
#     sum = 0

#     while n > 0:
#         digits = n % 10
#         n = n // 10
#         sum = sum + digits ** 2

#     if sum in s:
#         print("False")
#         break
#     else:
#         s.add(sum)
#         n = sum
# else:
#     print("True")




# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.


# Example 1:
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
              
# Example 3:
# Input: n = 3
# Output: false


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
           return True
        else:
            if n % 2 == 0:
                for i in range(0, n):
                    a = 2**i
                    if a == n:
                        return i
                        break
                else:
                    return False
            else:
                return False


# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 




#Leetcode question
##New question
#finding the count of the longest sequence of 1 from the below string
#'010101100001111'
#output 4

n = '01010110011111001111'
count = 0
max_count = 0
for i in n:
    if i == '1':
        count = count + 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)






























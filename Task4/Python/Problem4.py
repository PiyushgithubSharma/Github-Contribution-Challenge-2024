'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

#Given code has used type conversion for solution come up with a code that not uses type conversion.
#You need to correct complete function body.
#Do not change class name and method name.

class Solution:
    def addBinary(self, a: bin, b: bin) -> bin:
        num1 = bin(a, 2)
        num2 = bin(b, 2)
        
        result = num1 + num2
        
        result_binary = bin(result)[2:]
        
        return result_binary
a = Solution()
print(a.addBinary(1010,1011))


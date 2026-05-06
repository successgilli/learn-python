# - take input string
# - reverse the string and if it equals the input, it is a palindrome
def isPalindromeByBruteForce(s):
    return "".join(reversed(s)) == s

'''
- take input string
- Use two pointers
- start a pointer one at the start and the other at the end
- start a loop, for each string character, if start pointer val equals end pointer val, continue
- If not, return false
- After the loop exits, return True
'''
def isPalindromeTwoPointers(s: str) -> bool:
    startPnt = 0
    endPnt = len(s) - 1

    while startPnt < endPnt:
        if s[startPnt] != s[endPnt]:
            return False
        
        startPnt += 1
        endPnt -= 1
    
    return True


print(isPalindromeByBruteForce("racecar"))
print(isPalindromeTwoPointers("racecar"))

class Solution:
    def isPalindrome(self, s: str) -> bool:
    # start 2 pointers, one from the back and one from the front
    # only compare the alphanumeric chars, ignore the others
    # if they dont match then gone

        back = len(s) - 1
        front = 0
        while (back >= front):
            if(not s[back].isalnum()):
                back = back - 1
            elif(not s[front].isalnum()):
                front = front + 1
            else:
                if(s[back].lower() == s[front].lower()):
                    back = back - 1
                    front = front + 1
                else:
                    return False
 
        return True



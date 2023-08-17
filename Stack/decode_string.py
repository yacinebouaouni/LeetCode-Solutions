class Solution:
    def decodeString(self, s: str) -> str:

        stack = list()

        for char in s:

            if char != ']':
                stack.append(char)

            else:
                # Find all char up to [
                currString = ""
                while stack[-1] != '[':
                    currString = stack.pop() + currString
                
                stack.pop()

                # Get all the digits
                currNum = ""
                while stack and stack[-1].isdigit():
                    currNum = stack.pop() + currNum
                
                stack.append(currString * int(currNum))


        return "".join(stack)

            

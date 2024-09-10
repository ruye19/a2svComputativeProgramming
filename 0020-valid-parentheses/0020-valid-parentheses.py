class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        cto={ ")":"(" , "}":"{" ,"]":"["}
        for c in s:
            if c in cto:
                if stack and stack[-1]==cto[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        return True if not stack else False         
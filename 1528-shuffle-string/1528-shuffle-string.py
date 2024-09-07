class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled = [''] * len(s)
    
        # Step 2: Iterate through the string and place each character at the correct index
        for i, char in enumerate(s):
            shuffled[indices[i]] = char
        
        # Step 3: Join the list into a final string and return it
        return ''.join(shuffled)

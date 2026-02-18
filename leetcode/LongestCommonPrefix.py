class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        a=strs[0]
        
        for i in strs[1:]:
            while not i.startswith(a):
                a=a[:-1]

                if a=="":
                    return ""
        
        return a

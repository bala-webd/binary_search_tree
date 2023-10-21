class Solution(object):
    def longestCommonPrefix(self, strs):
        prefixes = {}
        for string in strs:
            for i in range(len(string)):
                if len(string) - 1 != i:
                    key = string[i] + string[i+1]
                    if prefixes.get(key, None):
                        prefixes[key] += 1
                    else:
                        prefixes[key] = 1
                else:
                    prefixes[string] = 1
        print("prefixes", prefixes)


sol = Solution()
print("Method call", sol.longestCommonPrefix(["Bala", "Muruga", "Balance"]))

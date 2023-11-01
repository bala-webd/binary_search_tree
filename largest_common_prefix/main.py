class Solution(object):
    def longestCommonPrefix(self, strs):
        prefixes = {}
        consider_one = False
        for string in strs:
            if len(strs) == 1 and len(string) == 1:
                consider_one = True
            for i in range(len(string)):
                position = i+1
                desired_prefix = string[:position]
                detected_prefix = prefixes.get(desired_prefix, 0)
                if detected_prefix:
                    prefixes[desired_prefix] += 1
                else:
                    prefixes[desired_prefix] = 1
        largest_count = 0
        largest_prefix = ""
        for prefix, count in prefixes.items():
            if (count > largest_count or (largest_count != 0 and count == largest_count)) and count == len(strs):
                largest_count = count
                largest_prefix = prefix
        if largest_count == 0 or (not consider_one and largest_count == 1):
            return ""
        return largest_prefix


sol = Solution()
# print("Method call", sol.longestCommonPrefix(["flower", "flow", "flight"]))
# print("Method call", sol.longestCommonPrefix(["dog", "racecar", "car"]))
# print("Method call", sol.longestCommonPrefix(["a"]))
print("Method call", sol.longestCommonPrefix(
    ["flower", "flower", "flower", "flower"]))
